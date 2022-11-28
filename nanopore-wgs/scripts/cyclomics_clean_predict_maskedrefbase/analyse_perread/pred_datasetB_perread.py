import os
import pysam

directory = '/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/predict_cyclomics_clean_bam_maskedrefbase'
csv_file = 'cycl_clean_predict_t2t_perread.csv'

with open(csv_file, 'w') as file:
    file.truncate(0)
    header = ['region', 'region_readid', 'pred-readid', 'pred-readid-short', 'pred-NM', 'pred-align_length', 'pred-cigar', 'pred-score', 'pred-model-cov', 'pred-read-cov']
    file.write(','.join(header))
    file.write('\n')

def check_region(start):
    start = int(start)
    if start >= 7574728 and start <= 7574828:
        region = 'region1'
    elif start >= 7577651 and start <= 7577788 :
        region = 'region2'
    elif start >= 7577813 and start <= 7577958:
        region = 'region3'
    elif start >= 7578281 and start <= 7578443 :
        region = 'region4'
    elif start >= 7579211 and start <= 7579352:
        region = 'region5'
    else: 
        region = 'region_unknown'
    return region

nr_reads_check = 0 
for filename in os.listdir(directory):
    if filename.endswith('.bam'):
        print(filename)
        f = os.path.join(directory, filename)
        s1 = filename.split('.')[0].split('_')
        # print(s1)
        coverage_model = s1[3]
        coverage_splitread = s1[5]
        # print(coverage_splitread)
        # print(coverage_model)
        bamfile = pysam.AlignmentFile(f, 'rb')
        with open(csv_file, 'a') as file:
            for read in bamfile.fetch('chr17'):
                # print(read.get_reference_positions()[0])
                region = check_region(read.get_reference_positions()[0])
                id_clean = read.query_name.split('_')[0]
                region_readid = region + '_' + id_clean
                nm = read.get_tag('NM')
                if nm == 'nan':
                    print('nan')
                score = nm / read.query_alignment_length
                line = [region, region_readid, read.query_name, id_clean, str(read.get_tag('NM')), str(read.query_alignment_length), read.cigarstring, str(score), coverage_model, coverage_splitread]
                file.write(','.join(line))
                file.write('\n')
                nr_reads_check += 1
        print(f'total nr reads: {nr_reads_check}')