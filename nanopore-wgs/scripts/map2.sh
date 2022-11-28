#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=10:00:00
#SBATCH --mem=10G

# reference_genome='/hpc/compgen/projects/nanoxog/raw/benchmark/jain/genomes/Homo_sapiens.fna'
# fastq='/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/Notts/FAB39088-288418386_Multi/all_basecalls_FAB39088.fastq'
# output_name='all_basecalls_FAB39088'

# reference_genome='/hpc/compgen/GENOMES/CHM13_t2t_v2/chm13v2.0.fa'
# reference_genome='/hpc/compgen/GENOMES/CHM13_t2t/chm13.draft_v1.1.fa'
# fastq='/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/reads.fastq.gz.aa'
# output_name='reads_chr18'


# samtools sort reads_chr18_withheader.bam -o reads_chr18_withheader.sorted.bam
# samtools index reads_chr18_withheader.sorted.bam
# samtools view -bh -F 260 -F 20 reads_chr18_withheader.sorted.bam chr18 > reads_chr18_withheader_chr18.sorted.bam
# samtools index reads_chr18_withheader_chr18.sorted.bam
# samtools idxstats reads_chr18_withheader.sorted.bam
# samtools view -bh -F 260 -F 20 reads_chr18_withheader.sorted.bam chr18 > reads_chr18_withheader.sorted.bam    # filter for chr18, primary aligned, mapped, forward strand

# echo reads_chr18_withheader.sorted.bam
# samtools idxstats reads_chr18_withheader.sorted.bam

# echo reads_chr18_withheader_chr18.sorted.bam
# samtools idxstats reads_chr18_withheader_chr18.sorted.bam

# samtools coverage -m reads_chr18_withheader_chr18.sorted.bam

# samtools coverage -m -r chr18:50999980-71000021 reads_chr18_withheader_chr18.sorted.bam

# echo 'filter reads.sorted.bam for chr18'
# samtools view -bh -F 260 -F 20  /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/rel8/reads.sorted.bam > /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/rel8/reads_chr18_filtered.sorted.bam

samtools view -bh -F 260 -F 20 /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/reads_withheader.sorted.bam chr17 > /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/reads_withheader_chr17.sorted.bam
samtools index /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/reads_withheader_chr17.sorted.bam
samtools idxstats /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/reads_withheader_chr17.sorted.bam