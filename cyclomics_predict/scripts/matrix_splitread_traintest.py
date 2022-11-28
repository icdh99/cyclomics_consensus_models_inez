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
    def __init__(self, vcf_file, bam_file, cov, add_ref, refseq, readid, hdf5file, window = 0):
        self.window = window; 
        self.cov = cov
        if self.cov == 20:x_size = 1134
        if self.cov == 5: x_size = 324   
        self.bam = utils_lambda.read_bam(bam_file); 
        # self.consensus = utils_lambda.read_bam(consensus_file)
        self.vcf_df = utils_lambda.read_vcf_pandas(vcf_file) 
        self.variants_iter = self.vcf_df[["CHROM", "POS"]].iterrows()
        i = 0                                                   # set counter for nr of variants
        self.super_max = 0   
        self.x_big = np.zeros((x_size,))
        self.y_big = np.zeros((6,))
        while i < self.vcf_df[["CHROM", "POS"]].shape[0]:
            xmat_perpos_list, ymat_perpos_list = self.get_mapped_features(i, add_ref, cov, x_size, refseq)   
            for xmat_perpos, ymat_perpos in zip(xmat_perpos_list, ymat_perpos_list):
                if len(xmat_perpos) == x_size and len(ymat_perpos == 6):
                    self.x_big = np.vstack((self.x_big, xmat_perpos))
                    self.y_big = np.vstack((self.y_big, ymat_perpos))
            i += 1
        self.x_big = np.delete(self.x_big, 0, 0)
        self.y_big = np.delete(self.y_big, 0, 0)
        print(f'{readid}: {self.x_big.shape}\t{self.y_big.shape}\tmax aligned: {self.super_max}')
        self.savehdf5(self.x_big, self.y_big, x_size, cov, readid, hdf5file)    

    def get_mapped_features(self,i, add_ref, cov, x_size, refseq):
        max = 0 
        (chromosome, position) = next(self.variants_iter)[1]
        # print(f"{chromosome}:{position}")
        listx = [[np.zeros((0,))] for x in range(5)]         # 5 is zelfgekozen nummer --> aanpassen naar iets groots en dan aan het einde de lege arrays verwijderen!!!!
        listy = [[np.zeros((0,))] for x in range(5)]
        for pileupcolumn in self.bam.pileup(chromosome, min_base_quality = 0):  
            if pileupcolumn.pos < position + 1 - round(self.window/2): continue
            elif pileupcolumn.pos >  position - 1 + round(self.window/2): break
            else:
                pos_base = pileupcolumn.pos + 1
                if pileupcolumn.get_num_aligned() > max: max = pileupcolumn.get_num_aligned()
                boqs = pileupcolumn.get_query_qualities()
                seq = pileupcolumn.get_query_sequences(add_indels=True)  # reverse strand is small cap in bases.
                chunks_seq = [(seq[x:x+cov]) for x in range(0, len(seq), cov)]
                chunks_boqs = [(boqs[x:x+cov]) for x in range(0, len(boqs), cov)]
                for t, (list_seq, list_boqs) in enumerate(zip(chunks_seq, chunks_boqs)):
                    if type(listx[t])  == list: subx = listx[t][0]
                    else: subx = listx[t]
                    if type(listy[t]) == list: suby = listy[t][0]
                    else: suby = listy[t]
                    xmat, ymat = self.make_matrix(list_boqs, list_seq, pos_base, i, add_ref, x_size, refseq)   # list per position of window,
                    subx = np.hstack((subx, xmat))
                    suby = np.hstack((suby, ymat))
                    listx[t] = subx
                    listy[t] = suby
        listx = [e for e in listx if np.any(e)]     # remove empty arrays from list
        listy = [e for e in listy if np.any(e)]
        for pos, row in enumerate(listx): 
            listx[pos] = self.check_rows(row, x_size)
        if max > self.super_max: self.super_max = max
        return listx, listy                                     

    def check_rows(self, a, x_size):
        if a.shape != (x_size,):
            b = a.T.copy()
            b = np.resize(b, (x_size,)) # a complete row per position should have 9 bases in the window * 6 bases as coverage = length 54. dus dit is voor als je window te groot is voor de sequence, dan krijg j elege dingen rechts in je matrixje.
            a = b.T
        return a

    def make_matrix(self, boqs, seq, position, teller, add_ref, x_size, refseq):         # make a list per position of the window with all bases and quality scores
        seq = [item.upper() for item in seq]                    # change low caps bases
        seq = ["D" if base == "*" else base for base in seq]     # deletions

        vcf = self.vcf_df.values                             
        ymat = np.zeros((0,))   #empty array 
        xmat = np.zeros((0,))   #emtpy array

        

        if position == vcf[teller,1]: 
            base = vcf[teller,4]
            ymat = np.append(ymat, self.base_encode(base,1)) # alt = y
            if add_ref == 'ref':
                # output = subprocess.getoutput(f'samtools faidx /hpc/compgen/GENOMES/CHM13_t2t/chm13.draft_v1.1.fa chr17:{position-2}-{position-2}')
                # ref_base = output.split()[-1]
                ref_base = refseq[position-3]
                xmat = np.append(xmat, self.base_encode(ref_base)) # ref = x 
            elif add_ref ==  'noref':
                xmat = np.append(xmat, self.base_encode(random.choice(["A", "C", "G", "T", "D", "N"],))) 
        else:                                               
            if add_ref == 'ref':
                # output = subprocess.getoutput(f'samtools faidx /hpc/compgen/GENOMES/CHM13_t2t/chm13.draft_v1.1.fa chr17:{position-2}-{position-2}')
                # ref_base = output.split()[-1]
                ref_base = refseq[position-3]
                xmat = np.append(xmat, self.base_encode(ref_base)) # ref = x 
            elif add_ref == 'noref':
                xmat = np.append(xmat, self.base_encode(random.choice(["A", "C", "G", "T", "D", "N"],))) 
        for i in range(len(seq)):   
            qs = round(1 - (10**-((boqs[i])/10)), 10)
            xmat = np.append(xmat, self.base_encode(seq[i][0],qs))
        xmat = self.check_length(xmat, x_size)
        return xmat, ymat

    def check_length(self, a, x_size):
        a = np.resize(a, (int(x_size/9),))
        return a

    def base_encode(self, base, qs=1):
        mapper = {"A": 0, "C": 1, "G": 2, "T": 3, "D": 4, "N": 5}
        onehot_encoded = np.zeros((len(base), 6))
        for i, s in enumerate(base): onehot_encoded[i, mapper[s]] = qs                                                                 
        return onehot_encoded  
                  
    def savehdf5(self, x, y, x_size, cov, readid, hdf5_file):
        with h5py.File(f'{hdf5_file}_{readid}.hdf5', "a") as f:
            nr_samples = 500
            dx = f.create_dataset('x', data=x, maxshape=(None, x_size))
            dy = f.create_dataset('y', data=y, maxshape=(None, 6))
            dx.resize((nr_samples,x_size))
            dy.resize((nr_samples,6))
            # f.create_dataset(f'{readid}_x', data=x)
            # f.create_dataset(f'{readid}_y', data=y)

if __name__ == "__main__":
    vcffile = sys.argv[1]
    bam_file = sys.argv[2]
    txt_file = sys.argv[3]
    run_id = sys.argv[4]
    hdf5_file = sys.argv[5]
    cov = int(sys.argv[6])
    add_ref = sys.argv[7]
    print(cov, add_ref)
    print(sys.argv)

    # list of unique readids of the bamfile 
    with open(txt_file, 'r') as file:
        ids = file.read().splitlines()
    print(f'{len(ids)} ids') #221 ids

    # make an indexed version of the bam file where you can find the reads with a specific readid
    bam = pysam.AlignmentFile(bam_file)
    header = bam.header.copy()
    name_indexed_bam = pysam.IndexedReads(bam)
    name_indexed_bam.build()  

    # edit the readname so that only the readid is in the name
    # consensus = pysam.AlignmentFile(consensus_file)
    # outbam_consensus = pysam.AlignmentFile(f'{consensus_file}_{run_id}_new.bam', 'wb', template = consensus)
    # for read1 in consensus.fetch(until_eof=True):
    #     full = read1.query_name.split('_')
    #     name = full[0]
    #     read1.query_name = name
    #     outbam_consensus.write(read1)

    # make a readid indexable consensus file 
    # consensus2 = pysam.AlignmentFile(f'{consensus_file}_{run_id}_new.bam', ignore_truncation=True)
    # header_consensus = consensus2.header.copy()
    # name_indexed_consensus = pysam.IndexedReads(consensus2)
    # name_indexed_consensus.build()

    # print(f'new consensus bam file: {consensus_file}_{run_id}_new.bam')

    p = 0; q = 0; w = 0; failed_ids = []; v = 0

    # for all ids, try to find the reads with that id. exception if id is not found in consensus file
    for id in ids:
        w += 1
        try:
            # iterator_consensus = name_indexed_consensus.find(id)
            # out_consensus = pysam.Samfile(f'tmp_bamfiles_{run_id}/consensus_{id}.bam','wb', header = header)
            # for x in iterator_consensus:
                # out_consensus.write(x)
            iterator = name_indexed_bam.find(id)
            out = pysam.Samfile(f'tmpnormal_bamfiles_{run_id}/{id}.bam','wb', header = header)
            for x in iterator:
                out.write(x)
            p += 1
        except Exception as e:
            failed_ids.append(id)
            q += 1
            print(traceback.format_exc())
            exit()
            continue
    # ids_working = [v for v in ids if v not in failed_ids]
    with open('chr17.txt', 'r') as f:
            refseq = f.read().rstrip()
    for id in ids:
        try:
            # print(f'current read id: {run_id}/{id}')
            bamfile = f'tmpnormal_bamfiles_{run_id}/{id}.bam'
            pysam.index(bamfile)
            # count = pysam.AlignmentFile(bamfile).count()
            # consensusfile = f'tmp_bamfiles_{run_id}/consensus_{id}.bam'
            # pysam.index(consensusfile)
            # count2 = pysam.AlignmentFile(consensusfile).count()
            # print(f'{run_id}: nr mapped reads = {count}, nr consensus reads = {count2}')
            Features(vcffile, bamfile, cov,add_ref,refseq, id,hdf5_file,window=10)
        except Exception as e:
            v += 1
            print(e, f'id {id} is not working') 
            print(traceback.format_exc())

    # os.remove(f'{consensus_file}_{run_id}_new.bam')
    print(f'{len(ids)} original read ids')
    # print(f'{len(failed_ids)} failed read ids (no consensus sequence found)')
    print(f'{(v)} failed read ids during Features class')
    # print(f'{len(ids_working) - v} processed read ids for {bam_file}')
    # open file with matrices and check number of keys
    # with h5py.File(f'{hdf5_file}') as p:
    #         # print(f"Keys: {p.keys()}")
    #         print(f"Number of keys: {len(p.keys())}")
    logging.debug("done.\n")

end = time.time()
print("The time of execution is :", end-start)






def vcf_from_consensus(self, consensus_file):
    # consensus file has one read 
    # for read in consensus_file.fetch():
    #     print(read.query_name)
    with open(f'tmp_vcf_current_readid.vcf', 'w') as file:
        file.truncate(0)
        file.write('##fileformat=VCFv4.2'); file.write('\n')
        header = ["#CHROM", 'POS', 'ID', 'REF', 'ALT']
        file.write('\t'.join(header))
        file.write('\n')
        for pileupcolumn in consensus_file.pileup('chr17', min_base_quality = 0 ):
            base = pileupcolumn.get_query_sequences(add_indels=True)[0][0].upper()  # first item of list is first base, first item of base is base in case of indel 'T-1N'
            line = ["chr17", str(pileupcolumn.pos), ".", base, base]
            file.write('\t'.join(line))
            file.write('\n')
            # if len(pileupcolumn.get_query_sequences(add_indels=True)[0]) > 1:
            # print(pileupcolumn.get_query_sequences(add_indels=True)[0])
