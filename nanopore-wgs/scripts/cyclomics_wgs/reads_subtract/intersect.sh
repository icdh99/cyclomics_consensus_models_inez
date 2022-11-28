# prediction
BAM=/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_wgs_bam_output_maskedrefbase/predict_gwcycl_dnn_c100.sorted.bam
SNVBED=/hpc/compgen/projects/gw_cfdna/gw_cyclomics/analysis/lchen/SNV_tumor_informed/vcf2bed/HC01_HC02_HC03.filter_snv.bed
INSBED=/hpc/compgen/projects/gw_cfdna/gw_cyclomics/analysis/lchen/SNV_tumor_informed/vcf2bed/HC01_HC02_HC03.filter_ins.bed
DELBED=/hpc/compgen/projects/gw_cfdna/gw_cyclomics/analysis/lchen/SNV_tumor_informed/vcf2bed/HC01_HC02_HC03.filter_del.bed
BAMEXCLUDE=/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_wgs_bam_output_maskedrefbase_intersect/predict_gwcycl_dnn_c100_intersect.sorted.bam

# consensus 
# BAM=/hpc/compgen/projects/gw_cfdna/gw_cyclomics/analysis/lchen/cycloseq-output/HC02_CYC36-20ng/bams/HC02_CYC36-20ng.tagged.bam
# SNVBED=/hpc/compgen/projects/gw_cfdna/gw_cyclomics/analysis/lchen/SNV_tumor_informed/vcf2bed/HC01_HC02_HC03.filter_snv.bed
# INSBED=/hpc/compgen/projects/gw_cfdna/gw_cyclomics/analysis/lchen/SNV_tumor_informed/vcf2bed/HC01_HC02_HC03.filter_ins.bed
# DELBED=/hpc/compgen/projects/gw_cfdna/gw_cyclomics/analysis/lchen/SNV_tumor_informed/vcf2bed/HC01_HC02_HC03.filter_del.bed
# BAMEXCLUDE=/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_wgs_cons_intersect/cons_gwcycl_intersect.sorted.bam

# nr of reads before intersect
echo 'Number of reads before intersect: '
samtools view -c $BAM

# do intersect
bedtools intersect -wa -v -a $BAM -b $SNVBED $INSBED $DELBED > $BAMEXCLUDE

# index
samtools index $BAMEXCLUDE

# nr of reads after intersect
echo 'Number of reads after intersect: '
samtools view -c $BAMEXCLUDE

# options of intersect
# -wa = write original entry in A for each overlap
# -v = only report those entries in A that have no overlap in B