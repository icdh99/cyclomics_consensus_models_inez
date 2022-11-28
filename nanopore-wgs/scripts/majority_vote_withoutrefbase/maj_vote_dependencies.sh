# jid_1=$(sbatch --parsable --array=10-59 majorityvote.sh 5)
# jid_2=$(sbatch --parsable --dependency=afterany:${jid_1} --array=10-59 majorityvote.sh 10)
# jid_3=$(sbatch --parsable --dependency=afterany:${jid_2} --array=10-59 majorityvote.sh 15)
# jid_4=$(sbatch --parsable --dependency=afterany:${jid_3} --array=10-59 majorityvote.sh 20)
# jid_5=$(sbatch --parsable --dependency=afterany:${jid_4} --array=10-59 majorityvote.sh 100)

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

sbatch -o R-_fpr_%x.%j.out -J mv_train_5 analyse_majorityvote_10-39.sh 5
sbatch -o R-_fpr_%x.%j.out -J mv_train_10 analyse_majorityvote_10-39.sh 10
sbatch -o R-_fpr_%x.%j.out -J mv_train_15 analyse_majorityvote_10-39.sh 15
sbatch -o R-_fpr_%x.%j.out -J mv_train_20 analyse_majorityvote_10-39.sh 20
sbatch -o R-_fpr_%x.%j.out -J mv_train_100 analyse_majorityvote_10-39.sh 100

sbatch -o R-_fpr_%x.%j.out -J mv_test_5 analyse_majorityvote_40-59.sh 5
sbatch -o R-_fpr_%x.%j.out -J mv_test_10 analyse_majorityvote_40-59.sh 10
sbatch -o R-_fpr_%x.%j.out -J mv_test_15 analyse_majorityvote_40-59.sh 15
sbatch -o R-_fpr_%x.%j.out -J mv_test_20 analyse_majorityvote_40-59.sh 20
sbatch -o R-_fpr_%x.%j.out -J mv_test_100 analyse_majorityvote_40-59.sh 100

