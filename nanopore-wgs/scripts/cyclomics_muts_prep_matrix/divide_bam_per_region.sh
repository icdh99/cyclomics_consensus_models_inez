#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=48:00:00
#SBATCH --mem=40G


#look at folders!!!!
for nr in {0..196}
do
    echo $nr
    bam=(/hpc/compgen/projects/gw_cfdna/snv_qs/raw/000025-sup-extended-data/MapqAndNMFilter/fastq_runid_f5d283baa7cb2763b7dddc698cd2e8de0d038c39_"$nr"_0_filtered_split.NM_50_mapq_20.bam)
    echo $bam

    echo 'all reads: ' $(samtools view $bam chr17 | awk '{print $1}' | wc -l)

    echo 'region 1: ' $(samtools view $bam chr17:7574728-7574828 | awk '{print $1}' | wc -l)
    echo 'region 2: ' $(samtools view $bam chr17:7577651-7577788 | awk '{print $1}' | wc -l)
    echo 'region 3: ' $(samtools view $bam chr17:7577813-7577958 | awk '{print $1}' | wc -l)
    echo 'region 4: ' $(samtools view $bam chr17:7578281-7578443 | awk '{print $1}' | wc -l)
    echo 'region 5: ' $(samtools view $bam chr17:7579211-7579352 | awk '{print $1}' | wc -l)

    samtools view -bh $bam chr17:7574728-7574828 | samtools sort -o /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_bam_perregion/bam_region1/bam_region1_$nr.bam
    samtools index /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_bam_perregion/bam_region1/bam_region1_$nr.bam

    samtools view -bh $bam chr17:7577651-7577788 | samtools sort -o /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_bam_perregion/bam_region2/bam_region2_$nr.bam
    samtools index /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_bam_perregion/bam_region2/bam_region2_$nr.bam

    samtools view -bh $bam chr17:7577813-7577958 | samtools sort -o /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_bam_perregion/bam_region3/bam_region3_$nr.bam
    samtools index /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_bam_perregion/bam_region3/bam_region3_$nr.bam

    samtools view -bh $bam chr17:7578281-7578443 | samtools sort -o /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_bam_perregion/bam_region4/bam_region4_$nr.bam
    samtools index /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_bam_perregion/bam_region4/bam_region4_$nr.bam

    samtools view -bh $bam chr17:7579211-7579352 | samtools sort -o /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_bam_perregion/bam_region5/bam_region5_$nr.bam
    samtools index /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_bam_perregion/bam_region5/bam_region5_$nr.bam

done
