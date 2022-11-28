#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=48:00:00
#SBATCH --mem=10G
#SBATCH --partition=gpu
#SBATCH --gpus-per-node=1

model_coverage=$1
model_type=$2
model="/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/model/model_"$model_type"_c"$model_coverage"_finalmodel/model_"$model_type"_c"$model_coverage"_finalmodel.h5"

source activate tf

for region in region1 region2 region3 region4 region5
do
list_files="/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_hdf5/predict_"$model_type"_ref_0-10_"$region"_"*".hdf5"
    for hdf5 in $list_files
    do
    hdf5_cov=$(echo $hdf5 | cut -d'/' -f 10 | cut -d'_' -f 6 | cut -d'.' -f 1)
    name="/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_fastq/predict_cyclclean_"$model_type"_c"$model_coverage"_"$region"_"$hdf5_cov"X.fastq"
    echo $hdf5
    echo $model
    echo $name
    echo $hdf5_cov
    
    python predict_qs.py $model $name $hdf5

    done
echo $'\n'
done



