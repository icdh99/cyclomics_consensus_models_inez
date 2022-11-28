#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=60:00:00
#SBATCH --mem=20G

# for i in {0..44}
# do

# bam_file=(/hpc/compgen/projects/gw_cfdna/gw_cyclomics/analysis/lchen/cycloseq-output/HC02_CYC36-20ng/CycasConsensus/MapqAndNMFilter/FAS66395_pass_d9201700_"$i"_filtered_split.NM_50_mapq_20.bam)
# echo "Bam file: " $bam_file

# samtools view -c $bam_file

# samtools idxstats $bam_file

# samtools coverage -m $bam_file

# done

# samtools merge -o GW_cycl_chrom_merged.bam -L hg38.bed /hpc/compgen/projects/gw_cfdna/gw_cyclomics/analysis/lchen/cycloseq-output/HC02_CYC36-20ng/CycasConsensus/MapqAndNMFilter/FAS66395_pass_d9201700_*_filtered_split.NM_50_mapq_20.bam

# for i in {1..22}
# do
# samtools view -bh GW_cycl_chrom_merged.bam $i > GW_cycl_chrom_merged_$i.bam
# samtools index GW_cycl_chrom_merged_$i.bam
# done

# samtools view -bh GW_cycl_chrom_merged.bam X > GW_cycl_chrom_merged_X.bam
# samtools index GW_cycl_chrom_merged_X.bam

# samtools view -bh GW_cycl_chrom_merged.bam Y > GW_cycl_chrom_merged_Y.bam
# samtools index GW_cycl_chrom_merged_Y.bam

# mkdir new
# cd new
# csplit -s -z /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/cyclomics_wgs/hs37d5.fasta '/>/' '{*}'
# for i in xx* ; do \
#   n=$(sed 's/>// ; s/ .*// ; 1q' "$i") ; \
#   mv "$i" "chr$n.fa" ; \
#  done

python make_vcf_from_ref.py