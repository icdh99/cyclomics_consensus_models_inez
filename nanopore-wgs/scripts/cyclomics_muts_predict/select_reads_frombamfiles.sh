
# samtools view --qname-file readid_unique_long.txt -o cyclomics_muts_consensus_chr17_YM3filter_subsetreads.sorted.bam /hpc/compgen/projects/gw_cfdna/snv_qs/raw/cyclomics_mutations_dataset_cleanconsensus/cyclomics_muts_consensus_chr17_YM3filter.sorted.bam 
# samtools index cyclomics_muts_consensus_chr17_YM3filter_subsetreads.sorted.bam

# samtools view -c cyclomics_muts_consensus_chr17_YM3filter_subsetreads.sorted.bam

# mkdir cycl_pred_subsetreadsperregion

# for file in /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/cyclomics_muts_predict/analyse_perread_new/bam_perregion_pred/*.bam
# do
#     echo $file
#     region=$(echo $file | cut -d '/' -f 12 | cut -d '_' -f 6 | cut -d '.' -f 1 )
#     bam_out_name=$(echo $file | cut -d '/' -f 12 | cut -d '.' -f 1)
#     echo $bam_out_name
#     echo $region
#     region_file=readid_unique_short_"$region".txt
#     echo cycl_pred_subsetreadsperregion/"$bam_out_name"_subsetreads.sorted.bam
#     samtools view --qname-file $region_file -o cycl_pred_subsetreadsperregion/"$bam_out_name"_subsetreads.sorted.bam $file
# done

# for file in cycl_pred_subsetreadsperregion/*.bam
# do  
#     samtools index $file
#     samtools view -c $file
# done



# this don't work because all predictions are forward. need dataframe info to get for/rev information aaargh
# mkdir pred_subsetreadsperregion_forward
# mkdir pred_subsetreadsperregion_reverse
# # make forward and reverse bam files
# for file in cycl_pred_subsetreadsperregion/*.bam
# do  
#     echo $file
#     bam_out_name=$(echo $file | cut -d '/' -f 2 | cut -d '.' -f 1)
#     echo $bam_out_name
#     # reverse
#     samtools view -f 16 -bh $file -o pred_subsetreadsperregion_reverse/"$bam_out_name"_reverse.sorted.bam 
#     samtools index pred_subsetreadsperregion_reverse/"$bam_out_name"_reverse.sorted.bam 
#     samtools view -c pred_subsetreadsperregion_reverse/"$bam_out_name"_reverse.sorted.bam 

#     # forward
#     samtools view -F 20 -bh $file -o pred_subsetreadsperregion_forward/"$bam_out_name"_forward.sorted.bam 
#     samtools index pred_subsetreadsperregion_forward/"$bam_out_name"_forward.sorted.bam 
#     samtools view -c pred_subsetreadsperregion_forward/"$bam_out_name"_forward.sorted.bam 
# done
