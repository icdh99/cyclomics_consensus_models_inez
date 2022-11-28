import time
start = time.time()
import pandas as pd
# import pysam
# import os

print('a')
df_pred = pd.read_csv('/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/cyclomics_muts_predict/analyse_perread_new/csv_files_perregion/cycl_muts_predict_t2t_perread_mutinfo.csv')
print(f'number of rows: {df_pred.shape}')
print(list(df_pred.columns))
df_pred.drop(columns=['Unnamed: 0', 'cons-score-NM'], inplace=True)
print(df_pred.shape)


df_pred['NM-mut'] = df_pred.apply(lambda row: row['pred-NM'] - (row['mut1'] + row['mut2'] + row['mut3'] + row['mut4'] + row['mut5'] ), axis=1)

# print(df_pred['pred-align_length'].value_counts(ascending=True)) # langste read is 162 bp! 

df_pred['pred-score-NM'] = df_pred.apply(lambda row: row['NM-mut']/row['pred-align_length'], axis=1)

print(df_pred.shape)
print(df_pred.head)

df_pred.to_csv('/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/cyclomics_muts_predict/analyse_perread_new/csv_files_perregion/cycl_muts_predict_t2t_perread_mutinfo_step2.csv')

end = time.time()
print("The time of execution is :", end-start)