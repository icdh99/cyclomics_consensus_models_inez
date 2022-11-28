f=$(fastahack -r chr17 /hpc/compgen/GENOMES/CHM13_t2t/chm13.draft_v1.1.fa)

echo $f |awk '{print length}'
echo $f | wc -c
echo $f |awk '{print length}'