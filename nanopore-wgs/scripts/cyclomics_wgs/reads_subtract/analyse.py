import pandas as pd

# pred csv file
df_pred = pd.read_csv('csv_files/cycl_wgs_predict_t2t_select_chr.csv')
print(f'nr of reads in prediction: {df_pred.shape}')
df_pred.drop(columns=['Unnamed: 0'], inplace=True)
df_pred["chr"]=df_pred["chr"].apply(str)
df_pred['chr-readid'] = df_pred['chr'] + '_' + df_pred['pred-readid']
print(df_pred.head(), '\n')

# subset for unique read ids in prediction per model
print(f'number of reads per model before removing duplicates:\n {df_pred["model-cov"].value_counts()}')
print(f'number of rows before removing duplicates based on region readid and model cov: {df_pred.shape}')
df_pred = df_pred.sort_values('pred-align_length', ascending=False).drop_duplicates(subset=['chr-readid', 'model-cov'])
print(f'number of rows after removing duplicates based on chr readid and model cov: {df_pred.shape}')
print(f'number of reads after model after removing duplicates:\n {df_pred["model-cov"].value_counts()}\n')

# consensus csv file
df_cons = pd.read_csv('csv_files/cycl_wgs_cons_t2t_select_chr.csv')
print(f'nr of reads in consensus: {df_cons.shape}')
df_cons.drop(columns=['Unnamed: 0'], inplace=True)
df_cons["chr"]=df_cons["chr"].apply(str)
df_cons['chr-readid'] = df_cons['chr'] + '_' + df_cons['cons-readid']
print(df_cons.head(), '\n')

# subset for unique read ids in consensus
print(f'number of unique chr - read ids in consensus: {len(set(df_cons["chr-readid"]))}')
df_cons = df_cons.sort_values('cons-align_length', ascending=False).drop_duplicates(subset=['chr-readid'])
df_cons = df_cons.sort_index()
print(f'number of reads in consensus after drop duplicates: {df_cons.shape}\n')

# concat dataframes
# keep only chr-read ids that occur 6 times (in all models + in cycas)
df_pred_select = df_pred.rename(columns = {'pred-readid': 'readid', 'pred-NM':'NM', 'pred-align_length':'align_length', 'pred-cigar':'cigar', 'pred-score':'score'})
df_cons_select = df_cons.rename(columns = {'cons-readid': 'readid', 'cons-NM':'NM', 'cons-align_length':'align_length', 'cons-cigar':'cigar', 'cons-score':'score'})
df_concat = pd.concat([df_cons_select, df_pred_select], join='outer')
print(f'shape of concatenated dataframe: {df_concat.shape}')

freq = df_concat['chr-readid'].value_counts()
items = freq[freq == 6].index
df_concat = df_concat[df_concat['chr-readid'].isin(items)]
print(f'shape of dataframe with only overlapping read ids per chr: {df_concat.shape}')
print(df_concat['model-cov'].value_counts(ascending=True))
print(df_concat.head(), '\n')



