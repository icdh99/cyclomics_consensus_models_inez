# sbatch -o R-%x.%j.out -J 5_dnn_predict_muts predict.sh 5 dnn
# sbatch -o R-%x.%j.out -J 10_dnn_predict_muts predict.sh 10 dnn
# sbatch -o R-%x.%j.out -J 15_dnn_predict_muts predict.sh 15 dnn
# sbatch -o R-%x.%j.out -J 20_dnn_predict_muts predict.sh 20 dnn
# sbatch -o R-%x.%j.out -J 100_dnn_predict_muts predict.sh 100 dnn

# sbatch -o R-%x.%j.out -J 5_cnn_predict_muts predict.sh 5 cnn
# sbatch -o R-%x.%j.out -J 10_cnn_predict_muts predict.sh 10 cnn
# sbatch -o R-%x.%j.out -J 15_cnn_predict_muts predict.sh 15 cnn
# sbatch -o R-%x.%j.out -J 20_cnn_predict_muts predict.sh 20 cnn
# sbatch -o R-%x.%j.out -J 100_cnn_predict_muts predict.sh 100 cnn

sbatch -o R-%x.%j.out -J dnn_5_map_score map_score.sh dnn 5
sbatch -o R-%x.%j.out -J dnn_10_map_score map_score.sh dnn 10
sbatch -o R-%x.%j.out -J dnn_15_map_score map_score.sh dnn 15
sbatch -o R-%x.%j.out -J dnn_20_map_score map_score.sh dnn 20
sbatch -o R-%x.%j.out -J dnn_100_map_score map_score.sh dnn 100

sbatch -o R-%x.%j.out -J cnn_5_map_score map_score.sh cnn 5
sbatch -o R-%x.%j.out -J cnn_10_map_score map_score.sh cnn 10
sbatch -o R-%x.%j.out -J cnn_15_map_score map_score.sh cnn 15
sbatch -o R-%x.%j.out -J cnn_20_map_score map_score.sh cnn 20
sbatch -o R-%x.%j.out -J cnn_100_map_score map_score.sh cnn 100


