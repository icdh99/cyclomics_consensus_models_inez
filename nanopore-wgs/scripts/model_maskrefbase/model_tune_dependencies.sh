

jid_1=$(sbatch --parsable --job-name=tune_dnn_5 --output=%x.%j.out model_tune.sh dnn 5)
sbatch --dependency=afterany:${jid_1} --job-name=tune_cnn_5 --output=%x.%j.out model_tune.sh cnn 5

jid_2=$(sbatch --parsable --job-name=tune_dnn_10 --output=%x.%j.out model_tune.sh dnn 10)
sbatch --dependency=afterany:${jid_2} --job-name=tune_cnn_10 --output=%x.%j.out model_tune.sh cnn 10

jid_3=$(sbatch --parsable --job-name=tune_dnn_15 --output=%x.%j.out model_tune.sh dnn 15)
sbatch --dependency=afterany:${jid_3} --job-name=tune_cnn_15 --output=%x.%j.out model_tune.sh cnn 15

jid_4=$(sbatch --parsable --job-name=tune_dnn_20 --output=%x.%j.out model_tune.sh dnn 20)
sbatch --dependency=afterany:${jid_4} --job-name=tune_cnn_20 --output=%x.%j.out model_tune.sh cnn 20

jid_5=$(sbatch --parsable --job-name=tune_dnn_100 --output=%x.%j.out model_tune.sh dnn 100)
sbatch --dependency=afterany:${jid_5} --job-name=tune_cnn_100 --output=%x.%j.out model_tune.sh cnn 100



