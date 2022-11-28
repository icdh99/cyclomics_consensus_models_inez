#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=48:00:00
#SBATCH --mem=10G
#SBATCH --partition=gpu
#SBATCH --gpus-per-node=1

# chromosome=$1
# model_coverage=$2

for chromosome in chr21 chr22 chrX chrY
do 
    for model_coverage in 5 10 15 20 100
    do
    echo 'Chromosome: ' $chromosome
    echo 'Model coverage: ' $model_coverage

    model="/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/model_maskrefbase/model_dnn_c"$model_coverage"_finalmodel/model_dnn_c"$model_coverage"_finalmodel.h5"
    name="/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_wgs_fastq_maskedrefbase/predict_gwcycl_dnn_c"$model_coverage"_"$chromosome".fastq"
    hdf5="/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_wgs_hdf5_maskedrefbase/predict_dnn_"$chromosome".hdf5"

    echo $model
    echo $name
    echo $hdf5

    ls $model
    ls $hdf5

    # # # source /hpc/compgen/users/idenhond/miniconda
    # # # source activate tf
    python predict_qs.py $model $name $hdf5

    done

done


