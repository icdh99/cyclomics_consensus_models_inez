

# python predict_qs.py $model $name $hdf5
#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=48:00:00
#SBATCH --mem=20G
#SBATCH --partition=gpu
#SBATCH --gpus-per-node=1

chromosome=$1
model_coverage

model='/hpc/compgen/projects/gw_cfdna/snv_qs/lambda_analysis/files_for_model/simulationsv5/make_matrices/models/model-dnn-c20ref-final.h5'
name='predict_gwcycl_dnn_c15_'
hdf5='/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_normal/train_data_dnn/traintest_bam_region5_0-10_ref_alt_predict.hdf5'

echo $model
echo $name.fastq
echo $hdf5

python predict_qs.py $model $name.fastq $hdf5
