
# for cov in 10 15 20 100
# do

#     fastq_merged=/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_fastq/predict_cycl_muts_dnn_c"$cov"_merged.fastq

#     ls /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_fastq/predict_cyclclean_dnn_c"$cov"_region*.fastq 

#     cat /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_fastq/predict_cyclclean_dnn_c"$cov"_region*.fastq  > $fastq_merged

#     wc -l $fastq_merged
#     echo ""
# done

# for file in /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_bam_output/*.bam
# do
#     echo $file
#     samtools idxstats $file
# done

sum=0
for file in /hpc/compgen/projects/gw_cfdna/snv_qs/raw/000025-sup-extended-data/MapqAndNMFilter/*.bam
do 
    echo $file
    number=$(samtools view -c "$file")
    sum=$((sum + number))
done
echo "The sum of the lines of the files is: $sum"