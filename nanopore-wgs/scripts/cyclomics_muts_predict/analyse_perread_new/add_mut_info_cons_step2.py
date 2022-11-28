import time
start = time.time()
import pandas as pd
import pysam
import os


df_cons = pd.read_csv('/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/cyclomics_muts_predict/analyse_perread_new/csv_files_perregion/cycl_muts_consensus_t2t_perread_mutinfo.csv')
print(f'number of rows: {df_cons.shape}')
print(list(df_cons.columns))
df_cons.drop(columns=['Unnamed: 0'], inplace=True)
print(df_cons.shape)

print(df_cons[df_cons['region_readid'].str.contains('772a60de-3d0a-4d29-8ab9-6ab4010231c2')])
print(df_cons[df_cons['region_readid'].str.contains('7015defe-49e0-4c0a-8f0f-ef46961aaeaa')])

print(df_cons['region'].value_counts())
print(df_cons['mut3'].value_counts())


df_cons['NM-mut'] = df_cons.apply(lambda row: row['cons-NM'] - (row['mut1'] + row['mut2'] + row['mut3'] + row['mut4'] + row['mut5'] ), axis=1)

print(df_cons['cons-align_length'].value_counts(ascending=True))
print(df_cons[df_cons['cons-align_length'] > 200]['cons-align_length'].value_counts(ascending=True))
print(df_cons[df_cons['cons-align_length'] > 200].value_counts(ascending=True).shape)

df_cons.drop(df_cons[df_cons['cons-align_length'] > 200].index, inplace=True)
print(df_cons.shape)

print(df_cons[df_cons['NM-mut'] == -1])
print(df_cons[df_cons['NM-mut'] == -1]['cons-readid'].to_string())
print(df_cons.loc[24694, 'cons-readid'])
print(df_cons.loc[125213, 'cons-readid'])
print(df_cons[df_cons['region_readid'].str.contains('772a60de-3d0a-4d29-8ab9-6ab4010231c2')])
print(df_cons[df_cons['region_readid'].str.contains('7015defe-49e0-4c0a-8f0f-ef46961aaeaa')])
df_cons.drop(df_cons.index[df_cons['NM-mut'] == -1], inplace = True)

df_cons['cons-score-NM'] = df_cons.apply(lambda row: row['NM-mut']/row['cons-align_length'], axis=1)

# print(df_cons.shape)
# print(df_cons.head)

# print(df_cons[df_cons['region_readid'].str.contains('772a60de-3d0a-4d29-8ab9-6ab4010231c2')])
# print(df_cons[df_cons['region_readid'].str.contains('7015defe-49e0-4c0a-8f0f-ef46961aaeaa')])

# df_cons.to_csv('/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/cyclomics_muts_predict/analyse_perread_new/csv_files_perregion/cycl_muts_consensus_t2t_perread_mutinfo_step2.csv')
