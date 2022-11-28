#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=48:00:00
#SBATCH --mem=20G
#SBATCH --cpus-per-task=8

# ref=/hpc/compgen/GENOMES/CHM13_t2t/chm13.draft_v1.1.fa
# ref=/hpc/compgen/GENOMES/CHM13_t2t/chm13.draft_v1.1.fa
ref=/hpc/compgen/GENOMES/CHM13_t2t_v2/chm13v2.0.fa

for cov in 5 10 15 20 100
do
    for i in 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 20+
    do
    ls /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/predict_cyclomics_clean_fastq/predict_cyclclean_dnn_c"$cov"_region*_"$i"X.fastq
    fastq_merged=/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/predict_cyclomics_clean_fastq/predict_cyclclean_dnn_c"$cov"_merged_"$i"X.fastq
    
    name=/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/predict_cyclomics_clean_bam/predict_cyclclean_dnn_c"$cov"_merged_"$i"X
    
    # cat /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/predict_cyclomics_clean_fastq/predict_cyclclean_dnn_c"$cov"_region*_"$i"X.fastq > $fastq_merged
    minimap2 -ax map-ont -t 8 $ref $fastq_merged > $name.sam
    samtools view -S -b $name.sam > $name.bam
    samtools sort $name.bam -o $name.sorted.bam
    samtools index $name.sorted.bam
    rm $name.bam $name.sam 
    echo 'Merged fastq file: ' $fastq_merged
    
    echo 'Resulting bam file: ' $name.sorted.bam
    

    python score.py $name.sorted.bam

    echo $'\n'
    done
done

# fastq="/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_wgs_fastq/predict_gwcycl_dnn_c"$model_coverage"_"$chromosome".fastq"
# name="/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_wgs_bam_output/predict_gwcycl_dnn_c"$model_coverage"_"$chromosome""
# outdir='/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_wgs_bam_output/'
# ref='/hpc/cog_bioinf/GENOMES.old/hs37d5/hs37d5.fasta'

# echo $fastq
# echo $name
# echo $ref

# source activate nanopore-snv
# # minimap2 -ax map-ont -t 8 $ref $fastq > $name.sam
# # samtools view -S -b $name.sam > $name.bam
# # samtools sort $name.bam -o $name.sorted.bam
# # samtools index $name.sorted.bam

# # rm $name.bam $name.sam 

# python score.py $name.sorted.bam

# echo $name.sorted.bam
