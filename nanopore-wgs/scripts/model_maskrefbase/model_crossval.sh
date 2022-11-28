#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=200:00:00
#SBATCH --mem=20G
#SBATCH --partition=gpu
#SBATCH --gpus-per-node=1

# CROSSVAL
# for loop for DNN crossval

# for coverage in 5 10 15 20 100
# do
# date=$(date +%F_%R)
# hdf5_folder="/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/traintest/traintest_maskedrefbase/chr18_$1_train"
# model_name="$1_"$coverage"_finalmodel"

# echo "Type of network: $1"
# echo "Coverage bin: $coverage"
# echo "HDF5 folder: $hdf5_folder"
# echo "Model name: $model_name"

# echo "../model_$1_finalmodel.py'"

# mkdir model_$1_c"$coverage"_finalmodel_$date
# cd model_$1_c"$coverage"_finalmodel_$date
# python ../model_$1_trainfinalmodel.py $hdf5_folder $model_name $coverage
# cd ..

# done


coverage=$2

date=$(date +%F_%R)
hdf5_folder="/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/traintest/traintest_maskedrefbase/chr18_$1_train"

model_name="$1_"$coverage"_crossval"

echo $date

echo "Type of network: $1"
echo "Coverage bin: $coverage"
echo "HDF5 folder: $hdf5_folder"
echo "Model name: $model_name"

echo "../model_$1_crossval.py'"

mkdir model_$1_c"$coverage"_crossval_$date
cd model_$1_c"$coverage"_crossval_$date
python ../model_$1_crossval.py $hdf5_folder $model_name $coverage
cd ..



