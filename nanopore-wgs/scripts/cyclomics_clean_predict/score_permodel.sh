#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=1:00:00
#SBATCH --mem=2G


bam=/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/predict_cyclomics_clean_bam/predict_cyclclean_dnn_c5_merged_allcov.bam
echo $bam
python score.py $bam

bam=/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/predict_cyclomics_clean_bam/predict_cyclclean_dnn_c10_merged_allcov.bam
echo $bam
python score.py $bam

bam=/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/predict_cyclomics_clean_bam/predict_cyclclean_dnn_c15_merged_allcov.bam
echo $bam
python score.py $bam

bam=/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/predict_cyclomics_clean_bam/predict_cyclclean_dnn_c20_merged_allcov.bam
echo $bam
python score.py $bam

bam=/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/predict_cyclomics_clean_bam/predict_cyclclean_dnn_c100_merged_allcov.bam
echo $bam
python score.py $bam