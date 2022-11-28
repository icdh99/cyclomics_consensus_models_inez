import os
import pysam
import pandas as pd

# bam_input = '/hpc/compgen/projects/gw_cfdna/gw_cyclomics/analysis/lchen/cycloseq-output/HC02_CYC36-20ng/bams/HC02_CYC36-20ng.tagged.bam'
bam_input = '/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_wgs_cons_intersect/cons_gwcycl_intersect.sorted.bam'
csv_file = f'csv_files/cycl_wgs_cons_t2t.csv'

with open(csv_file, 'w') as file:
    file.truncate(0)
    header = ['chr', 'cons-readid', 'cons-NM', 'cons-align_length', 'cons-cigar', 'cons-score', 'model-cov', 'cons-YR', 'cons-YM']
    file.write(','.join(header))
    file.write('\n')

nr_reads_check = 0
bamfile = pysam.AlignmentFile(bam_input, 'rb')
model_cov = 'Cycas Consensus'
with open(csv_file, 'a') as file:
    for read in bamfile.fetch():
        if read.has_tag('YM'):
            chr = read.reference_name
            id_clean = read.query_name.split('_')[0]
            nm = read.get_tag('NM')
            aln_length = read.query_alignment_length
            score = nm / aln_length
            cigar = read.cigarstring
            ym = read.get_tag('YM')
            yr = read.get_tag('YR')
            line = [str(chr), id_clean, str(nm), str(aln_length), cigar, str(score), model_cov, str(ym), str(yr)]
            file.write(','.join(line))
            file.write('\n')
            nr_reads_check += 1
print(f'total nr reads: {nr_reads_check}')

 
df = pd.read_csv('csv_files/cycl_wgs_cons_t2t.csv')
print(f'number of reads before chromosome selection: {df.shape}')
print(df.head())

## print count per contigs for each model
print(f'chromosome counts for {model_cov} reads:')
print(df[df['model-cov'] == model_cov]['chr'].value_counts())



# edit dataframe so that only normal chromosomes remain
# save to new csv file

chromosomes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', 'X', 'Y'] 

df_select_chr = df.loc[df['chr'].isin(chromosomes)]
print(f'number of reads after chromosome selection: {df_select_chr.shape}')
df_select_chr.to_csv('csv_files/cycl_wgs_cons_t2t_select_chr.csv')

# print count per contigs for each model
print(f'chromosome counts for {model_cov} reads:')
print(df_select_chr[df_select_chr['model-cov'] == model_cov]['chr'].value_counts())
  