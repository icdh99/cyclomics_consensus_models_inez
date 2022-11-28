# for model in dnn cnn
# do
#     for cov in 5 10 15 20 100
#     do 
#     sbatch plot.sh $model $cov
#     done
# done


# ref=/hpc/compgen/GENOMES/CHM13_t2t_v2/chm13v2.0.fa

for file in /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/cyclomics_muts_predict/cycl_pred_subsetreadsperregion/*.bam
do  
    echo -n "$(echo $file | cut -d '/' -f 11-12 )" ; echo -n " "; echo $(samtools view -c $file  )
    
    # echo $file
    # model=$(echo $file | cut -d '/' -f 11 | cut -d '_' -f 4  )
    # echo $model
    # cov=$(echo $file | cut -d '/' -f 11 | cut -d '_' -f 5  )
    # echo $cov
    # region=$(echo $file | cut -d '/' -f 11 | cut -d '_' -f 6  )
    # echo $region
    # # sbatch plot.sh $model $cov
    # perbase base-depth -r $ref --max-depth 200000 --bed-file $region.bed $file > perbase_subsetreads/predict_cycl_muts_"$model"_"$cov"_merged_"$region".csv
done

