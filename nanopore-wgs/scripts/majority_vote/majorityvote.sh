#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=30:00:00
#SBATCH --mem=20G

# dnn/cnn maakt niet uit
# submitten: array=0-39 voor crossval majority vote

date=$(date +%F_%R)
echo $date 

coverage_bin=$1

bam=(/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/rel8/reads_withheader_chr18.sorted.bam)
vcf=(/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/ref_per_chromosome/chr18_subset/chr18_subset_$SLURM_ARRAY_TASK_ID.vcf)
# vcf=(/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/ref_per_chromosome/chr18_subset/chr18_subset_0.vcf)
out_file=(/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/majority_vote/results_majorityvote_chr18_subset_c$1_$SLURM_ARRAY_TASK_ID.txt)

echo 'Bam file: ' $bam
echo 'Vcf file: ' $vcf
echo 'Coverage bin: ' $1
echo 'Out file: ' $out_file

python majorityvote.py $bam $vcf $coverage_bin $out_file


