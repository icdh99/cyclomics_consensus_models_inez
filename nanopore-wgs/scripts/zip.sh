#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=24:00:00
#SBATCH --mem=20G

gzip -9 /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/tar_files/FAB49164-4045668814_Multi.tar

gzip -9 /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/tar_files/FAF05869-87644245_Multi.tar