#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=200:00:00
#SBATCH --mem=30G

chrnr=$1

# for chrnr in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 X Y
# do

bam_file=(/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_wgs_bam_input/GW_cycl_chrom_merged_"$chrnr".bam)
hdf5_prefix=(/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_wgs_hdf5_maskedrefbase/predict_dnn_chr"$chrnr".hdf5)
ref_file=(/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_wgs_ref/chr"$chrnr".fa)
name=$(echo $bam_file | cut -d'/' -f 10)
samtools view $bam_file | awk '{print $1}' | sort | uniq > $name.txt

echo $name
 
echo 'Bam file: ' $bam_file
echo 'Read id file: ' $name.txt
echo 'Hdf5 file: ' $hdf5_prefix
echo 'Ref file: ' $ref_file
echo 'nr unique readids in '$name ':' $(samtools view $bam_file | awk '{print $1}' | sort | uniq | wc -l)
echo 'Chromosome: ' chr$chrnr

rm $hdf5_prefix
mkdir tmp_bamfiles_"$chrnr"

python predict_dnn.py $bam_file $name.txt tmp_bamfiles_"$chrnr" $hdf5_prefix $ref_file chr$chrnr

rm -r tmp_bamfiles_"$chrnr"

# done




