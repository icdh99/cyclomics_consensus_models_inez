region1=chr17:7574727-7574828
seq=$(samtools faidx /hpc/compgen/GENOMES/CHM13_t2t/chm13.draft_v1.1.fa $region1)
echo $seq
python make_vcf.py region1 $seq

region2=chr17:7577658-7577787
seq=$(samtools faidx /hpc/compgen/GENOMES/CHM13_t2t/chm13.draft_v1.1.fa $region2)
echo $seq
python make_vcf.py region2 $seq

region3=chr17:7577815-7577956
seq=$(samtools faidx /hpc/compgen/GENOMES/CHM13_t2t/chm13.draft_v1.1.fa $region3)
echo $seq
python make_vcf.py region3 $seq

region4=chr17:7578282-7578442
seq=$(samtools faidx /hpc/compgen/GENOMES/CHM13_t2t/chm13.draft_v1.1.fa $region4)
echo $seq
python make_vcf.py region4 $seq

region5=chr17:7579212-7579351
seq=$(samtools faidx /hpc/compgen/GENOMES/CHM13_t2t/chm13.draft_v1.1.fa $region5)
echo $seq
python make_vcf.py region5 $seq