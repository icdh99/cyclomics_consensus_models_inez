#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=60:00:00
#SBATCH --mem=50G

# wget -q https://s3-us-west-2.amazonaws.com/human-pangenomics/T2T/CHM13/nanopore/rel8-guppy-5.0.7/reads.fastq.gz

wget -q https://s3-us-west-2.amazonaws.com/human-pangenomics/T2T/CHM13/nanopore/rel8-guppy-5.0.7/sequencing_summary.txt.gz 