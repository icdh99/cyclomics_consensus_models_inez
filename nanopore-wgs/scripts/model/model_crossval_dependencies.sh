# jid_1=$(sbatch --parsable model.sh dnn 10)
# jid_2=$(sbatch --parsable --dependency=afterok:${jid_1} model.sh dnn 15)
# jid_3=$(sbatch --parsable --dependency=afterok:${jid_2} model.sh dnn 20)
# jid_4=$(sbatch --parsable --dependency=afterok:${jid_3} model.sh dnn 100)
# jid_5=$(sbatch --parsable --dependency=afterok:${jid_4} model.sh cnn 15)
# jid_6=$(sbatch --parsable --dependency=afterok:${jid_5} model.sh cnn 20)

jid_1=$(sbatch --parsable model.sh cnn 5)
jid_2=$(sbatch --parsable --dependency=afterany:${jid_1} model.sh cnn 10)
jid_3=$(sbatch --parsable --dependency=afterany:${jid_2} model.sh cnn 15)
jid_4=$(sbatch --parsable --dependency=afterany:${jid_3} model.sh cnn 20)
jid_5=$(sbatch --parsable --dependency=afterany:${jid_4} model.sh cnn 100)



# to do:
# edit scripts to include coverage all --> gedaan bij dnn script
# run DNN all --> staat hierbij nu 
# nog toevoegen aan CNN all en die apart runnen als de rest klaarrrrr is
