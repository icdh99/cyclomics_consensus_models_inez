bam=/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_bam_perregion/consensus/cyclomics_muts_consensus_region1.bam
samtools view -c $bam
samtools view $bam | awk '{print $12'} | head -100

