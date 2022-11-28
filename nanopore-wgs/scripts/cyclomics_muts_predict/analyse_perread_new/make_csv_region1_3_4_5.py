import os
import pysam


# PREDICTIONS
directory = '/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/cyclomics_muts_predict/analyse_perread_new/bam_perregion_pred'
csv_file = f'csv_files_perregion/cycl_muts_predict_t2t_perread.csv'
with open(csv_file, 'w') as file:
    file.truncate(0)
    header = ['region', 'region_readid', 'pred-readid', 'pred-readid-short', 'pred-NM', 'pred-align_length', 'pred-cigar', 'pred-score', 'model-cov', 'pred-model-only', 'pred-cov-only',  'mut1', 'mut2', 'mut3', 'mut4', 'mut5', 'NM-mut', 'cons-score-NM']
    file.write(','.join(header))
    file.write('\n')



for region in ['region1', 'region3', 'region4', 'region5']:
    print(region)
    nr_reads_check = 0 
    for filename in os.listdir(directory):
        if filename.endswith('.bam') and region in filename:
            print(filename)
            f = os.path.join(directory, filename)
            s1 = filename.split('.')[0].split('_')
            model_type = s1[3]
            coverage_model = s1[4]
            model_cov = model_type + '_' + coverage_model
            print(model_type, coverage_model)
            bamfile = pysam.AlignmentFile(f, 'rb')
            with open(csv_file, 'a') as file:
                for read in bamfile.fetch('chr17'):
                    id_clean = read.query_name.split('_')[0]
                    region_readid = region + '_' + id_clean
                    nm = read.get_tag('NM')
                    score = nm / read.query_alignment_length
                    line = [region, region_readid, read.query_name, id_clean, str(read.get_tag('NM')), str(read.query_alignment_length), read.cigarstring, str(score), model_cov, model_type, coverage_model, str(0), str(0), str(0), str(0), str(0), str(0), str(0)]
                    file.write(','.join(line))
                    file.write('\n')
                    nr_reads_check += 1
            print(f'total nr reads: {nr_reads_check}')


