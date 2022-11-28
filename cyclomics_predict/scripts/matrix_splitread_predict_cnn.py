
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
    def __init__(self, vcf, bam_file, cov, add_ref, refseq, readid, hdf5file, window = 0):
        self.window = window; 
        x_size = cov 
        self.bam = utils_lambda.read_bam(bam_file); 
        self.vcf_df = utils_lambda.read_vcf_pandas(vcf) 
        self.variants_iter = self.vcf_df[["CHROM", "POS"]].iterrows()
        i = 0                                                   # set counter for nr of variants
        self.super_max = 0   
        self.x_big = np.zeros((1,x_size+1,9,6))
        while i < self.vcf_df[["CHROM", "POS"]].shape[0]:
            xmat_perpos = self.get_mapped_features(i, add_ref, x_size, refseq)   
            if xmat_perpos.shape == (x_size+1,9,6):
                xmat_perpos = np.expand_dims(xmat_perpos, 0)
                self.x_big = np.concatenate((self.x_big, xmat_perpos))
            i += 1
        self.x_big = np.delete(self.x_big, 0, 0)
        print(f'{readid}: {self.x_big.shape}\tmax aligned: {self.super_max}')
        self.savehdf5(self.x_big, x_size, cov, readid, hdf5file)                        

    def get_mapped_features(self,i, add_ref, x_size, refseq):
        max = 0 
        completerowx = np.zeros((x_size+1,1,6)); 
        # completerowy = np.zeros((0,))
        (chromosome, position) = next(self.variants_iter)[1]
        for pileupcolumn in self.bam.pileup('chr17', 7579212, 7579351, min_base_quality = 0):   # REGION 5
            if pileupcolumn.pos < position + 1 - round(self.window/2): continue
            elif pileupcolumn.pos >  position - 1 + round(self.window/2): break
            else:
                pos_base = pileupcolumn.pos + 1
                if pileupcolumn.get_num_aligned() > max:
                    max = pileupcolumn.get_num_aligned()
                boqs = pileupcolumn.get_query_qualities()
                seq = pileupcolumn.get_query_sequences(add_indels=True)  # reverse strand is small cap in bases.
                xmat = self.make_matrix(boqs, seq, pos_base, i, add_ref, x_size, refseq)   # list per position of window, length of list is 202
                xmat = np.expand_dims(xmat, 1)
                completerowx = np.concatenate((completerowx, xmat), axis=1)
                # completerowy = np.hstack((completerowy, ymat))  # deze heb je niet nodig als het niet de vcf positie is....
        completerowx = self.check_rows(completerowx, x_size)

        if max > self.super_max: self.super_max = max
        return completerowx                                           

    def check_rows(self, a, x_size):
        a = np.delete(a, 0, 1)
        a.resize((x_size+1,9,6))
        # if a.shape != (x_size,):
        #     b = a.T.copy()
        #     b = np.resize(b, (x_size,)) # a complete row per position should have 9 bases in the window * 6 bases as coverage = length 54. dus dit is voor als je window te groot is voor de sequence, dan krijg j elege dingen rechts in je matrixje.
        #     a = b.T
        return a

    def make_matrix(self, boqs, seq, position, teller, add_ref, x_size, refseq):         # make a list per position of the window with all bases and quality scores
        seq = [item.upper() for item in seq]                    # change low caps bases
        seq = ["D" if base == "*" else base for base in seq]     # deletions

        vcf = self.vcf_df.values                             
        xmat = np.zeros((1,6))   #emtpy array

        if position == vcf[teller,1]: 
            if add_ref == 'ref':
                xmat = np.concatenate((xmat, self.base_encode(refseq[position-3]))) # ref = x 
            elif add_ref ==  'noref':
                xmat = np.concatenate((xmat, self.base_encode(random.choice(["A", "C", "G", "T", "D", "I"],)))) 
        else:                                               
            if add_ref == 'ref':
                xmat = np.concatenate((xmat, self.base_encode(refseq[position-3]))) # ref = x 
            elif add_ref == 'noref':
                xmat = np.concatenate((xmat, self.base_encode(random.choice(["A", "C", "G", "T", "D", "I"],)))) 
        for i in range(len(seq)):   #len(seq) ipv 10 was origineel. nu coverage 10: zodat alleen de eerste 10 bases per positie worden meegenomen. hier zou code wel echt sneller van moeten gaan, en je kan goed zien waar de insertions zitten omdat je dat print alleen voor degene die in de matrix uitkomen nu.
            qs = round(1 - (10**-((boqs[i])/10)), 10)
            xmat = np.concatenate((xmat, self.base_encode(seq[i][0],qs)))
        # xmat = self.check_length(xmat, x_size)
        xmat = np.delete(xmat, 0, 0)
        xmat.resize((x_size+1,6))
        return xmat

    def check_length(self, a, x_size):
        a = np.resize(a, (int(x_size/9),))
        return a

    def base_encode(self, base, qs=1):
        mapper = {"A": 0, "C": 1, "G": 2, "T": 3, "D": 4, "I": 5}
        onehot_encoded = np.zeros((len(base), 6))
        for i, s in enumerate(base): 
            onehot_encoded[i, mapper[s]] = qs                                                                 
        return onehot_encoded  
                  
    def savehdf5(self, x, x_size, cov, readid, hdf5_file):
        with h5py.File(f'{hdf5_file}', "a") as f:
            f.create_dataset(readid, data=x)
            # f.create_dataset('y', data=y)

if __name__ == "__main__":
    vcf_file = sys.argv[1]
    bam_file = sys.argv[2]
    txt_file = sys.argv[3]
    run_id = sys.argv[4]
    hdf5_file = sys.argv[5]
    cov = int(sys.argv[6])
    add_ref = sys.argv[7]

    print(vcf_file)
    print(bam_file)
    print(run_id)
    print(hdf5_file)
    print(cov, add_ref)

    with open(txt_file, 'r') as file:
        ids = file.read().splitlines()
    print(f'{len(ids)} ids')

    bam = pysam.AlignmentFile(bam_file)
    header = bam.header.copy()
    name_indexed = pysam.IndexedReads(bam)
    name_indexed.build()  
    with open('chr17.txt', 'r') as f: refseq = f.read().rstrip()
    v = 0
    w = 0
    for id in ids:
        try:
            iterator = name_indexed.find(id)
            out = pysam.Samfile(f'tmpnormal_bamfiles_{run_id}/{id}.bam','wb', header = header)
            for x in iterator: out.write(x)
        except Exception as e:
            print(e, f'id {id} is not working (index)')
            v += 1
    
    for id in ids:
        try:
            bamfile = f'tmpnormal_bamfiles_{run_id}/{id}.bam'
            pysam.index(bamfile)
            Features(vcf_file,bamfile,cov,add_ref,refseq, id,hdf5_file,window=10)
        except Exception as e:     
            print(e)
            print(f'id {id} is not working')    
            w += 1

    print(f'{len(ids)} original read ids')
    print(f'{v} failed read ids (no index)')
    print(f'{(w)} failed read ids during Features class')
    print(f'{len(ids) - (v+w)} processed read ids for {bam_file}')            
        
    with h5py.File(f'{hdf5_file}') as p: print(f"Number of keys: {len(p.keys())}")
    logging.debug("done.")

end = time.time()
print("The time of execution is :", end-start)