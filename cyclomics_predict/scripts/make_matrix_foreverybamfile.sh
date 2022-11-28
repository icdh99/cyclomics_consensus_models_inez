#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=24:00:00
#SBATCH --mem=10G

# remove hdf5 file before running if you want to overwrite existing keys
# make a vcf file per region
# run script make_vcf_per_region.sh

region=region5

for i in {0..10}
do
# file_consensus=(/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/bam_$region/bam_"$region"_consensus.bam)
file_bam=(/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_normal/bam_$region/bam_"$region"_$i.bam)
# file_bam=(/hpc/compgen/projects/gw_cfdna/snv_qs/raw/CycasConsensus/MapqAndNMFilter/FAU48563_pass_f5d283ba_0_filtered_split.NM_50_mapq_20.bam)
vcf=(/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/vcf_normalref/vcf_$region.vcf)
# vcf=(/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/vcf/vcf_$region.vcf)
name=$(echo $file_bam | cut -d'/' -f 11)    #fastq______mapq_20.bam 10 alt, 11 normal
runid=$(echo $name | cut -d'_' -f 3 | cut -d'.' -f 1)    # 0, 1, 2, 3... 
echo 'consensus file: ' $file_consensus
echo 'bam file: ' $file_bam
echo 'name: ' $name
echo 'runid: ' $runid
echo 'vcf file: ' $vcf

mkdir tmpnormal_bamfiles_$runid
mkdir /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_normal/train_data_dnn
mkdir /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_normal/train_data_cnn
mkdir /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_normal/data_readids

echo 'nr unique readids in '$name ':' $(samtools view $file_bam | awk '{print $1}' | sort | uniq | wc -l)
mkdir /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_readids
samtools view $file_bam | awk '{print $1}' | sort | uniq > /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_normal/data_readids/$name.txt

hdf5_dnn=(/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_normal/train_data_dnn/traintest_bam_"$region"_0-10_ref_alt_predict.hdf5)
# rm $hdf5_dnn
hdf5_cnn=(/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_normal/train_data_cnn/traintest_bam_"$region"_0-10_ref_alt_predict.hdf5)
# rm $hdf5_cnn
python matrix_splitread_predict_dnn.py $vcf $file_bam /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_normal/data_readids/$name.txt $runid $hdf5_dnn 20 ref
python matrix_splitread_predict_cnn.py $vcf $file_bam /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_normal/data_readids/$name.txt $runid $hdf5_cnn 20 ref

rm -r tmpnormal_bamfiles_$runid
rm -r /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_normal/data_readids

done

# region=region5
# for i in {0..10}
# do
# # file_consensus=(/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/bam_$region/bam_"$region"_consensus.bam)
# # file_bam=(/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_normal/bam_$region/bam_"$region"_$i.bam)
# file_bam=(/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/bam_$region/bam_"$region"_$i.bam)
# # vcf=(/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/vcf_normalref/vcf_$region.vcf)
# vcf=(/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/vcf/vcf_$region.vcf)
# name=$(echo $file_bam | cut -d'/' -f 10)    #fastq______mapq_20.bam 10 alt, 11 normal
# runid=$(echo $name | cut -d'_' -f 3 | cut -d'.' -f 1)    # 0, 1, 2, 3... 
# echo 'consensus file: ' $file_consensus
# echo 'bam file: ' $file_bam
# echo 'name: ' $name
# echo 'runid: ' $runid
# echo 'vcf file: ' $vcf

# mkdir tmp_bamfiles_$runid
# # mkdir /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_normal/train_data_dnn
# # mkdir /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_normal/train_data_cnn

# echo 'nr unique readids in '$name ':' $(samtools view $file_bam | awk '{print $1}' | sort | uniq | wc -l)
# mkdir /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_readids
# samtools view $file_bam | awk '{print $1}' | sort | uniq > /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_readids/$name.txt

# hdf5_dnn=(/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/train_data_dnn/traintest_bam_"$region"_0-10_ref_alt_predict.hdf5)
# # rm $hdf5_dnn
# hdf5_cnn=(/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/train_data_cnn/traintest_bam_"$region"_0-10_ref_alt_predict.hdf5)
# # rm $hdf5_cnn
# python matrix_splitread_predict_dnn_insertions.py $vcf $file_bam /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_readids/$name.txt $runid $hdf5_dnn 20 noref
# python matrix_splitread_predict_cnn_insertions.py $vcf $file_bam /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_readids/$name.txt $runid $hdf5_cnn 20 noref

# rm -r tmp_bamfiles_$runid
# rm -r /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_readids

# done