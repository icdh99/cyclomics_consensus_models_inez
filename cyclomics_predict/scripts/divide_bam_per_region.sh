#!/bin/bash

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=icdenhond@gmail.com
#SBATCH --time=48:00:00
#SBATCH --mem=40G

# {0..40}

#look at folders!!!!
for i in {11..182}
do
    nr=$i
    echo $nr
    bam_consensus=/hpc/compgen/projects/gw_cfdna/snv_qs/raw/Minimap2Align/SamtoolsMergeBams/FAU48563.merged.bam
    bam=(/hpc/compgen/projects/gw_cfdna/snv_qs/raw/CycasConsensus/MapqAndNMFilter/FAU48563_pass_f5d283ba_"$nr"_filtered_split.NM_50_mapq_20.bam)
    # bam=(/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/bamfiles_altv2/FAU48563_altv2_"$nr".sorted.bam)

    echo $bam_consensus
    echo $bam

    echo 'all reads: ' $(samtools view $bam | awk '{print $1}' | wc -l)
    
    echo 'region 1: ' $(samtools view $bam chr17:7574728-7574828 | awk '{print $1}' | wc -l)
    # samtools view $bam_consensus chr17:7574728-7574828 | awk '{print $1}' | sort | uniq | wc -l
    echo 'region 2: ' $(samtools view $bam chr17:7577659-7577784 | awk '{print $1}' | sort | uniq | wc -l)
    # samtools view $bam_consensus chr17:7577659-7577784 | awk '{print $1}' | sort | uniq | wc -l
    echo 'region 3: ' $(samtools view $bam chr17:7577816-7577956 | awk '{print $1}' | sort | uniq | wc -l)
    # samtools view $bam_consensus chr17:7577816-7577956 | awk '{print $1}' | sort | uniq | wc -l
    echo 'region 4: ' $(samtools view $bam chr17:7578283-7578443 | awk '{print $1}' | sort | uniq | wc -l)
    # samtools view $bam_consensus chr17:7578283-7578443 | awk '{print $1}' | sort | uniq | wc -l
    echo 'region 5: ' $(samtools view $bam chr17:7579214-7579351 | awk '{print $1}' | sort | uniq | wc -l)
    # samtools view $bam_consensus chr17:7579214-7579351 | awk '{print $1}' | sort | uniq | wc -l

    samtools view -bh $bam chr17:7574728-7574828 | samtools sort -o ../data/data_normal/bam_region1/bam_region1_$nr.bam
    samtools index ../data/data_normal/bam_region1/bam_region1_$nr.bam
    samtools view -bh $bam_consensus chr17:7574728-7574828 | samtools sort -o ../data/data_normal/bam_region1/bam_region1_consensus.bam
    samtools index ../data/data_normal/bam_region1/bam_region1_consensus.bam
    samtools view -bh $bam chr17:7577659-7577784 | samtools sort -o ../data/data_normal/bam_region2/bam_region2_$nr.bam
    samtools index ../data/data_normal/bam_region2/bam_region2_$nr.bam
    samtools view -bh $bam_consensus chr17:7577659-7577784 | samtools sort -o ../data/data_normal/bam_region2/bam_region2_consensus.bam
    samtools index ../data/data_normal/bam_region2/bam_region2_consensus.bam
    samtools view -bh $bam chr17:7577816-7577956 | samtools sort -o ../data/data_normal/bam_region3/bam_region3_$nr.bam
    samtools index ../data/data_normal/bam_region3/bam_region3_$nr.bam
    samtools view -bh $bam_consensus chr17:7577816-7577956 | samtools sort -o ../data/data_normal/bam_region3/bam_region3_consensus.bam
    samtools index ../data/data_normal/bam_region3/bam_region3_consensus.bam
    samtools view -bh $bam chr17:7578283-7578443 | samtools sort -o ../data/data_normal/bam_region4/bam_region4_$nr.bam
    samtools index ../data/data_normal/bam_region4/bam_region4_$nr.bam
    samtools view -bh $bam_consensus chr17:7578283-7578443 | samtools sort -o ../data/data_normal/bam_region4/bam_region4_consensus.bam
    samtools index ../data/data_normal/bam_region4/bam_region4_consensus.bam
    samtools view -bh $bam chr17:7579214-7579351 | samtools sort -o ../data/data_normal/bam_region5/bam_region5_$nr.bam
    samtools index ../data/data_normal/bam_region5/bam_region5_$nr.bam
    samtools view -bh $bam_consensus chr17:7579214-7579351 | samtools sort -o ../data/data_normal/bam_region5/bam_region5_consensus.bam
    samtools index ../data/data_normal/bam_region5/bam_region5_consensus.bam
done
# samtools view $bam chr17:7574728-7574828 | awk '{print $1}' | sort | uniq > ../data/data/bam_region1/readid_region1_$nr.txt
# samtools view $bam_consensus chr17:7574728-7574828 | awk '{print $1}' | sort | uniq > ../data/data/bam_region1/readid_region1_consensus.txt
# samtools view $bam chr17:7577659-7577784 | awk '{print $1}' | sort | uniq > ../data/data/bam_region2/readid_region2_$nr.txt
# samtools view $bam_consensus chr17:7577659-7577784 | awk '{print $1}' | sort | uniq > ../data/data/bam_region2/readid_region2_consensus.txt
# samtools view $bam chr17:7577816-7577956 | awk '{print $1}' | sort | uniq > ../data/data/bam_region3/readid_region3_$nr.txt
# samtools view $bam_consensus chr17:7577816-7577956 | awk '{print $1}' | sort | uniq > ../data/data/bam_region3/readid_region3_consensus.txt
# samtools view $bam chr17:7578283-7578443 | awk '{print $1}' | sort | uniq > ../data/data/bam_region4/readid_region4_$nr.txt
# samtools view $bam_consensus chr17:7578283-7578443 | awk '{print $1}' | sort | uniq > ../data/data/bam_region4/readid_region4_consensus.txt
# samtools view $bam chr17:7579214-7579351 | awk '{print $1}' | sort | uniq > ../data/data/bam_region5/readid_region5_$nr.txt
# samtools view $bam_consensus chr17:7579214-7579351 | awk '{print $1}' | sort | uniq > ../data/data/bam_region5/readid_region5_consensus.txt