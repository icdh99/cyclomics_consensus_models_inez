jid_1=$(sbatch --parsable --job-name="predict" sbatch predict.sh chr20 15)
jid_2=$(sbatch --parsable --dependency=afterok:${jid_1} --job-name="map" sbatch map_score.sh chr20 15)


