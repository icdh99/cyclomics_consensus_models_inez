# Consensus Calling and Validation of Single Nucleotide Variant Calling from Nanopore Sequencing with Deep Learning for CyclomicsSeq

This repository contains the code for my internship project performed at the UMC Utrecht. 

## Model training
The final models can be found in the folders nanopore-wgs/scripts/model_maskrefbase/model_cnn_c5_finalmodel with cnn being either cnn or dnn and c5 indicating the coverage bin of the model (c5 = 3-5X, c10 = 6-10X, c15 = 11-15X, c20 = 16-20X, c100 = 3-20X).

The files nanopore-wgs/scripts/model_maskrefbase/model_cnn_trainfinalmodel.py and nanopore-wgs/scripts/model_maskrefbase/model_cnn_trainfinalmodel.py are the scripts to train the final DNN and CNN models.

Scripts for cross-validation, tuning and testing of the DNN and CNN model can be found in the same folder. 

### Majority vote for benchmarking of model performance
The scripts to calculate the majority vote performance can be found in the folder nanopore-wgs/scripts/majority_vote_withoutrefbase

## Consensus calling for CyclomicsSeq dataset A ('clean' dataset)
Raw data: raw/CYC000025-extended-data

Create samples: nanopore-wgs/scripts/matrix/predict_cyclomics/make_matrix.sh

For each CyclomicsSeq dataset, the samples are created using the bam files in the CycasConsensus/MapQandNMFilter folder.

Predict: nanopore-wgs/scripts/cyclomics_clean_predict_maskedrefbase/predict.sh

Map: nanopore-wgs/scripts/cyclomics_clean_predict_maskedrefbase/map_score.sh

Cycas Consensus files: raw/CYC000025-extended-data/Minimap2Align/SamtoolsMergeBams/FAU48563.merged.bam

## Consensus calling for CyclomicsSeq dataset B (mutation dataset)
Raw data: raw/000025-sup-extended-data

Create samples: nanopore-wgs/scripts/cyclomics_muts_prep_matrix/make_matrix.sh

Predict: nanopore-wgs/scripts/cyclomics_muts_predict/predict.sh

Map: nanopore-wgs/scripts/cyclomics_muts_predict/map_score.sh

Cycas Consensus files: raw/cyclomics_mutations_dataset_cleanconsensus/cyclomics_muts_consensus_chr17_YM3filter.sorted.bam

## Consensus calling for CyclomicsSeq dataset C (genome-wide dataset)
Raw data: /hpc/compgen/projects/gw_cfdna/gw_cyclomics/analysis/lchen/cycloseq-output/HC02_CYC36-20ng/CycasConsensus/MapqAndNMFilter

Create samples: nanopore-wgs/scripts/cyclomics_wgs/make_matrix.sh

Predict: nanopore-wgs/scripts/cyclomics_wgs/predict.sh

Map: nanopore-wgs/scripts/cyclomics_wgs/map_score.sh

Cycas Consensus files: /hpc/compgen/projects/gw_cfdna/gw_cyclomics/analysis/lchen/cycloseq-output/HC02_CYC36-20ng/bams/HC02_CYC36-20ng.tagged.bam

Cycas Consensus files filtered for overlapping SNPs and indels: nanopore-wgs/data/cyclomics_wgs_cons_intersect/cons_gwcycl_intersect.sorted.bam


## Data folders
### Model training/testing
nanopore-wgs/rel8: mapped reads to chr18 from Nanopore T2T dataset used for sample generation. Forward reads only. 

nanopore-wgs/data/traintest: samples for DNN training, testing and hyperparameter optimization

nanopore-wgs/data/ref_per_chromosome: used for generation of samples

### CyclomicsSeq dataset A
/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict: mapped CyclomicsSeq reads and vcf files used for generation of input samples

nanopore-wgs/data/predict_cyclomics_clean_maskedrefbase: input samples generated from mapped CyclomicsSeq reads 

nanopore-wgs/data/predict_cyclomics_clean_fastq_maskedrefbase: sequences predicted by each model 

nanopore-wgs/data/predict_cyclomics_clean_bam_maskedrefbase: mapped sequences predicted by each model


### CyclomicsSeq dataset B
nanopore-wgs/data/cyclomics_muts_vcf_perregion: vcf files used for generation of input samples 

nanopore-wgs/data/cyclomics_muts_bam_perregion: mapped CyclomicsSeq reads used as input to generate samples 

nanopore-wgs/data/cyclomics_muts_hdf5: input samples generated from mapped CyclomicsSeq reads 

nanopore-wgs/data/cyclomics_muts_fastq: sequences predicted by each model 

nanopore-wgs/data/cyclomics_muts_bam_output: mapped sequences predicted by each model


### CyclomicsSeq dataset C
nanopore-wgs/data/cyclomics_wgs_bam_input: mapped CyclomicsSeq reads used as input to generate samples 

nanopore-wgs/data/cyclomics_wgs_hdf5_maskedrefbase:  input samples generated from mapped CyclomicsSeq reads 

nanopore-wgs/data/cyclomics_wgs_fastq_maskedrefbase: equences predicted by each model 

nanopore-wgs/data/cyclomics_wgs_bam_output_maskedrefbase: mapped sequences predicted by each model

nanopore-wgs/data/cyclomics_wgs_bam_output_maskedrefbase_intersect: mapped sequences predicted by each model without reads overlapping with known SNPs or indels

nanopore-wgs/data/cyclomics_wgs_cons_intersect: Cycas Consensus sequences without reads overlapping with known SNPs or indels







