#!/bin/sh

jid_1=$(sbatch --parsable --job-name="chr3predict" sbatch predict.sh chr3)
jid_2=$(sbatch --parsable --dependency=afterok:${jid_1} --job-name="chr4 predict" sbatch predict.sh chr4)
jid_3=$(sbatch --parsable --dependency=afterok:${jid_2} --job-name="chr5 predict" sbatch predict.sh chr5)
jid_4=$(sbatch --parsable --dependency=afterok:${jid_3} --job-name="chr6 predict" sbatch predict.sh chr6)
jid_5=$(sbatch --parsable --dependency=afterok:${jid_4} --job-name="chr7 predict" sbatch predict.sh chr7)
jid_6=$(sbatch --parsable --dependency=afterok:${jid_5} --job-name="chr8 predict" sbatch predict.sh chr8)

