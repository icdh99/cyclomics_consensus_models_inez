# Consensus Calling and Validation of Single Nucleotide Variant Calling from Nanopore Sequencing with Deep Learning for CyclomicsSeq

CyclomicsSeq is a sequencing technique developed to sequence cell-free DNA and is based on Nanopore sequencing. Cell-free DNA (cfDNA) fragments can be found in the bloodstream and can be derived from both healthy and tumour cells, in the latter situation it is called circulating tumour DNA (ctDNA). ctDNA fragments provide a valuable source for tumour single nucleotide variant calling. Nanopore sequencing has a high error rate and makes systematic sequencing errors, that is that it makes the same sequencing error more often in the same sequence context. Therefore, the CyclomicsSeq method sequences every ctDNA fragment multiple times by rolling circle amplification and consensus calling of the multiple sequenced copies of the same original ctDNA fragment. With the consensus calling step, the ctDNA sequence can be determined and random sequencing errors are removed. However, systematic sequencing errors persist and interfere with single nucleotide variant calling. Here, we propose a deep learning method to perform the consensus calling step for CyclomicsSeq. The model will be trained on Nanopore sequencing reads and thus be able to circumvent systematic sequencing errors in the consensus calling step.

This repository contains the code for my internship project performed at the UMC Utrecht. 

## General workflow of the project
First, we train a deep learning model. We train a Dense Neural Network (DNN) and a Convolutional Neural Network (CNN) on reads that have been sequenced with Nanopore sequencing (https://github.com/marbl/CHM13/blob/master/Sequencing_data.md). We create a sample for each position and store the reference base for that position as the label for that sample. The model is trained to predict the label for each sample. We train models on different coverages of the reads. When the models perform well, they can be used for the consensus calling step for CyclomicsSeq. We have 10 models (5x DNN, 5x CNN) trained on different coverage of the reads (3-5X, 6-10X, 11-15X, 16-20X, 3-20X).

The CyclomicsSeq copies of one ctDNA fragment are converted into samples as well. The coverage of the sample is determined by the number of copies per ctDNA fragment. The samples are then predicted using all models. The model outputs a fastq sequence per original ctDNA fragment. These sequences are mapped to the corresponding reference genome. We benchmark our model's performance against the current CyclomicsSeq consensus calling method 

## Model training
The final models can be found in the folders `nanopore-wgs/scripts/model_maskrefbase/model_cnn_c5_finalmodel` with cnn being either cnn or dnn and c5 indicating the coverage bin of the model (c5 = 3-5X, c10 = 6-10X, c15 = 11-15X, c20 = 16-20X, c100 = 3-20X).

The files `nanopore-wgs/scripts/model_maskrefbase/model_cnn_trainfinalmodel.py` and `nanopore-wgs/scripts/model_maskrefbase/model_cnn_trainfinalmodel.py` are the scripts to train the final DNN and CNN models.

Scripts for cross-validation, tuning and testing of the DNN and CNN model can be found in the same folder. 

### Majority vote for benchmarking of model performance
The scripts to calculate the majority vote performance can be found in the folder `nanopore-wgs/scripts/majority_vote_withoutrefbase`

## Consensus calling for CyclomicsSeq dataset A ('clean' dataset)
Raw data: `raw/CYC000025-extended-data`

Create samples: `nanopore-wgs/scripts/matrix/predict_cyclomics/make_matrix.sh`

For each CyclomicsSeq dataset, the samples are created using the bam files in the `CycasConsensus/MapQandNMFilter` folder.

Predict: `nanopore-wgs/scripts/cyclomics_clean_predict_maskedrefbase/predict.sh`

Map: `nanopore-wgs/scripts/cyclomics_clean_predict_maskedrefbase/map_score.sh`

Cycas Consensus files: `raw/CYC000025-extended-data/Minimap2Align/SamtoolsMergeBams/FAU48563.merged.bam`

## Consensus calling for CyclomicsSeq dataset B (mutation dataset)
Raw data: `raw/000025-sup-extended-data`

Create samples: `nanopore-wgs/scripts/cyclomics_muts_prep_matrix/make_matrix.sh`

Predict: `nanopore-wgs/scripts/cyclomics_muts_predict/predict.sh`

Map: `nanopore-wgs/scripts/cyclomics_muts_predict/map_score.sh`

Cycas Consensus files: `raw/cyclomics_mutations_dataset_cleanconsensus/cyclomics_muts_consensus_chr17_YM3filter.sorted.bam`

## Consensus calling for CyclomicsSeq dataset C (genome-wide dataset)
Raw data: `/hpc/compgen/projects/gw_cfdna/gw_cyclomics/analysis/lchen/cycloseq-output/HC02_CYC36-20ng/CycasConsensus/MapqAndNMFilter`

Create samples: `nanopore-wgs/scripts/cyclomics_wgs/make_matrix.sh`

Predict: `nanopore-wgs/scripts/cyclomics_wgs/predict.sh`

Map: `nanopore-wgs/scripts/cyclomics_wgs/map_score.sh`

Cycas Consensus files: `/hpc/compgen/projects/gw_cfdna/gw_cyclomics/analysis/lchen/cycloseq-output/HC02_CYC36-20ng/bams/HC02_CYC36-20ng.tagged.bam`

Cycas Consensus files filtered for overlapping SNPs and indels: `nanopore-wgs/data/cyclomics_wgs_cons_intersect/cons_gwcycl_intersect.sorted.bam`


## Data folders
### Model training/testing
`nanopore-wgs/rel8`: mapped reads to chr18 from Nanopore T2T dataset used for sample generation. Forward reads only. 

`nanopore-wgs/data/traintest`: samples for DNN training, testing and hyperparameter optimization

`nanopore-wgs/data/ref_per_chromosome`: used for generation of samples

### CyclomicsSeq dataset A
`/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict`: mapped CyclomicsSeq reads and vcf files used for generation of input samples

`nanopore-wgs/data/predict_cyclomics_clean_maskedrefbase`: input samples generated from mapped CyclomicsSeq reads 

`nanopore-wgs/data/predict_cyclomics_clean_fastq_maskedrefbase`: sequences predicted by each model 

`nanopore-wgs/data/predict_cyclomics_clean_bam_maskedrefbase`: mapped sequences predicted by each model


### CyclomicsSeq dataset B
`nanopore-wgs/data/cyclomics_muts_vcf_perregion`: vcf files used for generation of input samples 

`nanopore-wgs/data/cyclomics_muts_bam_perregion`: mapped CyclomicsSeq reads used as input to generate samples 

`nanopore-wgs/data/cyclomics_muts_hdf5`: input samples generated from mapped CyclomicsSeq reads 

`nanopore-wgs/data/cyclomics_muts_fastq:` sequences predicted by each model 

`nanopore-wgs/data/cyclomics_muts_bam_output`: mapped sequences predicted by each model


### CyclomicsSeq dataset C
`nanopore-wgs/data/cyclomics_wgs_bam_input`: mapped CyclomicsSeq reads used as input to generate samples 

`nanopore-wgs/data/cyclomics_wgs_hdf5_maskedrefbase`:  input samples generated from mapped CyclomicsSeq reads 

`nanopore-wgs/data/cyclomics_wgs_fastq_maskedrefbase`: sequences predicted by each model 

`nanopore-wgs/data/cyclomics_wgs_bam_output_maskedrefbase`: mapped sequences predicted by each model

`nanopore-wgs/data/cyclomics_wgs_bam_output_maskedrefbase_intersect`: mapped sequences predicted by each model without reads overlapping with known SNPs or indels

`nanopore-wgs/data/cyclomics_wgs_cons_intersect`: Cycas Consensus sequences without reads overlapping with known SNPs or indels







