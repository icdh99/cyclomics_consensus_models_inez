#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=60:00:00
#SBATCH --mem=50G
#SBATCH --cpus-per-task=64

# reference_genome='/hpc/compgen/projects/nanoxog/raw/benchmark/jain/genomes/Homo_sapiens.fna'
# fastq='/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/Notts/FAB39088-288418386_Multi/all_basecalls_FAB39088.fastq'
# output_name='all_basecalls_FAB39088'

# reference_genome='/hpc/compgen/GENOMES/CHM13_t2t_v2/chm13v2.0.fa'
reference_genome='/hpc/compgen/GENOMES/CHM13_t2t/chm13.draft_v1.1.fa'
fastq='/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/reads.fastq.gz.aa'
output_name='reads_chr18'

# minimap2 -ax map-ont -t 64 $reference_genome $fastq > $output_name.sam 

# samtools view -S -bh $output_name.sam > $output_name.bam  # option -h to include header in bam file
samtools sort $output_name.bam -o $output_name.sorted.bam
samtools view -bh -F 260 -F 20 $output_name.sorted.bam chr18 > $output_name.sorted.bam    # filter for chr18, primary aligned, mapped, forward strand
samtools index $output_name.sorted.bam

# rm $output_name.bam $output_name.sam 

samtools idxstats $output_name.sorted.bam

samtools coverage -m $output_name.sorted.bam

samtools coverage -m -r chr18:61000000-82000001 $output_name.sorted.bam

# echo 'filter reads.sorted.bam for chr18'
# samtools view -bh -F 260 -F 20 -r chr18 /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/rel8/reads.sorted.bam > /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/rel8/reads_chr18_filtered.sorted.bam