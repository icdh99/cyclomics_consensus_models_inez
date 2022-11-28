BAM=/hpc/compgen/projects/gw_cfdna/snv_qs/raw/CYC000025-extended-data/CycasConsensus/MapqAndNMFilter/FAU48563_pass_f5d283ba_0_filtered_split.NM_50_mapq_20.bam
samtools sort $BAM -o inputbam.sorted.bam

# count number of unique read ids
echo 'nr unique readids in 'inputbam.sorted.bam ':' $(samtools view inputbam.sorted.bam| awk '{print $1}' | sort | uniq | wc -l)

# get header
samtools view -Hb inputbam.sorted.bam > header.sam

# # filter region 1 reads
# samtools view -bh inputbam.sorted.bam chr17:7574728-7574828 > filtered_step1.bam
# samtools sort filtered_step1.bam -o filtered_step1.sorted.bam
# samtools index filtered_step1.sorted.bam

# # count number of unique read ids 
# samtools view -c filtered_step1.sorted.bam
# echo 'nr unique readids in filtered_step1.sorted.bam :' $(samtools view $"filtered_step1.sorted.bam" | awk '{print $1}' | sort | uniq | wc -l)

# samtools view filtered_step1.sorted.bam | awk '{print $1}' | sort | uniq > name.txt

# for file in txtfiles/*
# do
#     # ls $file
#     name=$(echo $file | cut -d '.' -f 1 | cut -d '/' -f 2)
#     echo $name
#     samtools view --qname-file $file filtered_step1.sorted.bam > bamfiles-perreadid/$name.bam
#     samtools sort bamfiles-perreadid/$name.bam -o bamfiles-perreadid/$name.sorted.bam
#     samtools index bamfiles-perreadid/$name.sorted.bam
# done
# # bam to fastq
# # bedtools bamtofastq -i filtered_step1.sorted.bam -fq filtered_step1.fastq

# # wc -l filtered_step1.fastq
