#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=48:00:00
#SBATCH --mem=20G
#SBATCH --cpus-per-task=8

# ref=/hpc/compgen/GENOMES/CHM13_t2t/chm13.draft_v1.1.fa
ref=/hpc/compgen/GENOMES/CHM13_t2t_v2/chm13v2.0.fa

region=$1

fastq_merged=/hpc/compgen/projects/gw_cfdna/snv_qs/predict_cyclclean_with_lambdamodel/predict_cyclclean_"$region"_merged.fastq
name=/hpc/compgen/projects/gw_cfdna/snv_qs/predict_cyclclean_with_lambdamodel/predict_cyclclean_"$region"_merged
    
minimap2 -ax map-ont -t 8 $ref $fastq_merged > $name.sam
samtools view -S -b $name.sam > $name.bam
samtools sort $name.bam -o $name.sorted.bam
samtools index $name.sorted.bam
rm $name.bam $name.sam 
echo 'Merged fastq file: ' $fastq_merged
echo 'Resulting bam file: ' $name.sorted.bam

python score.py $name.sorted.bam

echo $'\n'


