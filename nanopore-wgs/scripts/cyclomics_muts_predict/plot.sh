#!/bin/bash

#SBATCH --mail-type=FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=4:00:00
#SBATCH --mem=2G

ref=/hpc/compgen/GENOMES/CHM13_t2t_v2/chm13v2.0.fa

# model=$1
# cov=$2

# mkdir perbase

for region in region1 region2 region3 region4 region5
do 
    echo $region
    # name=predict_cycl_muts_"$model"_c"$cov"_merged
    # echo $name

    # perbase base-depth -r $ref --max-depth 200000 --bed-file $region.bed /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_bam_output/$name.sorted.bam > perbase/"$name"_"$region".csv


    # mkdir plots_errorrate
    # python plot_predictions.py $name $region


    # run perbase for consensus
    # now also contains reads with no YM tag
    perbase base-depth -r $ref --max-depth 200000 --bed-file $region.bed /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/cyclomics_muts_predict/cyclomics_muts_consensus_chr17_YM3filter_subsetreads.sorted.bam > perbase_subsetreads/cycl_muts_consensus_"$region".csv
done