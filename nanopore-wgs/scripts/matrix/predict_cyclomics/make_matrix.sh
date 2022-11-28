#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=60:00:00
#SBATCH --mem=20G

# region=region2
region=$1
model_type=$2

for i in {0..182}
do
bam_file=(/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_normal/bam_$region/bam_"$region"_$i.bam)
vcf_file=(/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/vcf_normalref/vcf_$region.vcf)

name=$(echo $bam_file | cut -d'/' -f 11)
runid=$(echo $name | cut -d'_' -f 3 | cut -d'.' -f 1)
samtools view $bam_file | awk '{print $1}' | sort | uniq > $name.txt

echo 'Bam file: ' $bam_file
echo 'Vcf file: ' $vcf_file
echo 'Runid: ' $runid
echo 'Read id file: ' $name.txt
echo 'nr unique readids in '$name ':' $(samtools view $bam_file | awk '{print $1}' | sort | uniq | wc -l)

echo 'HDF5 file: ' /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/predict_cyclomics_clean_maskedrefbase/predict_"$model_type"_ref_0-10_"$region"
echo 'Region: ' $region
echo 'Model type: ' $model_type

mkdir tmp_bamfiles_"$model_type"_"$region"_"$runid"

# python script  CHANGE REGION COORDINATES IN PILEUP IN PYTHON SCRIPT --> now region 1 - 5 for clean dataset
python predict_"$model_type".py $vcf_file $bam_file $name.txt $runid /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/predict_cyclomics_clean_maskedrefbase/predict_"$model_type"_ref_0-10_"$region" $region
# python predict_cnn.py $vcf_file $bam_file $name.txt $runid /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/predict_cyclomics_clean_maskedrefbase/predict_"$model_type"_ref_0-10_"$region"

rm -r tmp_bamfiles_"$model_type"_"$region"_"$runid"
rm $name.txt

done

