import os
import pysam


# PREDICTIONS

directory = '/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_bam_output'
csv_file = 'cycl_muts_predict_t2t_perread.csv'

with open(csv_file, 'w') as file:
    file.truncate(0)
    header = ['region', 'region_readid', 'pred-readid', 'pred-readid-short', 'pred-NM', 'pred-align_length', 'pred-cigar', 'pred-score', 'model-cov', 'pred-model-only', 'pred-cov-only',  'mut1', 'mut2', 'mut3', 'mut4', 'mut5', 'NM-mut', 'cons-score-NM']
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
        model_type = s1[3]
        coverage_model = s1[4]
        model_cov = model_type + '_' + coverage_model
        # print(model_type, coverage_model)
        bamfile = pysam.AlignmentFile(f, 'rb')
        with open(csv_file, 'a') as file:
            for read in bamfile.fetch('chr17'):
                # print(read.get_reference_positions()[0])
                region = check_region(read.get_reference_positions()[0])
                id_clean = read.query_name.split('_')[0]
                region_readid = region + '_' + id_clean
                # print(region_readid)
                nm = read.get_tag('NM')
                # print(nm)
                # print(read.seq[7578324 - read.pos])

                score = nm / read.query_alignment_length
                # print(score)
                line = [region, region_readid, read.query_name, id_clean, str(read.get_tag('NM')), str(read.query_alignment_length), read.cigarstring, str(score), model_cov, model_type, coverage_model, str(None), str(None), str(None), str(None), str(None), str(None), str(None)]
                file.write(','.join(line))
                file.write('\n')
                nr_reads_check += 1
        print(f'total nr reads: {nr_reads_check}')



# CONSENSUS
regions=['region1', 'region2', 'region3', 'region4', 'region5']

csv_file = 'cycl_muts_consensus_t2t_perread.csv'

with open(csv_file, 'w') as file:
    file.truncate(0)
    header = ['region_readid', 'region', 'cons-readid', 'cons-readid-short', 'cons-NM', 'cons-YM', 'cons-YR', 'cons-align_length', 'cons-cigar', 'cons-score', 'model-cov', 'mut1', 'mut2', 'mut3', 'mut4', 'mut5', 'NM-mut', 'cons-score-NM']
    file.write(','.join(header))
    file.write('\n')

nr_reads_check = 0 
for region in regions:
    bamfile = pysam.AlignmentFile(f'/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/cyclomics_muts_predict/analyse_perread/cyclomics_mut_consensus_{region}.bam', 'rb')
    i = 0
    per_region=0
    with open(csv_file, 'a') as file:
        for read in bamfile.fetch('chr17'):
            id_clean = read.query_name.split('_')[0]
            region_readid = region + "_" + id_clean
            nm = read.get_tag('NM')
            score = nm / read.query_alignment_length
            if read.has_tag('YM'):
                line = [region_readid, region, read.query_name, id_clean, str(read.get_tag('NM')), str(read.get_tag('YM')), read.get_tag('YR'), str(read.query_alignment_length), read.cigarstring, str(score), 'Cycas Consensus', str(None), str(None), str(None), str(None), str(None), str(None), str(None)]
                file.write(','.join(line))
                file.write('\n')
                nr_reads_check += 1
                per_region+=1
            i += 1
    print(f'all reads in {region}: {i}')
    print(f'added reads in {region}: {per_region}')
print(f'all reads added to file: {nr_reads_check}')