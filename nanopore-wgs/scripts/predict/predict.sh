#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=48:00:00
#SBATCH --mem=10G
#SBATCH --partition=gpu
#SBATCH --gpus-per-node=1

date

model='/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/model/model_dnn_c15_2022-10-11_17:22/model-07.h5'
fastq='/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/predict_cyclomics_fastq/dnn_ref_0-10-c15_predict_cycl_region2_cov5_1215.fastq'
hdf5='/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/predict_cyclomics/predict_dnn_ref_0-10_region2_15.hdf5' #cyclomics reads with c10

echo $model
echo $fastq
echo $hdf5

python predict_qs.py $model $fastq $hdf5
