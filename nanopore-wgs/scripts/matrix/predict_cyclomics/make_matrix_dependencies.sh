# script to submit multiple dependencies for make matrix for cyclomics predict

jid_region1=$(sbatch --parsable  make_matrix.sh region1)
jid_region2=$(sbatch --parsable --dependency=afterok:${jid_region1} make_matrix.sh region2)
jid_region3=$(sbatch --parsable --dependency=afterok:${jid_region2} make_matrix.sh region3)
jid_region4=$(sbatch --parsable --dependency=afterok:${jid_region3} make_matrix.sh region4)
jid_region5=$(sbatch --parsable --dependency=afterok:${jid_region4} make_matrix.sh region5)
