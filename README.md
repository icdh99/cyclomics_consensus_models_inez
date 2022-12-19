# Consensus Calling and Validation of Single Nucleotide Variant Calling from Nanopore Sequencing with Deep Learning for CyclomicsSeq

This repository contains the code for my internship project performed at the UMC Utrecht. 

## Model training
The files nanopore-wgs/scripts/model_maskrefbase/model_cnn_trainfinalmodel.py and nanopore-wgs/scripts/model_maskrefbase/model_cnn_trainfinalmodel.py are the scripts to train the final DNN and CNN models.

## Consensus calling for CyclomicsSeq dataset A
The files nanopore-wgs/scripts/cyclomics_clean_predict_maskedrefbase/predict_qs.py and nanopore-wgs/scripts/cyclomics_clean_predict_maskedrefbase/map_score.sh contain the script to perform the consensus calling prediction and mapping for CyclomicsSeq dataset A.

## Consensus calling for CyclomicsSeq dataset B
The files nanopore-wgs/scripts/cyclomics_clean_predict_maskedrefbase/predict_qs.py and nanopore-wgs/nanopore-wgs/scripts/cyclomics_muts_predict/map_score.sh contain the script to perform the consensus calling prediction and mapping for CyclomicsSeq dataset B.

## Consensus calling for CyclomicsSeq dataset C
The files nanopore-wgs/scripts/nanopore-wgs/scriptscyclomics_wgs/predict_qs.py and nanopore-wgs/scripts/cyclomics_wgs/map_score.sh contain the script to perform the consensus calling prediction and mapping for CyclomicsSeq dataset C.
