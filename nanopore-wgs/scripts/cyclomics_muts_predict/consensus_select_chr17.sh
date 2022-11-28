#!/bin/bash

#SBATCH --mail-type=FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=4:00:00
#SBATCH --mem=2G

# ref=/hpc/compgen/GENOMES/CHM13_t2t_v2/chm13v2.0.fa

# name=cyclomics_muts_consensus

# mkdir perbase
# perbase base-depth -r $ref --max-depth 200000 /hpc/compgen/projects/gw_cfdna/snv_qs/raw/000025-sup-extended-data/SamtoolsMergeBams/fastq.merged.bam > perbase/$name.csv

# mkdir plots_errorrate
# python plot_predictions.py $name

samtools view -b /hpc/compgen/projects/gw_cfdna/snv_qs/raw/000025-sup-extended-data/SamtoolsMergeBams/fastq.merged.bam chr17 > cyclomics_muts_consensus_chr17.sorted.bam
# samtools sort cyclomics_muts_consensus_chr17.bam
samtools index cyclomics_muts_consensus_chr17.sorted.bam