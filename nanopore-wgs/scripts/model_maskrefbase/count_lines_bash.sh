#!/bin/bash

sum=0

for file in /hpc/compgen/projects/gw_cfdna/gw_cyclomics/analysis/lchen/cycloseq-output/HC02_CYC36-20ng/CycasConsensus/MapqAndNMFilter/*.bam
do
        echo $file
        number=$(wc -l < "$file")
        echo $number
        sum=$((sum + number))
done
echo "The sum of the $count file(s) is: $sum"