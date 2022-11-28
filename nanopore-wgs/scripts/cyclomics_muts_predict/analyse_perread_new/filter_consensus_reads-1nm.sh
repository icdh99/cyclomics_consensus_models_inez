INPUT_BAM=/hpc/compgen/projects/gw_cfdna/snv_qs/raw/cyclomics_mutations_dataset_cleanconsensus/cyclomics_muts_consensus_chr17_YM3filter.sorted.bam
OUTPUT_BAM=cyclomics_muts_consensus_chr17_YM3filter_nm-1.sorted.bam
QNAME_FILE=readids_nm-1_cons.txt

samtools view -bh --qname-file $QNAME_FILE $INPUT_BAM > $OUTPUT_BAM
samtools index $OUTPUT_BAM

samtools view -c $OUTPUT_BAM
# samtools view $OUTPUT_BAM