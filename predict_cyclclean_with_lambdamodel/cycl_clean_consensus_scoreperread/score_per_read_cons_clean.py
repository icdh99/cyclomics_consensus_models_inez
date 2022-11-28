import pysam

regions=['region1', 'region2', 'region3', 'region4', 'region5']

# csv_file = '/hpc/compgen/projects/gw_cfdna/snv_qs/predict_cyclclean_with_lambdamodel/cycl_clean_consensus_scoreperread/cycl_clean_consensus_properties_per_read.csv'

# with open(csv_file, 'w') as file:
#     file.truncate(0)
#     header = ['region', 'cons-readid', 'cons-readid-short', 'cons-NM', 'cons-YM', 'cons-YR', 'cons-align_length', 'cons-cigar', 'cons-score']
#     file.write(','.join(header))
#     file.write('\n')

# nr_reads_check = 0 
# for region in regions:
#     bamfile = pysam.AlignmentFile(f'/hpc/compgen/projects/gw_cfdna/snv_qs/predict_cyclclean_with_lambdamodel/cycl_clean_consensus_scoreperread/cyclomics_clean_consensus_{region}.bam', 'rb')
#     i = 0
#     with open(csv_file, 'a') as file:
#         for read in bamfile.fetch('chr17'):
#             id_clean = read.query_name.split('_')[0]
#             nm = read.get_tag('NM')
#             score = nm / read.query_alignment_length
#             if read.has_tag('YM'):
#                 line = [region, read.query_name, id_clean, str(read.get_tag('NM')), str(read.get_tag('YM')), read.get_tag('YR'), str(read.query_alignment_length), read.cigarstring, str(score)]
#                 file.write(','.join(line))
#                 file.write('\n')
#                 nr_reads_check += 1
#             i += 1
#     print(i)
# print(nr_reads_check)



csv_file_predictions = '/hpc/compgen/projects/gw_cfdna/snv_qs/predict_cyclclean_with_lambdamodel/cycl_clean_predictions_scoreperread/cycl_predictions_properties_per_read.csv'

regions=['region2', 'region3', 'region4', 'region5']
with open(csv_file_predictions, 'w') as file:
    file.truncate(0)
    header = ['region', 'pred-readid',  'pred-NM', 'pred-align_length', 'pred-cigar', 'pred-score']
    file.write(','.join(header))
    file.write('\n')

nr_reads_check = 0 
for region in regions:
    bamfile = pysam.AlignmentFile(f'/hpc/compgen/projects/gw_cfdna/snv_qs/predict_cyclclean_with_lambdamodel/predict_cyclclean_{region}_merged.sorted.bam', 'rb')
    i = 0
    with open(csv_file_predictions, 'a') as file:
        for read in bamfile.fetch('chr17'):
            # id_clean = read.query_name.split('_')[0]
            nm = read.get_tag('NM')
            score = nm / read.query_alignment_length
            line = [region, read.query_name,  str(read.get_tag('NM')), str(read.query_alignment_length), read.cigarstring, str(score)]
            file.write(','.join(line))
            file.write('\n')
            nr_reads_check += 1
            i += 1
    print(i)
print(nr_reads_check)