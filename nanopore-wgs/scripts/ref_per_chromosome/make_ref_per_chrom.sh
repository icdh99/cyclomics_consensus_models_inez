#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=24:00:00
#SBATCH --mem=10G

python make_ref_per_chrom.py