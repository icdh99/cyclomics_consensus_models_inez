import pysam


# cyclomics clean dataset

bam_consensus_file = '/hpc/compgen/projects/gw_cfdna/snv_qs/raw/Minimap2Align/SamtoolsMergeBams/FAU48563.merged.bam'
bam_prediction_file = '/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/predict_cyclomics_clean_bam/predict_cyclclean_dnn_c5_merged_allcov.bam'

bam_consensus = pysam.AlignmentFile(bam_consensus_file, 'rb')
bam_prediction = pysam.AlignmentFile(bam_prediction_file, 'rb')


for read in bam_prediction.fetch():
    print(read.query_name)
    id_prediction = read.query_name
    break

for read in bam_consensus.fetch():
    if id_prediction in read.query_name and 'chr17' in read.query_name:
        print(read.query_name)
        id_consensus = read.query_name

print(f'number of reads in consensus file: {bam_consensus.count()}')
print(f'number of reads in prediction file: {bam_prediction.count()}')

# id_consensus = '6111dc69-765f-4a3b-a99c-2d1909d99909_I_0_chr1:3051460:3051661'
# id_prediction = '6111dc69-765f-4a3b-a99c-2d1909d99909_I_0_chr1:3051460:3051661'

name_indexed_consensus = pysam.IndexedReads(bam_consensus)
name_indexed_consensus.build()  
iterator = name_indexed_consensus.find(id_consensus)
header = bam_consensus.header.copy()
out = pysam.Samfile(f'tmp_bamfiles_consensus/{id_consensus}.bam','wb', header = header)
for x in iterator: out.write(x)

name_indexed_prediction = pysam.IndexedReads(bam_prediction)
name_indexed_prediction.build()  
iterator = name_indexed_prediction.find(id_prediction)
header = bam_prediction.header.copy()
out = pysam.Samfile(f'tmp_bamfiles_prediction/{id_prediction}.bam','wb', header = header)
for x in iterator: out.write(x)




