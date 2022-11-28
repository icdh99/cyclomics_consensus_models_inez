import time
start = time.time()
import pysam
import sys
import matplotlib.pyplot as plt

# bam = '/hpc/compgen/projects/gw_cfdna/snv_qs/lambda_analysis/predict_cyclomics_pipeline/cycl_20runs.sorted.bam'
# bam = '/hpc/compgen/projects/gw_cfdna/snv_qs/lambda_analysis/scripts_cyclomics/dnn_noref_0_0_c20_noref.sorted.bam'
bam = sys.argv[1]
# bam = '/hpc/compgen/projects/gw_cfdna/snv_qs/lambda_analysis/data_cyclomics/000001_v3/Minimap2Align/SamtoolsMergeBams/fastq.merged.bam'
file = pysam.AlignmentFile(bam, "rb")

nr_mapped = 0
for contig in file.get_index_statistics():
    nr_mapped += contig[1]
    if contig[1] != 0:
        print(f'{contig[1]} reads mapped on {contig[0]}')

print(f'\n{nr_mapped} mapped reads')
print(f'{file.unmapped} unmapped reads')

nm_total = 0
read_length_total = 0
nr_reads = 0
errors = []

skip_contigs = ['BB22', 'BB24', 'BB25', 'BB41C']

for read in file.fetch('chr17', until_eof = False):  #
    if (read.reference_name in skip_contigs):
        continue
    nm = read.get_cigar_stats()[0][-1]

    read_length = read.query_alignment_length
    nm_total += nm
    read_length_total += read_length
    nr_reads += 1

score = nm_total / read_length_total * 100

print(f'\nbam file: {bam}')
print(f'score: {score}%')
print(f'score is based on {nr_reads} mapped reads')

file.close()

end = time.time()
print("\nThe time of execution is :", end-start)
print('\n')