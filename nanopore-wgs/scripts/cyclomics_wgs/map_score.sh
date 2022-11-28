#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=48:00:00
#SBATCH --mem=20G
#SBATCH --cpus-per-task=8
#SBATCH --output=R-%x.%j.out

"""
map for all chromosomes at once, for each model
"""
model_coverage=$1

fastq="/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_wgs_fastq_maskedrefbase/predict_gwcycl_dnn_c"$model_coverage"_allchrom.fastq" 
name="/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_wgs_bam_output_maskedrefbase/predict_gwcycl_dnn_c"$model_coverage"" 
ref='/hpc/compgen/GENOMES/hs37d5/hs37d5.fasta'

echo $fastq
echo $name
echo $ref

minimap2 -ax map-ont -t 8 $ref $fastq > $name.sam
samtools view -S -b $name.sam > $name.bam
samtools sort $name.bam -o $name.sorted.bam
samtools index $name.sorted.bam

rm $name.bam $name.sam 

samtools idxstats $name.sorted.bam

python score.py $name.sorted.bam

echo $name.sorted.bam
