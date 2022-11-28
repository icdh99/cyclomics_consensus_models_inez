sbatch -o R-%x.%j.out -J dnn_r3 make_matrix.sh region3 dnn
sbatch -o R-%x.%j.out -J cnn_r3 make_matrix.sh region3 cnn

sbatch -o R-%x.%j.out -J dnn_r4 make_matrix.sh region4 dnn
sbatch -o R-%x.%j.out -J cnn_r4 make_matrix.sh region4 cnn

sbatch -o R-%x.%j.out -J dnn_r5 make_matrix.sh region5 dnn
sbatch -o R-%x.%j.out -J cnn_r5 make_matrix.sh region5 cnn