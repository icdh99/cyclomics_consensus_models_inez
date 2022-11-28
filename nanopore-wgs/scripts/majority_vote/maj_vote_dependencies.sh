# jid_1=$(sbatch --parsable --array=0-59 majorityvote.sh 5)
# jid_2=$(sbatch --parsable --dependency=afterok:${jid_1} --array=0-59 majorityvote.sh 10)
# jid_3=$(sbatch --parsable --dependency=afterok:${jid_2} --array=0-59 majorityvote.sh 15)
# jid_4=$(sbatch --parsable --dependency=afterok:${jid_3} --array=0-59 majorityvote.sh 20)
# jid_5=$(sbatch --parsable --dependency=afterok:${jid_4} --array=0-59 majorityvote.sh 100)

# jid_6=$(sbatch --parsable --dependency=afterok:${jid_1} analyse_majorityvote_0-39.sh 5)
# jid_7=$(sbatch --parsable --dependency=afterok:${jid_2} analyse_majorityvote_0-39.sh 10)
# jid_8=$(sbatch --parsable --dependency=afterok:${jid_3} analyse_majorityvote_0-39.sh 15)
# jid_9=$(sbatch --parsable --dependency=afterok:${jid_4} analyse_majorityvote_0-39.sh 20)
# jid_10=$(sbatch --parsable --dependency=afterok:${jid_5} analyse_majorityvote_0-39.sh 100)

# jid_11=$(sbatch --parsable --dependency=afterok:${jid_1} analyse_majorityvote_40-59.sh 5)
# jid_12=$(sbatch --parsable --dependency=afterok:${jid_2} analyse_majorityvote_40-59.sh 10)
# jid_13=$(sbatch --parsable --dependency=afterok:${jid_3} analyse_majorityvote_40-59.sh 15)
# jid_14=$(sbatch --parsable --dependency=afterok:${jid_4} analyse_majorityvote_40-59.sh 20)
# jid_15=$(sbatch --parsable --dependency=afterok:${jid_5} analyse_majorityvote_40-59.sh 100)

# sbatch analyse_majorityvote_0-39.sh 5
sbatch analyse_majorityvote_0-39.sh 10
sbatch analyse_majorityvote_0-39.sh 15
sbatch analyse_majorityvote_0-39.sh 20
sbatch analyse_majorityvote_0-39.sh 100

sbatch analyse_majorityvote_40-59.sh 5
sbatch analyse_majorityvote_40-59.sh 10
sbatch analyse_majorityvote_40-59.sh 15
sbatch analyse_majorityvote_40-59.sh 20
sbatch analyse_majorityvote_40-59.sh 100
