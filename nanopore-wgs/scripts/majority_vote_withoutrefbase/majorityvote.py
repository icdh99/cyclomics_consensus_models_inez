import time
start = time.time()
import pysam
import sys
import pandas as pd
import numpy as np
import random
import utils_lambda
import logging
from datetime import datetime
from collections import Counter
logging.basicConfig(format="%(filename)s:line%(lineno)d: %(message)s", level=logging.DEBUG)

class Features:
    def __init__(self, vcf, bam_file, cov, add_ref, out_file, window = 0):
        self.window = window
        x_size = 1134
        self.vcf_df = utils_lambda.read_vcf_pandas(vcf)
        self.bam = utils_lambda.read_bam(bam_file); 
        self.variants_iter = self.vcf_df[["CHROM", "POS"]].iterrows()
        i = 0   # set counter for nr of variants
        while i < self.vcf_df[["CHROM", "POS"]].shape[0]:
        # while i < 100:
            self.get_mapped_features(i, add_ref, x_size, out_file, cov) 
            i += 1
    
    def get_majority_vote(self, seq, position, teller, add_ref, x_size):
        vcf = self.vcf_df.values
        truth_base = vcf[teller,4]
        counter = Counter(seq)
        maj = max(counter, key=counter.get).upper()
        # if truth_base != maj:
            # print(position, ref, maj)
        return position, truth_base, maj

    def list_seq_add_ref(self, list_seq, pos_base, i, add_ref):
        vcf = self.vcf_df.values
        # if add_ref == 'ref': list_seq.append(vcf[i,3].lower())
        # else: list_seq.append(random.choice(["a", "c", "g", "t", '*']))
        return(list_seq)
    
    def write_to_file(self, pos, ref, maj, file):
        with open(f'{file}', 'a') as f:
            line = '\t'.join([str(pos), ref, maj])
            f.write(line)
            f.write('\n')

    def get_mapped_features(self,i, add_ref, x_size, out_file, cov):
        (chromosome, position) = next(self.variants_iter)[1]    
        # DETERMINE NR COVERAGE   
        
        
        if cov == 5: coverage_list = [3,4,5]
        if cov == 10: coverage_list = [6,7,8,9,10]
        if cov == 15: coverage_list = [11,12,13,14,15]
        if cov == 20: coverage_list = [16,17,18,19,20]
        if cov == 100: coverage_list = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

        coverage = coverage_list[i%(len(coverage_list))]

        for pileupcolumn in self.bam.pileup(f'{chromosome}', position -1, position, min_base_quality = 0):  
            if pileupcolumn.pos == position:
                seq = pileupcolumn.get_query_sequences(add_indels=True)
                # SUBSET COVERAGE
                seq = seq[:coverage]
                pos_base = pileupcolumn.pos
                list_seq_ext = seq
                # list_seq_ext = self.list_seq_add_ref(seq, pos_base, i, add_ref)
                # print(list_seq_ext)
                position, truth_base, maj = self.get_majority_vote(list_seq_ext, pos_base, i, add_ref, x_size)    
                # print(truth_base, maj)
                self.write_to_file(position, truth_base, maj, out_file)
                # chunks_seq = [(seq[x:x+x_size]) for x in range(0, len(seq), x_size)]
                # pos_base = pileupcolumn.pos + 1
                # for t, list_seq in enumerate(chunks_seq):
                #     list_seq_ext = self.list_seq_add_ref(list_seq, pos_base, i, add_ref)
                #     position, truth_base, maj = self.get_majority_vote(list_seq_ext, pos_base, i, add_ref, x_size)    
                #     self.write_to_file(position, truth_base, maj, out_file)
                  
if __name__ == "__main__":
    # nr = int(sys.argv[1])
    # cov = int(sys.argv[2])
    # add_ref = sys.argv[3]
    # allpos_or_mut = sys.argv[4]
    
    print(f'\ndate: {datetime.now()}')
    
    # if allpos_or_mut == 'allpos': 
    #     vcf_file = f'/hpc/compgen/projects/gw_cfdna/snv_qs/lambda_analysis/vcf_lambda/vcf_lambda_{nr}.vcf'
    #     bam_file = '/hpc/compgen/projects/gw_cfdna/snv_qs/lambda_analysis/files_for_model/simulationsv5/data/sim_7mer_750.sorted.bam'
    #     out_file = f'/hpc/compgen/projects/gw_cfdna/snv_qs/lambda_analysis/majority_vote/majorityvote_allpos_{cov}_{add_ref}_{nr}.txt'
    #     print(f'out folder for all pos: {out_file}')

    # if allpos_or_mut == 'mut':
    #     vcf_file = f'/hpc/compgen/projects/gw_cfdna/snv_qs/lambda_analysis/files_for_model/simulationsv5/vcf_files_lists/mut{nr}.vcf'
    #     bam_file = f'/hpc/compgen/projects/gw_cfdna/snv_qs/lambda_analysis/files_for_model/simulationsv5/data/sim_7mer_mutnew{nr}.sorted.bam'
    #     out_file = f'/hpc/compgen/projects/gw_cfdna/snv_qs/lambda_analysis/majority_vote/majorityvote_sim_{cov}_{add_ref}_{nr}.txt'
    #     print(f'out folder for mut: {out_file}')
    bam_file = sys.argv[1]
    vcf_file = sys.argv[2]
    cov = int(sys.argv[3])
    out_file = sys.argv[4]
    add_ref = 'ref'

    with open(out_file, 'w') as f:
        f.truncate(0)
        header = ['#pos', 'ref', 'maj']
        f.write('\t'.join(header))
        f.write('\n')

    pysam.index(bam_file)
    print(f'vcf file: {vcf_file}')
    print(f'bam file: {bam_file}')
    print(f'coverage: {cov}')
    print(f'add ref: {add_ref}')
    print(f'out file: {out_file}')

    try:
        Features(vcf_file, bam_file, cov, add_ref, out_file, window=0)
    except Exception as e:
        print(e)
        print(f'{bam_file} does not work.\n')

    logging.debug("done.")
    print('\n')

end = time.time()
print("The time of execution is :", end-start)