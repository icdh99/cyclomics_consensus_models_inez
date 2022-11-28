import pandas as pd
import numpy as np

# prediction dataframe
df_pred = pd.read_csv('/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/cyclomics_muts_predict/analyse_perread_new/csv_files_perregion/cycl_muts_predict_t2t_perread_mutinfo_step2.csv')
print(f'nr of reads for Cycas Consensus: {df_pred.shape}')
df_pred.drop(columns=['Unnamed: 0'], inplace=True)

for i, model_cov in enumerate(['dnn_c5', 'dnn_c10', 'dnn_c15', 'dnn_c20', 'dnn_c100', 'cnn_c5', 'cnn_c10', 'cnn_c15', 'cnn_c20', 'cnn_c100']):
    print(f'number of reads for {model_cov}: {df_pred[df_pred["model-cov"] == model_cov].shape[0]}')

print(df_pred['region'].value_counts())

# consensus dataframe
df_cons = pd.read_csv('/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/cyclomics_muts_predict/analyse_perread_new/csv_files_perregion/cycl_muts_consensus_t2t_perread_mutinfo_step2.csv')
print(f'nr of reads for Cycas Consensus: {df_cons.shape}')
df_cons.drop(columns=['Unnamed: 0'], inplace=True)
print(df_cons['region'].value_counts())

df_pred_select = df_pred.rename(columns = {'pred-readid': 'readid', 'pred-readid-short': 'readid-short', 'pred-NM':'NM', 'pred-align_length':'align_length', 'pred-cigar':'cigar', 'pred-score':'score', 'pred-score-NM':'score-NM'})
df_cons_select = df_cons.rename(columns = {'cons-readid': 'readid', 'cons-readid-short': 'readid-short', 'cons-NM':'NM', 'cons-align_length':'align_length', 'cons-cigar':'cigar', 'cons-score':'score', 'cons-score-NM':'score-NM'})
df_concat = pd.concat([df_cons_select, df_pred_select], join='outer')
print(f'shape of concatenated dataframe: {df_concat.shape}')

# concat dataframe
# all rows below each other for each model
# keep only readids that occur 11x = in all models + cycas
freq = df_concat['region_readid'].value_counts()
items = freq[freq == 11].index
df_concat = df_concat[df_concat['region_readid'].isin(items)]
df_concat.drop(columns = ['pred-model-only', 'pred-cov-only'], inplace = True)
print(df_concat['model-cov'].value_counts(ascending=True))
print(df_concat.shape)
print(df_concat.head())
print(df_concat.columns)

print(len(set(df_concat[df_concat['model-cov'] == 'Cycas Consensus']['readid'])))
df_region1 = df_concat[(df_concat['model-cov'] == 'dnn_c5') & (df_concat['region'] == 'region1')]
print(df_region1.shape)
print(len(set(df_concat[(df_concat['model-cov'] == 'dnn_c5') & (df_concat['region'] == 'region1')]['region_readid'])))

for region in ['region1', 'region3', 'region4', 'region5']:
    print(len(set(df_concat[(df_concat['model-cov'] == 'dnn_c5') & (df_concat['region'] == region)]['region_readid'])))
    with open(f'readid_unique_short_{region}.txt', 'w') as f:
        f.truncate(0)
        for line in set(df_concat[(df_concat['model-cov'] == 'dnn_c5') & (df_concat['region'] == region)]['region_readid']):
            # print(line)
            readid_short = line.split('_')[1]
            f.write(f"{readid_short}\n")

# with open('readid_unique_long.txt', 'w') as f:
#     for line in set(df_concat[df_concat['model-cov'] == 'Cycas Consensus']['readid']):
#         # print(line)
#         f.write(f"{line}\n")
        


        

# with open('readid_unique_short.txt', 'w') as f:
#     for line in df_concat['readid_short']