bam_consensus=/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/bam_region1/bam_region1_consensus.bam
bam0=/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/bam_region1/bam_region1_0.bam

counter=0
while IFS= read -r line; do
    # echo $line
    # readid=$(echo $line | cut -d"_" -f 1)
    # echo $readid
    n=$(samtools view $bam_consensus | grep $line | wc -l)
    if [ $n -gt 0 ]
    then
        # samtools view $bam_consensus | grep $line | wc -l
        # samtools view $bam0 | grep $line | wc -l
        let counter++
    fi
done < /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/bam_region1/readid_region1_0.txt
echo $counter

bam_consensus=/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/bam_region2/bam_region2_consensus.bam
bam0=/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/bam_region1/bam_region2_0.bam
counter=0
while IFS= read -r line; do
    # echo $line
    # readid=$(echo $line | cut -d"_" -f 1)
    # echo $readid
    n=$(samtools view $bam_consensus | grep $line | wc -l)
    if [ $n -gt 0 ]
    then
        # samtools view $bam_consensus | grep $line | wc -l
        # samtools view $bam0 | grep $line | wc -l
        let counter++
    fi
done < /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/bam_region2/readid_region2_0.txt
echo $counter

bam_consensus=/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/bam_region3/bam_region3_consensus.bam
bam0=/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/bam_region1/bam_region3_0.bam
counter=0
while IFS= read -r line; do
    # echo $line
    # readid=$(echo $line | cut -d"_" -f 1)
    # echo $readid
    n=$(samtools view $bam_consensus | grep $line | wc -l)
    if [ $n -gt 0 ]
    then
        # samtools view $bam_consensus | grep $line | wc -l
        # samtools view $bam0 | grep $line | wc -l
        let counter++
    fi
done < /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/bam_region3/readid_region3_0.txt
echo $counter

bam_consensus=/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/bam_region4/bam_region4_consensus.bam
bam0=/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/bam_region1/bam_region4_0.bam
counter=0
while IFS= read -r line; do
    # echo $line
    # readid=$(echo $line | cut -d"_" -f 1)
    # echo $readid
    n=$(samtools view $bam_consensus | grep $line | wc -l)
    if [ $n -gt 0 ]
    then
        # samtools view $bam_consensus | grep $line | wc -l
        # samtools view $bam0 | grep $line | wc -l
        let counter++
    fi
done < /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/bam_region4/readid_region4_0.txt
echo $counter

bam_consensus=/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/bam_region5/bam_region5_consensus.bam
bam0=/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/bam_region1/bam_region5_0.bam
counter=0
while IFS= read -r line; do
    # echo $line
    # readid=$(echo $line | cut -d"_" -f 1)
    # echo $readid
    n=$(samtools view $bam_consensus | grep $line | wc -l)
    if [ $n -gt 0 ]
    then
        # samtools view $bam_consensus | grep $line | wc -l
        # samtools view $bam0 | grep $line | wc -l
        let counter++
    fi
done < /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/bam_region5/readid_region5_0.txt
echo $counter