#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=48:00:00
#SBATCH --mem=10G
#SBATCH --partition=gpu
#SBATCH --gpus-per-node=1


model_coverage=$1
model="/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/model/model_dnn_c"$model_coverage"_finalmodel/model_dnn_c"$model_coverage"_finalmodel.h5"

source activate tf

for region in region2 region3 region4 region5
do
list_files="/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/predict_cyclomics_clean/predict_dnn_ref_0-10_"$region"_"*".hdf5"
    for hdf5 in $list_files
    do
    hdf5_cov=$(echo $hdf5 | cut -d'/' -f 10 | cut -d'_' -f 6 | cut -d'.' -f 1)
    name="/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/predict_cyclomics_clean_fastq/predict_cyclclean_dnn_c"$model_coverage"_"$region"_"$hdf5_cov"X.fastq"
    echo $hdf5
    echo $model
    echo $name
    echo $hdf5_cov

    python predict_qs.py $model $name $hdf5
    done
echo $'\n'
done



