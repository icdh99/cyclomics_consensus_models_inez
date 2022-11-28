#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=100:00:00
#SBATCH --mem=60G
#SBATCH --partition=gpu
#SBATCH --gpus-per-node=1

# CROSSVAL
date=$(date +%F_%R)
hdf5_folder="/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/traintest/chr18_$1/test"

# model_name="$1_$2_test"

model_path=$(find /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/model/model_$1_c$2_finalmodel -name '*.h5')
echo $model_path

echo "Type of network: $1"
echo "Coverage bin: $2"
echo "HDF5 folder: $hdf5_folder"
echo 'Model: ' $model_path

mkdir model_$1_c$2_test
cd model_$1_c$2_test

for i in 5 10 15 20 100
# for i in 5
do
model_name="$1_$2_test_$i"
echo "Model name: $model_name"
python ../model_$1_testdata.py $hdf5_folder $model_name $i $model_path
done


