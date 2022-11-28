#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=48:00:00
#SBATCH --mem=10G
#SBATCH --cpus-per-task=8
#SBATCH --output=R-%x.%j.out

# ls /hpc/compgen/projects/gw_cfdna/gw_cyclomics/analysis/lchen/cycloseq-output/HC02_CYC36-20ng/CycasConsensus/MapqAndNMFilter/*.bam
# cat /hpc/compgen/projects/gw_cfdna/gw_cyclomics/analysis/lchen/cycloseq-output/HC02_CYC36-20ng/CycasConsensus/MapqAndNMFilter/*.bam > gwcycl_mapqnmfilter_merged.bam

samtools sort gwcycl_mapqnmfilter_merged.bam -o gwcycl_mapqnmfilter_merged.sorted.bam
samtools index gwcycl_mapqnmfilter_merged.sorted.bam
BAM=gwcycl_mapqnmfilter_merged.sorted.bam
FASTQ=/hpc/compgen/projects/gw_cfdna/snv_qs/medaka/input_fastq_gwcycl_merged/gwcycl_mapqnmfilter_merged.fastq

samtools fastq -@ 8 $BAM > $FASTQ