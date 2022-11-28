#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=100:00:00
#SBATCH --mem=60G
#SBATCH --partition=gpu
#SBATCH --gpus-per-node=1

# TUNE 
date=$(date +%F_%R)
hdf5_folder="/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/traintest/traintest_maskedrefbase/chr18_$1_hypopt"

model_name="$1_$2_tuner"

echo "Type of network: $1"
echo "Coverage bin: $2"
echo "HDF5 folder: $hdf5_folder"
echo "Model name: $model_name"

echo "../model_$1_tuner.py'"

mkdir model_$1_c$2_tuner_$date
cd model_$1_c$2_tuner_$date
python ../model_$1_tuner.py $hdf5_folder $model_name $2



