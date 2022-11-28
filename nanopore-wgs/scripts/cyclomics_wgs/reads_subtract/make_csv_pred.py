import os
import pysam
import pandas as pd

directory = '/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_wgs_bam_output_maskedrefbase_intersect'
csv_file = f'csv_files/cycl_wgs_predict_t2t.csv'

with open(csv_file, 'w') as file:
    file.truncate(0)
    header = ['chr', 'pred-readid', 'pred-NM', 'pred-align_length', 'pred-cigar', 'pred-score', 'model-cov']
    file.write(','.join(header))
    file.write('\n')

for filename in os.listdir(directory):
    if filename.endswith('.bam'):
        nr_reads_check = 0
        print(filename)
        model = filename.split('_')[2]
        cov = filename.split('_')[3].split('.')[0]
        model_cov = f'{model}_{cov}'
        print(model_cov)
        f = os.path.join(directory, filename)
        bamfile = pysam.AlignmentFile(f, 'rb')
        with open(csv_file, 'a') as file:
            for read in bamfile.fetch():
                chr = read.reference_name
                id_clean = read.query_name.split('_')[0]
                nm = read.get_tag('NM')
                aln_length = read.query_alignment_length
                score = nm / aln_length
                cigar = read.cigarstring
                line = [str(chr), id_clean, str(nm), str(aln_length), cigar, str(score), model_cov]
                file.write(','.join(line))
                file.write('\n')
                nr_reads_check += 1
        print(f'total nr reads: {nr_reads_check}')

df = pd.read_csv('csv_files/cycl_wgs_predict_t2t.csv')
print(df.shape)
print(df.head())

# print count per contigs for each model
# for model_cov in ['dnn_c5','dnn_c10','dnn_c15','dnn_c20','dnn_c100']:
#     print(f'chromosome counts for {model_cov} reads:')
#     print(df[df['model-cov'] == model_cov]['chr'].value_counts())
#     break

# edit dataframe so that only normal chromosomes remain
# save to new csv file

chromosomes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', 'X', 'Y'] 

df_select_chr = df.loc[df['chr'].isin(chromosomes)]
print(df_select_chr.shape)
df_select_chr.to_csv('csv_files/cycl_wgs_predict_t2t_select_chr.csv')

# print count per contigs for each model
# for model_cov in ['dnn_c5','dnn_c10','dnn_c15','dnn_c20','dnn_c100']:
#     print(f'chromosome counts for {model_cov} reads:')
#     print(df_select_chr[df_select_chr['model-cov'] == model_cov]['chr'].value_counts())
#     break