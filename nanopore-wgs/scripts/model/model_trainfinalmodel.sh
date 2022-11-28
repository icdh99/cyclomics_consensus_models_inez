#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=30:00:00
#SBATCH --mem=20G
#SBATCH --partition=gpu
#SBATCH --gpus-per-node=1


# TRAIN FINAL MODEL
date=$(date +%F_%R)
hdf5_folder="/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/traintest/chr18_$1/train_val"
model_name="$1_$2_finalmodel"

echo "Type of network: $1"
echo "Coverage bin: $2"
echo "HDF5 folder: $hdf5_folder"
echo "Model name: $model_name"

echo "../model_$1_finalmodel.py'"

mkdir model_$1_c$2_finalmodel_$date
cd model_$1_c$2_finalmodel_$date
python ../model_$1_trainfinalmodel.py $hdf5_folder $model_name $2

