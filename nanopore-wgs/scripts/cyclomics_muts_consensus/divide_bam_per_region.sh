#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=48:00:00
#SBATCH --mem=40G


#look at folders!!!!

# cyclomics data with mutations
bam=/hpc/compgen/projects/gw_cfdna/snv_qs/raw/000025-sup-extended-data/SamtoolsMergeBams/fastq.merged.bam
echo $bam

echo 'all reads: ' $(samtools view $bam chr17 | awk '{print $1}' | wc -l)

echo 'region 1: ' $(samtools view $bam chr17:7574728-7574828 | awk '{print $1}' | wc -l)
echo 'region 2: ' $(samtools view $bam chr17:7577651-7577788 | awk '{print $1}' | wc -l)
echo 'region 3: ' $(samtools view $bam chr17:7577813-7577958 | awk '{print $1}' | wc -l)
echo 'region 4: ' $(samtools view $bam chr17:7578281-7578443 | awk '{print $1}' | wc -l)
echo 'region 5: ' $(samtools view $bam chr17:7579211-7579352 | awk '{print $1}' | wc -l)

samtools view -bh $bam chr17:7574728-7574828 | samtools sort -o /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_bam_perregion/consensus/cyclomics_muts_consensus_region1.bam
samtools index /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_bam_perregion/consensus/cyclomics_muts_consensus_region1.bam

samtools view -bh $bam chr17:7577651-7577788 | samtools sort -o /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_bam_perregion/consensus/cyclomics_muts_consensus_region2.bam
samtools index /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_bam_perregion/consensus/cyclomics_muts_consensus_region2.bam

samtools view -bh $bam chr17:7577813-7577958 | samtools sort -o /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_bam_perregion/consensus/cyclomics_muts_consensus_region3.bam
samtools index /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_bam_perregion/consensus/cyclomics_muts_consensus_region3.bam

samtools view -bh $bam chr17:7578281-7578443 | samtools sort -o /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_bam_perregion/consensus/cyclomics_muts_consensus_region4.bam
samtools index /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_bam_perregion/consensus/cyclomics_muts_consensus_region4.bam

samtools view -bh $bam chr17:7579211-7579352 | samtools sort -o /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_bam_perregion/consensus/cyclomics_muts_consensus_region5.bam
samtools index /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_bam_perregion/consensus/cyclomics_muts_consensus_region5.bam

