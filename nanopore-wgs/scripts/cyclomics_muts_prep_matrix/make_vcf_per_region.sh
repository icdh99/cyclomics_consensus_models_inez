ref=chm13v2.0.fa

# region1=chr17:7574728-7574828
# seq=$(samtools faidx $ref $region1)
# echo $seq
# python make_vcf.py region1 $seq

region2=chr17:7577651-7577788
seq=$(samtools faidx $ref $region2)
echo $seq
python make_vcf.py region2 $seq

# region3=chr17:7577813-7577958
# seq=$(samtools faidx $ref $region3)
# echo $seq
# python make_vcf.py region3 $seq

region4=chr17:7578281-7578443
seq=$(samtools faidx $ref $region4)
echo $seq
python make_vcf.py region4 $seq

# region5=chr17:7579211-7579352
# seq=$(samtools faidx $ref $region5)
# echo $seq
# python make_vcf.py region5 $seq