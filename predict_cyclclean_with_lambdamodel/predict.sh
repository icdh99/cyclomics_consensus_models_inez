#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=48:00:00
#SBATCH --mem=20G
#SBATCH --partition=gpu
#SBATCH --gpus-per-node=1

region=$1 # make into $ argument

for coverage in 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 20+
do

hdf5=/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/predict_cyclomics_clean/predict_dnn_ref_0-10_"$region"_"$coverage".hdf5
model='/hpc/compgen/projects/gw_cfdna/snv_qs/lambda_analysis/files_for_model/simulationsv5/make_matrices/models/model-dnn-c20ref-final.h5'
name="/hpc/compgen/projects/gw_cfdna/snv_qs/predict_cyclclean_with_lambdamodel/fastq/predict_cycl_clean_dnn20Xref_lambda_"$region"_"$coverage".fastq"

echo $model
echo $name
echo $hdf5

python predict_qs.py $model $name $hdf5
echo ""

done




