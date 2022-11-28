
jid_1=$(sbatch --parsable model_trainfinalmodel.sh dnn 10)
jid_2=$(sbatch --parsable --dependency=afterok:${jid_1} model_trainfinalmodel.sh dnn 15)
jid_3=$(sbatch --parsable --dependency=afterok:${jid_2} model_trainfinalmodel.sh dnn 20)
jid_1=$(sbatch --parsable model_trainfinalmodel.sh dnn 100)

jid_2=$(sbatch --parsable --dependency=afterany:${jid_1} model_trainfinalmodel.sh cnn 5)
jid_3=$(sbatch --parsable --dependency=afterany:${jid_2} model_trainfinalmodel.sh cnn 10)
jid_4=$(sbatch --parsable --dependency=afterany:${jid_3} model_trainfinalmodel.sh cnn 15)
jid_5=$(sbatch --parsable --dependency=afterany:${jid_4} model_trainfinalmodel.sh cnn 20)
jid_6=$(sbatch --parsable --dependency=afterany:${jid_5} model_trainfinalmodel.sh cnn 100)