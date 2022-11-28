#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=12:00:00
#SBATCH --mem=10G

python merge_hdf5.py