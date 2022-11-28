#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=100:00:00
#SBATCH --mem=40G
#SBATCH --partition=gpu
#SBATCH --gpus-per-node=1

# python model_dnn.py /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/train_data_dnn_merged/train_data_dnn_ref_merged_insaltv2_0-10.hdf5 dnn_ref_insaltv2_0-10_2309
# python model_dnn.py /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/train_data_dnn_merged/train_data_dnn_noref_merged_insaltv2_0-10_region2.hdf5 dnn_noref_insaltv2_0-10_2309
# python model_cnn.py /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/train_data_cnn/train_data_cnn_noref_merged_0-10.hdf5 cnn_noref_0-10_1909

# # cnn no ref indels region 2
# mkdir model_cnn_noref_insalt_0-10_region2_hyperopt
# cd model_cnn_noref_insalt_0-10_region2_hyperopt
# python ../model_cnn_with_tuner.py /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/train_data_cnn_merged/train_data_cnn_noref_merged_0-10_region2.hdf5 cnn_noref_insaltv2_region2_0-10_2609_hyperopt

# cnn ref indels region 2
mkdir model_cnn_ref_insalt_0-10_region2_hyperopt
cd model_cnn_ref_insalt_0-10_region2_hyperopt
python ../model_cnn_with_tuner.py /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/train_data_cnn_merged/train_data_cnn_ref_merged_insaltv2_0-10.hdf5 cnn_ref_insaltv2_region2_0-10_2609_hyperopt

# dnn no ref indels region 2
# mkdir model_dnn_noref_insalt_0-10_region2
# cd model_dnn_noref_insalt_0-10_region2
# python ../model_dnn.py /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/train_data_dnn_merged/train_data_dnn_noref_merged_insaltv2_0-10_region2.hdf5 dnn_noref_insaltv2_region2_0-10_2309

# dnn ref indels region 2
# mkdir model_dnn_ref_insalt_0-10_region2
# cd model_dnn_ref_insalt_0-10_region2
# python ../model_dnn.py /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/train_data_dnn_merged/train_data_dnn_ref_merged_insaltv2_0-10.hdf5 dnn_ref_insaltv2_region2_0-10_2309


# cnn no ref normal region 2
# mkdir model_cnn_noref_normal_0-10_region2
# cd model_cnn_noref_normal_0-10_region2
# python ../model_cnn.py /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_normal/train_data_cnn_merged/train_data_cnn_noref_merged_normal_region2_0-10.hdf5 cnn_noref_normal_region2_0-10_2309

# cnn ref normal region 2
# mkdir model_cnn_ref_normal_0-10_region2
# cd model_cnn_ref_normal_0-10_region2
# python ../model_cnn.py /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_normal/train_data_cnn_merged/train_data_cnn_ref_merged_normal_region2_0-10.hdf5 cnn_ref_normal_region2_0-10_2309

# dnn no ref normal region 2
# mkdir model_dnn_noref_normal_0-10_region2
# cd model_dnn_noref_normal_0-10_region2
# python ../model_dnn.py /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_normal/train_data_dnn_merged/train_data_dnn_noref_merged_normal_region2_0-10.hdf5 dnn_noref_normal_region2_0-10_2309

# dnn ref normal region 2
# mkdir model_dnn_ref_normal_0-10_region2
# cd model_dnn_ref_normal_0-10_region2
# python ../model_dnn.py /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_normal/train_data_dnn_merged/train_data_dnn_ref_merged_normal_region2_0-10.hdf5 dnn_ref_normal_region2_0-10_2309


# cnn no ref normal region 2 
# mkdir model_cnn_noref_normal_0-10_region2_hyperopt
# cd model_cnn_noref_normal_0-10_region2_hyperopt
# python ../model_cnn_normal_with_tuner.py /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_normal/train_data_cnn_merged/train_data_cnn_noref_merged_normal_region2_0-10.hdf5 cnn_noref_normal_region2_0-10_2609_optimized

# cnn ref normal region 2
# mkdir model_cnn_ref_normal_0-10_region2_optimized
# cd model_cnn_ref_normal_0-10_region2_optimized
# python ../model_cnn_normal_ref_optimized.py /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_normal/train_data_cnn_merged/train_data_cnn_ref_merged_normal_region2_0-10.hdf5 cnn_ref_normal_region2_0-10_2609_optimized
