#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=48:00:00
#SBATCH --mem=20G

## RUN ON CPU WITH CONDA NANOPORE_SNV

name='dnn_ref_0-10-c15_predict_cycl_region2_cov5_1210'
fastq="/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/predict_cyclomics_fastq/$name.fastq"
ref='/hpc/compgen/GENOMES/CHM13_t2t/chm13.draft_v1.1.fa'
out="/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/predict_cyclomics_bam/$name"

echo $fastq
echo $out
echo $name

minimap2 -ax map-ont $ref $fastq > $out.sam
samtools view -S -b $out.sam > $out.bam
samtools sort $out.bam -o $out.sorted.bam
samtools index $out.sorted.bam

rm $out.bam $out.sam 

python score.py $out.sorted.bam
