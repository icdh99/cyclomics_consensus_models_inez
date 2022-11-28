import os
import pysam


# PREDICTIONS
region = 'region3'
directory = '/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/cyclomics_muts_predict/analyse_perread_new/bam_perregion_pred'
csv_file = f'csv_files_perregion/cycl_muts_predict_t2t_perread_{region}.csv'
with open(csv_file, 'w') as file:
    file.truncate(0)
    header = ['region', 'region_readid', 'pred-readid', 'pred-readid-short', 'pred-NM', 'pred-align_length', 'pred-cigar', 'pred-score', 'model-cov', 'pred-model-only', 'pred-cov-only',  'mut1', 'mut2', 'mut3', 'mut4', 'mut5', 'NM-mut', 'cons-score-NM']
    file.write(','.join(header))
    file.write('\n')
nr_reads_check = 0 
for filename in os.listdir(directory):
    if filename.endswith('.bam') and region in filename:
        print(filename)
        f = os.path.join(directory, filename)
        print(f)
        s1 = filename.split('.')[0].split('_')
        model_type = s1[3]
        coverage_model = s1[4]
        model_cov = model_type + '_' + coverage_model
        print(model_type, coverage_model)
        bamfile = pysam.AlignmentFile(f, 'rb')
        with open(csv_file, 'a') as file:
            for pileupcolumn in bamfile.pileup("chr17", 7577899, 7577900, max_depth = 400000, min_base_quality = 0, truncate = True ):
                # 7577 899 in pileup is 7577900 mutations
                print(f'pileup column position: {pileupcolumn.pos}')
                count = 0
                print(pileupcolumn.get_query_sequences()[:100])
                print(len(pileupcolumn.get_query_sequences()))
                print(len(pileupcolumn.get_query_names()))

                for read in pileupcolumn.pileups:
                    # print(pileupread.alignment.query_name)
                    count += 1
                    id_clean = read.alignment.query_name.split('_')[0]
                    region_readid = region + '_' + id_clean
                    nm = read.alignment.get_tag('NM')
                    score = nm / read.alignment.query_alignment_length
                    line = [region, region_readid, read.alignment.query_name, id_clean, str(read.alignment.get_tag('NM')), str(read.alignment.query_alignment_length), read.alignment.cigarstring, str(score), model_cov, model_type, coverage_model, str(None), str(None), str(None), str(None), str(None), str(None), str(None)]
                    print(line)
                    break
                    file.write(','.join(line))
                    file.write('\n')

                print(f'total number of reads mapping to mutation position 1: {count}')
        break
        #     for read in bamfile.fetch('chr17'):
        #         id_clean = read.query_name.split('_')[0]
        #         region_readid = region + '_' + id_clean
        #         nm = read.get_tag('NM')
        #         score = nm / read.query_alignment_length
        #         line = [region, region_readid, read.query_name, id_clean, str(read.get_tag('NM')), str(read.query_alignment_length), read.cigarstring, str(score), model_cov, model_type, coverage_model, str(None), str(None), str(None), str(None), str(None), str(None), str(None)]
        #         file.write(','.join(line))
        #         file.write('\n')
        #         nr_reads_check += 1
        # print(f'total nr reads: {nr_reads_check}')

# region = 'region5'
# directory = '/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/cyclomics_muts_predict/analyse_perread_new/bam_perregion_pred'
# csv_file = f'csv_files_perregion/cycl_muts_predict_t2t_perread_{region}.csv'
# with open(csv_file, 'w') as file:
#     file.truncate(0)
#     header = ['region', 'region_readid', 'pred-readid', 'pred-readid-short', 'pred-NM', 'pred-align_length', 'pred-cigar', 'pred-score', 'model-cov', 'pred-model-only', 'pred-cov-only',  'mut1', 'mut2', 'mut3', 'mut4', 'mut5', 'NM-mut', 'cons-score-NM']
#     file.write(','.join(header))
#     file.write('\n')
# nr_reads_check = 0 
# for filename in os.listdir(directory):
#     if filename.endswith('.bam') and region in filename:
#         print(filename)
#         f = os.path.join(directory, filename)
#         s1 = filename.split('.')[0].split('_')
#         model_type = s1[3]
#         coverage_model = s1[4]
#         model_cov = model_type + '_' + coverage_model
#         print(model_type, coverage_model)
#         bamfile = pysam.AlignmentFile(f, 'rb')
#         with open(csv_file, 'a') as file:
#             for read in bamfile.fetch('chr17'):
#                 id_clean = read.query_name.split('_')[0]
#                 region_readid = region + '_' + id_clean
#                 nm = read.get_tag('NM')
#                 score = nm / read.query_alignment_length
#                 line = [region, region_readid, read.query_name, id_clean, str(read.get_tag('NM')), str(read.query_alignment_length), read.cigarstring, str(score), model_cov, model_type, coverage_model, str(None), str(None), str(None), str(None), str(None), str(None), str(None)]
#                 file.write(','.join(line))
#                 file.write('\n')
#                 nr_reads_check += 1
#         print(f'total nr reads: {nr_reads_check}')