fasta=/hpc/compgen/projects/gw_cfdna/snv_qs/raw/CYC000025-extended-data/CycasConsensus/FilterShortReads/FAU48563_pass_f5d283ba_0_filtered.fastq

wc -l $fasta

# head -4 $fasta

id=e92f1e63-d2d9-4e70-9643-f725eee3e15a

# grep $id $fasta | wc -l

# $(samtools view $bam chr17:7579211-7579352 | awk '{print $1}' | wc -l)

cat $fasta | awk '$1 ~ /^@/' | awk '{print $1}' | sort  | wc -l
cat $fasta | awk '$1 ~ /^@/' | awk '{print $1}' | sort | uniq | wc -l
