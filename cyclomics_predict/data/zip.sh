#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=24:00:00
#SBATCH --mem=10G

file='/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/train_data_cnn_merged/train_data_cnn_noref_merged_0-10_region2.hdf5'
gzip -cv -1 $file > $file.gz
file='/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/train_data_cnn_merged/train_data_cnn_ref_merged_insaltv2_0-10.hdf5'
gzip -cv -1 $file > $file.gz
file='/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/predict_data_cnn/traintest_bam_region5_0-10_noref_alt_predict.hdf5'
gzip -cv -1 $file > $file.gz
file='/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/predict_data_cnn/traintest_bam_region5_0-10_ref_alt_predict.hdf5'
gzip -cv -1 $file > $file.gz
