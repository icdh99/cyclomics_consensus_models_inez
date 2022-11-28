#!/bin/bash

##SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=30:00:00
#SBATCH --mem=20G

# merge .txt files

coverage_bin=$1

echo 'Coverage bin: ' $1

array=(files_testdata/results_majorityvote_chr18_subset_c"$1"_*.txt)
echo "Files to be merged: " ${array[@]}

file1=${array[0]}

head -1 $file1 > results_majorityvote_chr18_subset_testdata_merged_c"$1".txt

tail -n +2 -q files_testdata/results_majorityvote_chr18_subset_c"$1"_*.txt >> results_majorityvote_chr18_subset_testdata_merged_c"$1".txt

python analyse_majorityvote.py results_majorityvote_chr18_subset_testdata_merged_c"$1".txt

# rm results_majorityvote_chr18_subsets_c"$1"_*.txt