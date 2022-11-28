# sbatch -o R-%x.%j.out -J dnn_r1_mut make_matrix.sh region1 dnn
# sbatch -o R-%x.%j.out -J cnn_r1_mut make_matrix.sh region1 cnn

sbatch -o R-%x.%j.out -J dnn_r2_mut_151_196 make_matrix.sh region2 dnn
sbatch -o R-%x.%j.out -J cnn_r2_mut_151_196 make_matrix.sh region2 cnn
sbatch -o R-%x.%j.out -J dnn_r4_mut_151_196 make_matrix.sh region4 dnn
sbatch -o R-%x.%j.out -J cnn_r4_mut_151_196 make_matrix.sh region4 cnn



# sbatch -o R-%x.%j.out -J dnn_r3_mut make_matrix.sh region3 dnn
# sbatch -o R-%x.%j.out -J cnn_r3_mut make_matrix.sh region3 cnn



# sbatch -o R-%x.%j.out -J dnn_r5_mut make_matrix.sh region5 dnn
# sbatch -o R-%x.%j.out -J cnn_r5_mut make_matrix.sh regions5 cnn