
jid_1=$(sbatch --parsable --job-name=test_dnn_5 --output=%x.%j.out model_test.sh dnn 5)
jid_2=$(sbatch --parsable --job-name=test_dnn_10 --output=%x.%j.out model_test.sh dnn 10)
jid_3=$(sbatch --parsable --job-name=test_dnn_15 --output=%x.%j.out model_test.sh dnn 15)
jid_4=$(sbatch --parsable --job-name=test_dnn_20 --output=%x.%j.out model_test.sh dnn 20)
jid_5=$(sbatch --parsable --job-name=test_dnn_100 --output=%x.%j.out model_test.sh dnn 100)

sbatch --parsable --job-name=test_cnn_5 --output=%x.%j.out --dependency=afterany:${jid_1} model_test.sh cnn 5
sbatch --parsable --job-name=test_cnn_10 --output=%x.%j.out --dependency=afterany:${jid_2} model_test.sh cnn 10
sbatch --parsable --job-name=test_cnn_15 --output=%x.%j.out --dependency=afterany:${jid_3} model_test.sh cnn 15
sbatch --parsable --job-name=test_cnn_20 --output=%x.%j.out --dependency=afterany:${jid_4} model_test.sh cnn 20
sbatch --parsable --job-name=test_cnn_100 --output=%x.%j.out --dependency=afterany:${jid_5} model_test.sh cnn 100

# sbatch --job-name=test_cnn_5 --output=%x.%j.out model_test.sh cnn 5
# sbatch --job-name=test_cnn_10 --output=%x.%j.out model_test.sh cnn 10
# sbatch --job-name=test_cnn_15 --output=%x.%j.out model_test.sh cnn 15
# sbatch --job-name=test_cnn_20 --output=%x.%j.out model_test.sh cnn 20
# sbatch --job-name=test_cnn_100 --output=%x.%j.out model_test.sh cnn 100