#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=48:00:00
#SBATCH --mem=20G

bam=/hpc/compgen/projects/gw_cfdna/snv_qs/raw/Minimap2Align/SamtoolsMergeBams/FAU48563.merged.bam

echo 'Bam file: ' $bam
echo 'Number of reads in bam file: ' $(samtools view -c $bam)

samtools idxstats $bam

python score.py $bam
