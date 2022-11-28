#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=48:00:00
#SBATCH --mem=20G

## RUN ON CPU WITH CONDA NANOPORE_SNV

# model='/hpc/compgen/projects/gw_cfdna/snv_qs/lambda_analysis/files_for_model/cnn/model/model_c20noref_gpu_0709/model-06-1.00.h5'
name='dnn_trained_lambda_c20ref_test_newcyclomicsregion5'
# hdf5='data_matrices/matrix_200220cycl3d_c20_noref.hdf5'
ref='/hpc/compgen/GENOMES/CHM13_t2t/chm13.draft_v1.1.fa'
# ref='/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/chm13.draft_v1.1_altv2.fa'

echo $name.fastq

# python predict_qs.py $model $name.fastq $hdf5

mkdir /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/results/predict/data

minimap2 -ax map-ont $ref $name.fastq > $name.sam
samtools view -S -b $name.sam > $name.bam
samtools sort $name.bam -o /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/results/predict/data/$name.sorted.bam
samtools index /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/results/predict/data/$name.sorted.bam

rm $name.bam $name.sam 

python score.py /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/results/predict/data/$name.sorted.bam

mkdir perbase
perbase base-depth -r $ref /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/results/predict/data/$name.sorted.bam > perbase/$name.csv

mkdir /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/results/predict/plotserrorrate
python ploterrorrate.py $name $name.fastq
