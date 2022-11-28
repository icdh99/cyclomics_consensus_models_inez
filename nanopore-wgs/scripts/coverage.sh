#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=24:00:00
#SBATCH --mem=20G

# bamfile='/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/all_basecalls_FAB49164.sorted.bam'
# echo $bamfile

# # average coverage for all covered regions
# samtools depth $bamfile | awk '{sum+=$3} END { print "Average = ",sum/NR}'

# total_size = ${samtools view -H $bamfile | grep -P '^@SQ' | cut -f 3 -d ':' | awk '{sum+=$1} END {print sum}'}
# echo $total_size

# # average X coverage (calculated over whole genome)
# samtools depth $bamfile | awk '{sum+=$3} END { print "Average = ",sum/'$total_size'}'

bamfile='/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/bam_files/all_basecalls_merged.bam'

echo $bamfile

samtools coverage -m $bamfile

