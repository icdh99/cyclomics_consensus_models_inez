NPROC=$(nproc)
BASECALLS=basecalls.fa

DRAFT=draft_assm/assm_final.fa

OUTDIR=medaka_consensus
mkdir $OUTDIR
medaka_consensus -i ${BASECALLS} -d ${DRAFT} -o ${OUTDIR} -t ${NPROC} -m r941_min_high_g303
