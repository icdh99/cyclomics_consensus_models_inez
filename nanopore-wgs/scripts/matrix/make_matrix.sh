#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=300:00:00
#SBATCH --mem=10G

# CHECK TIME AND MEMORY!!!

# TRAIN TEST

# submit this script with --array=0-11 to get all vcf files

# remove hdf5 file before running if you want to overwrite existing keys
echo "Type of network: $1"

bam=(/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/rel8/reads_withheader_chr18.sorted.bam)
vcf=(/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/ref_per_chromosome/chr18_subset/chr18_subset_$SLURM_ARRAY_TASK_ID.vcf)
hdf5=(/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/traintest/chr18_$1/traintest_chr18_$1_$SLURM_ARRAY_TASK_ID.hdf5)
hdf5=(/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/traintest/traintest_maskedrefbase/traintest_chr18_$1_$SLURM_ARRAY_TASK_ID.hdf5)
python_script="traintest/make_matrix_traintest_$1_maskrefbase.py"

# testing purposes
# bam=(/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/rel8/reads_withheader_chr18.sorted.bam)
# vcf=(/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/ref_per_chromosome/chr18_subset/chr18_subset_0.vcf)
# hdf5=(/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/traintest/traintest_maskedrefbase/traintest_chr18_dnn_0.hdf5)
# python_script="traintest/make_matrix_traintest_dnn_maskrefbase.py"

rm $hdf5

echo 'Bam file: ' $bam
echo 'Vcf file: ' $vcf
echo 'Hdf5 file: ' $hdf5
echo 'Python script: ' $python_script

python $python_script $vcf $bam $hdf5 ref

# du -sh $hdf5