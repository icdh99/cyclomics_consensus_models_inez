#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=12:00:00
#SBATCH --mem=10G

# original_file=/hpc/compgen/projects/gw_cfdna/snv_qs/raw/CycasConsensus/FilterShortReads/FAU48563_pass_f5d283ba_0_filtered.fastq

# folder=/hpc/compgen/projects/gw_cfdna/snv_qs/raw/CycasConsensus/FilterShortReads/
# name=FAU48563_pass_f5d283ba_0_filtered

# minimap2 -ax map-ont /hpc/compgen/GENOMES/CHM13_t2t/chm13.draft_v1.1.fa out.fastq > orig.sam
# ls orig.sam
# samtools view -S -b orig.sam > orig.bam
# samtools sort orig.bam -o orig.sorted.bam
# samtools index orig.sorted.bam
# rm orig.bam orig.sam 

for i in {0..10}
do
    path_out=/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/bamfiles_altv2
    name=FAU48563_altv2_$i
    echo /hpc/compgen/projects/gw_cfdna/snv_qs/raw/CycasConsensus/FilterShortReads/FAU48563_pass_f5d283ba_"$i"_filtered.fastq
    minimap2 -ax map-ont /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/chm13.draft_v1.1_altv2.fa /hpc/compgen/projects/gw_cfdna/snv_qs/raw/CycasConsensus/FilterShortReads/FAU48563_pass_f5d283ba_"$i"_filtered.fastq > $path_out/$name.sam
    samtools view -S -c $path_out/$name.sam
    samtools view -S -c -q 20 $path_out/$name.sam
    samtools view -S -b -q 20 $path_out/$name.sam > $path_out/$name.bam
    samtools sort $path_out/$name.bam -o $path_out/$name.sorted.bam
    samtools index $path_out/$name.sorted.bam
    rm $path_out/$name.bam $path_out/$name.sam 

    samtools idxstats $path_out/$name.sorted.bam

done