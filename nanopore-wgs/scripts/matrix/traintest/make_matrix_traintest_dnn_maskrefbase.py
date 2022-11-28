#!/usr/bin/python3
import time
start = time.time()
import pysam
import sys
import pandas as pd
import numpy as np
import random
import utils_lambda
import logging
import h5py
import re
import os
import subprocess
import traceback
logging.basicConfig(format="%(filename)s:line%(lineno)d: %(message)s", level=logging.DEBUG)
 
class Features:
    def __init__(self, vcf_file, bam_file, add_ref, refseq, hdf5file, window = 0):
        self.window = window; 
        x_size = 1134 # matrix always gets this length
        self.bam = utils_lambda.read_bam(bam_file); 
        self.vcf_df = utils_lambda.read_vcf_pandas(vcf_file) 
        self.variants_iter = self.vcf_df[["CHROM", "POS"]].iterrows()
        i = 0                                                   # set counter for nr of variants
        self.super_max = 0   
        self.x_big = np.zeros((x_size,))
        self.y_big = np.zeros((6,))
        while i < self.vcf_df[["CHROM", "POS"]].shape[0]:
        # while i < 10:
            if i%1000 == 0:
                print(f'current nr: {i}')
            xmat_perpos, ymat_perpos = self.get_mapped_features(i, add_ref, x_size, refseq)   
            if len(xmat_perpos) == x_size and len(ymat_perpos == 6):
                self.x_big = np.vstack((self.x_big, xmat_perpos))
                self.y_big = np.vstack((self.y_big, ymat_perpos))
            i += 1
        self.x_big = np.delete(self.x_big, 0, 0)
        self.y_big = np.delete(self.y_big, 0, 0)
        print(f'{bam_file}: {self.x_big.shape}\t{self.y_big.shape}\tmax aligned: {self.super_max}')
        self.savehdf5(self.x_big, self.y_big, x_size, hdf5file)    

    def get_mapped_features(self,i, add_ref, x_size, refseq):
        max = 0 
        (chromosome, position) = next(self.variants_iter)[1]
        # print(f"{chromosome}:{position}")

        completerowx = np.zeros((0,))
        completerowy = np.zeros((0,))

        # coverage_list = [16,17,18,19,20]
        # coverage = coverage_list[i%5]

        chromosome = 'chr18'
        start = 50000000
        end = start + 600000
        for pileupcolumn in self.bam.pileup(chromosome, start, end, min_base_quality = 0):  
            if pileupcolumn.pos < position + 1 - round(self.window/2): continue
            elif pileupcolumn.pos >  position - 1 + round(self.window/2): break
            else:
                pos_base = pileupcolumn.pos + 1
                if pileupcolumn.get_num_aligned() > max: max = pileupcolumn.get_num_aligned()
                boqs = pileupcolumn.get_query_qualities()
                seq = pileupcolumn.get_query_sequences(add_indels=True)  # reverse strand is small cap in bases.
                seq = seq[:20] # synatx also works with seq < 20
                if len(seq) < 3: # discard samples with a coverage lower than the minimum coverage (=3)
                    return completerowx, completerowy   #these have size 0 so nothing is added to the big x and big y arrays
                xmat, ymat = self.make_matrix(boqs, seq, pos_base, i, add_ref, x_size, refseq)
                completerowx = np.hstack((completerowx, xmat))
                completerowy = np.hstack((completerowy, ymat))
                
        completerowx = self.check_rows(completerowx, x_size)
        if max > self.super_max: self.super_max = max
        return completerowx, completerowy                                  

    def check_rows(self, a, x_size):
        if a.shape != (x_size,):
            b = a.T.copy()
            b = np.resize(b, (x_size,)) 
            a = b.T
        return a

    def make_matrix(self, boqs, seq, position, teller, add_ref, x_size, refseq):    # make a list per position of the window with all bases and quality scores
        seq = [item.upper() for item in seq]                    # change low caps bases to upper 
        seq = ["D" if base == "*" else base for base in seq]    # deletions
        vcf = self.vcf_df.values                             
        ymat = np.zeros((0,))   
        xmat = np.zeros((0,))   
        if position == vcf[teller,1]: 
            base = vcf[teller,4]
            ymat = np.append(ymat, self.base_encode(base,1)) # alt = y
            if add_ref == 'ref':     # HERE ADD ZERO
                xmat = np.append(xmat, np.zeros((1, 6)))
                # ref_base = refseq[position-3] # xmat = np.append(xmat, self.base_encode(ref_base)) # ref = x           
            elif add_ref ==  'noref': xmat = np.append(xmat, self.base_encode(random.choice(["A", "C", "G", "T", "D"],))) 
        else:                                               
            if add_ref == 'ref':
                ref_base = refseq[position-3]
                xmat = np.append(xmat, self.base_encode(ref_base)) # ref = x 
            elif add_ref == 'noref': xmat = np.append(xmat, self.base_encode(random.choice(["A", "C", "G", "T", "D"],))) 
        for i in range(len(seq)):   
            qs = round(1 - (10**-((boqs[i])/10)), 10)
            if len(seq[i]) > 1:
                if seq[i][1] == '+': 
                    xmat = np.append(xmat, self.base_encode_insertion(seq[i][0],qs))
                    continue
            xmat = np.append(xmat, self.base_encode(seq[i][0],qs))
        xmat = self.check_length(xmat, x_size)
        return xmat, ymat

    def check_length(self, a, x_size):
        a = np.resize(a, (int(x_size/9),)) #126
        return a

    def base_encode_insertion(self, base, qs=1):
        mapper = {"A": 0, "C": 1, "G": 2, "T": 3, "D": 4, "N": 5}
        onehot_encoded = np.zeros((len(base), 6))
        for i, s in enumerate(base): onehot_encoded[i, mapper[s]] = qs 
        onehot_encoded[0, -1] = qs  
        return onehot_encoded  
                  
    def base_encode(self, base, qs=1):
        mapper = {"A": 0, "C": 1, "G": 2, "T": 3, "D": 4, "N": 5}
        onehot_encoded = np.zeros((len(base), 6))
        for i, s in enumerate(base): onehot_encoded[i, mapper[s]] = qs   
        return onehot_encoded  
                  
    def savehdf5(self, x, y, x_size, hdf5_file):
        with h5py.File(f'{hdf5_file}', "a") as f:
            f.create_dataset('x', data=x, compression="gzip", compression_opts=9)
            f.create_dataset('y', data=y, compression="gzip", compression_opts=9)

if __name__ == "__main__":
    vcffile = sys.argv[1]
    bam_file = sys.argv[2]
    hdf5_file = sys.argv[3]
    add_ref = sys.argv[4]
    print(sys.argv)
    with open('/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/ref_per_chromosome/chr18_v1.1.txt', 'r') as f: 
        lines = [line.rstrip('\n') for line in f]
        header = lines[0]; print(header)
        refseq = ''.join(lines[1:])

    try:
        Features(vcffile, bam_file,add_ref,refseq,hdf5_file,window=10)
    except Exception as e:
        print(e, f'something is not working') 
        print(traceback.format_exc())

    # open file with matrices and check number of keys
    with h5py.File(f'{hdf5_file}') as p:
        print(f"Number of keys: {len(p.keys())}")
        x = p['x'][()]
        print(x.shape)
        y = p['y'][()]
        print(y.shape)
    logging.debug("done.\n")

end = time.time()
print("The time of execution is :", end-start)



