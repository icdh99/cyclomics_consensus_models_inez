# sbatch -o R-%x.%j.out -J dnn_5 predict.sh dnn 5
# sbatch -o R-%x.%j.out -J dnn_10 predict.sh dnn 10
# sbatch -o R-%x.%j.out -J dnn_15 predict.sh dnn 15
# sbatch -o R-%x.%j.out -J dnn_20 predict.sh dnn 20
# sbatch -o R-%x.%j.out -J dnn_100 predict.sh dnn 100

sbatch --parsable --dependency=afterany:15925065 -o R-%x.%j.out -J cnn_5 predict.sh cnn 5
sbatch --parsable --dependency=afterany:15925066 -o R-%x.%j.out -J cnn_10 predict.sh cnn 10
sbatch --parsable --dependency=afterany:15925067 -o R-%x.%j.out -J cnn_20 predict.sh cnn 15
sbatch --parsable --dependency=afterany:15925069 -o R-%x.%j.out -J cnn_15 predict.sh cnn 20
sbatch --parsable --dependency=afterany:15925072 -o R-%x.%j.out -J cnn_100 predict.sh cnn 100


