import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# DF PRED
df_pred = pd.read_csv('/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/cyclomics_clean_predict_maskedrefbase/analyse_perread/cycl_clean_predict_t2t_perread.csv')
print(f'nr of reads for prediction: {df_pred.shape}')
df_pred['read-cov'] = df_pred['pred-read-cov']
print(df_pred.head())
print(df_pred['region'].value_counts())
df_pred.drop(df_pred[df_pred['region'] == 'region_unknown'].index, inplace = True)
# for i, model_cov in enumerate(['c5', 'c10', 'c15', 'c20', 'c100']): print(f'number of reads for {model_cov} before removing duplicate read ids: {df_pred[df_pred["pred-model-cov"] == model_cov].shape[0]}')
df_pred = df_pred.sort_values('pred-align_length', ascending=False).drop_duplicates(subset=['region_readid', 'pred-model-cov'])
for i, model_cov in enumerate(['c5', 'c10', 'c15', 'c20', 'c100']): print(f'number of reads for {model_cov} after removing duplicate read ids: {df_pred[df_pred["pred-model-cov"] == model_cov].shape[0]}')

# DF CONS
df_cons = pd.read_csv('/hpc/compgen/projects/gw_cfdna/snv_qs/predict_cyclclean_with_lambdamodel/cycl_clean_consensus_scoreperread/cycl_clean_consensus_properties_per_read.csv')
df_cons['region_readid'] = df_cons['region'] + '_' + df_cons['cons-readid-short']
df_cons['model-cov'] = 'Cycas Consensus'
df_cons['read-cov'] = df_cons.apply(lambda row: '20+X' if row['cons-YM'] > 20 else str(int(row['cons-YM'])) + 'X', axis = 1)
# df_cons['read-cov'] = df_cons['cons-YM'] + 'X'
print(df_cons.head())
print(f'number of rows before removing duplicates based on region readid and model cov: {df_cons.shape}')
df_cons = df_cons.sort_values('cons-align_length', ascending=False).drop_duplicates(subset=['region_readid'])
print(f'number of rows after removing duplicates based on region readid and model cov: {df_cons.shape}')

# DF CONCAT
df_pred_select = df_pred.rename(columns = {'pred-readid': 'readid', 'pred-readid-short': 'readid-short', 'pred-NM':'NM', 'pred-align_length':'align_length', 'pred-cigar':'cigar', 'pred-score':'score', 'pred-score-NM':'score-NM', 'pred-model-cov':'model-cov'})
df_cons_select = df_cons.rename(columns = {'cons-readid': 'readid', 'cons-readid-short': 'readid-short', 'cons-NM':'NM', 'cons-align_length':'align_length', 'cons-cigar':'cigar', 'cons-score':'score', 'cons-score-NM':'score-NM'})
df_concat = pd.concat([df_cons_select, df_pred_select], join='outer', ignore_index = True)
df_concat['q_score'] = df_concat.apply(lambda row: 0.00001 if row['score'] == 0 else row['score'], axis = 1)
print(df_concat['model-cov'].value_counts(ascending=True))
print(f'shape of concatenated dataframe: {df_concat.shape}')
print(df_concat.head())

# DF CONCAT OVERLAP
freq = df_concat['region_readid'].value_counts()
items = freq[freq == 6].index
df_concat_overlap = df_concat[df_concat['region_readid'].isin(items)]
print(df_concat_overlap['model-cov'].value_counts(ascending=True))

# # CALCULATE MEDIAN OVERLAP PER MODEL
print(f'median score per model')
print(f'Cycas: {df_concat_overlap[df_concat_overlap["model-cov"] == "Cycas Consensus"]["score"].median()}')
print(f'DNN c5: {df_concat_overlap[df_concat_overlap["model-cov"] == "c5"]["score"].median()}')
print(f'DNN c10: {df_concat_overlap[df_concat_overlap["model-cov"] == "c10"]["score"].median()}')
print(f'DNN c15: {df_concat_overlap[df_concat_overlap["model-cov"] == "c15"]["score"].median()}')
print(f'DNN c20: {df_concat_overlap[df_concat_overlap["model-cov"] == "c20"]["score"].median()}')
print(f'DNN c100: {df_concat_overlap[df_concat_overlap["model-cov"] == "c100"]["score"].median()}')

print(f'median q score per model')
print(f'Cycas: {df_concat_overlap[df_concat_overlap["model-cov"] == "Cycas Consensus"]["q_score"].median()}')
print(f'DNN c5: {df_concat_overlap[df_concat_overlap["model-cov"] == "c5"]["q_score"].median()}')
print(f'DNN c10: {df_concat_overlap[df_concat_overlap["model-cov"] == "c10"]["q_score"].median()}')
print(f'DNN c15: {df_concat_overlap[df_concat_overlap["model-cov"] == "c15"]["q_score"].median()}')
print(f'DNN c20: {df_concat_overlap[df_concat_overlap["model-cov"] == "c20"]["q_score"].median()}')
print(f'DNN c100: {df_concat_overlap[df_concat_overlap["model-cov"] == "c100"]["q_score"].median()}')

print(f'mean score per model')
print(f'Cycas: {df_concat_overlap[df_concat_overlap["model-cov"] == "Cycas Consensus"]["score"].mean()}')
print(f'DNN c5: {df_concat_overlap[df_concat_overlap["model-cov"] == "c5"]["score"].mean()}')
print(f'DNN c10: {df_concat_overlap[df_concat_overlap["model-cov"] == "c10"]["score"].mean()}')
print(f'DNN c15: {df_concat_overlap[df_concat_overlap["model-cov"] == "c15"]["score"].mean()}')
print(f'DNN c20: {df_concat_overlap[df_concat_overlap["model-cov"] == "c20"]["score"].mean()}')
print(f'DNN c100: {df_concat_overlap[df_concat_overlap["model-cov"] == "c100"]["score"].mean()}')

print(f'mean q score per model')
print(f'Cycas: {df_concat_overlap[df_concat_overlap["model-cov"] == "Cycas Consensus"]["q_score"].mean()}')
print(f'DNN c5: {df_concat_overlap[df_concat_overlap["model-cov"] == "c5"]["q_score"].mean()}')
print(f'DNN c10: {df_concat_overlap[df_concat_overlap["model-cov"] == "c10"]["q_score"].mean()}')
print(f'DNN c15: {df_concat_overlap[df_concat_overlap["model-cov"] == "c15"]["q_score"].mean()}')
print(f'DNN c20: {df_concat_overlap[df_concat_overlap["model-cov"] == "c20"]["q_score"].mean()}')
print(f'DNN c100: {df_concat_overlap[df_concat_overlap["model-cov"] == "c100"]["q_score"].mean()}')

exit()

# NR OF READS PER MODEL PER COVERAGE BIN NON OVERLAP
plt.figure(1)
fig, ax = plt.subplots(figsize=(16.7, 8.27))
coverage = ['3X','4X','5X','6X','7X','8X','9X','10X','11X','12X','13X', '14X','15X','16X','17X','18X','19X','20X','20+X']
hue_order = ['Cycas Consensus', 'c5', 'c10', 'c15', 'c20', 'c100']
ax = sns.countplot(data=df_concat, x = 'read-cov', hue = 'model-cov', order = coverage, hue_order = hue_order, palette = sns.color_palette("Paired", 19))
labels = [f'Cycas Consensus', f'DNN 3-5X', f'DNN 6-10X', f'DNN 11-15X', f'DNN 16-20X', f'DNN 3-20X']
ax.legend(loc='upper right', bbox_to_anchor=(1,1), labels = labels, title = 'Model type')
plt.xlabel('Nr. copies per CyclomicsSeq read')
plt.ylabel('Count')
plt.savefig('plot1_nrreads_nonoverlap.png', bbox_inches='tight')
plt.close()

# NR OF READS PER MODEL PER COVERAGE BIN OVERLAP
plt.figure(1)
fig, ax = plt.subplots(figsize=(16.7, 8.27))
coverage = ['3X','4X','5X','6X','7X','8X','9X','10X','11X','12X','13X', '14X','15X','16X','17X','18X','19X','20X','20+X']
hue_order = ['Cycas Consensus', 'c5', 'c10', 'c15', 'c20', 'c100']
ax = sns.countplot(data=df_concat_overlap, x = 'read-cov', hue = 'model-cov', order = coverage, hue_order = hue_order, palette = sns.color_palette("Paired", 19))
plt.xlabel('Nr. copies per CyclomicsSeq read')
plt.ylabel('Count')
labels = [f'Cycas Consensus', f'DNN 3-5X', f'DNN 6-10X', f'DNN 11-15X', f'DNN 16-20X', f'DNN 3-20X']
ax.legend(loc='upper right', bbox_to_anchor=(1,1), labels = labels, title = 'Model type')
plt.savefig('plot1_nrreads_overlap.png', bbox_inches='tight')
plt.close()
 
# NR OF READS PER MODEL PER COVERAGE BIN OVERLAP ONLY CYCAS



plt.figure(1)
fig, ax = plt.subplots(figsize=(16.7, 8.27))
coverage = ['3X','4X','5X','6X','7X','8X','9X','10X','11X','12X','13X', '14X','15X','16X','17X','18X','19X','20X','20+X']
hue_order = ['Cycas Consensus']
ax = sns.countplot(data=df_concat_overlap, x = 'read-cov', hue = 'model-cov', order = coverage, hue_order = hue_order, palette = sns.color_palette("Paired", 19),)
plt.xlabel('Nr. copies per CyclomicsSeq read')
plt.ylabel('Count')
labels = [f'Cycas Consensus']
ax.get_legend().remove()
# ax.legend(loc='upper right', bbox_to_anchor=(1,1), labels = labels, title = 'Model type')
plt.savefig('plot1_nrreads_overlap_cycasonly.png', bbox_inches='tight')
plt.close()



# MEAN ERROR RATE ALL READS PER MODEL OVERLAP/NON OVERLAP
plt.figure(2)

        
cycas = '#a6cee3'
dnnc5 = '#1f78b4'
dnnc10 = '#b2df8a'
dnnc15 = '#33a02c'
dnnc20 = '#fb9a99'
dnnc100 = '#e31a1c'
cnnc5 = '#fdbf6f'
cnnc10 = '#ff7f00'
cnnc15 = '#cab2d6'
cnnc20 = '#6a3d9a'
cnnc100 = '#ffff99'
expected_brown = '#b15928'
palette = [cycas, dnnc5, dnnc10, dnnc15, dnnc20, dnnc100, cnnc5, cnnc10, cnnc15, cnnc20, cnnc100]

fig, ax = plt.subplots(figsize=(16.7, 8.27))
coverage = ['3X','4X','5X','6X','7X','8X','9X','10X','11X','12X','13X', '14X','15X','16X','17X','18X','19X','20X','20+X']
hue_order = ['Cycas Consensus', 'c5', 'c10', 'c15', 'c20', 'c100']
ax = sns.barplot(data=df_concat_overlap, x='read-cov', hue='model-cov', y ='score', order=coverage, hue_order=hue_order, palette=sns.color_palette(palette, 6))
plt.xlabel('Nr. copies per CyclomicsSeq read')
plt.ylabel('Per-read error rate')
labels = [f'Cycas Consensus', f'DNN 3-5X', f'DNN 6-10X', f'DNN 11-15X', f'DNN 16-20X', f'DNN 3-20X']
h, l = ax.get_legend_handles_labels()
ax.legend(h, labels, loc='upper right', bbox_to_anchor=(1,1), title = 'Model type')
plt.savefig('plot2_meanerrorrate_allreads_overlap_percovbin.png', bbox_inches='tight')
plt.close()

exit()

plt.figure(2)
fig, ax = plt.subplots(figsize=(8,4))
order = ['Cycas Consensus', 'c5', 'c10', 'c15', 'c20', 'c100']
sns.barplot(data=df_concat_overlap, x='model-cov', y ='score', order=order,  palette = sns.color_palette("Paired", 6))
plt.ylabel('Per-read error rate')
plt.xlabel('Model type')
labels = [f'Cycas\nConsensus', f'DNN\n3-5X', f'DNN\n6-10X', f'DNN\n11-15X', f'DNN\n16-20X', f'DNN\n3-20X']
plt.xticks(np.arange(0, len(labels)), labels)
plt.savefig('plot2B_meanerrorrate_allreads_overlap.png', bbox_inches='tight')
plt.close()

plt.figure(2)
fig, ax = plt.subplots(figsize=(8,4))
order = ['Cycas Consensus', 'c5', 'c10', 'c15', 'c20', 'c100']
sns.barplot(data=df_concat, x='model-cov', y ='score', order=order,  palette = sns.color_palette("Paired", 6))
plt.savefig('plot2D_meanerrorrate_allreads_nonoverlap.png', bbox_inches='tight')
plt.close()

# plt.figure(2)
# fig, ax = plt.subplots(figsize=(8,4))
# order = ['Cycas Consensus', 'c5', 'c10', 'c15', 'c20', 'c100']
# sns.barplot(data=df_concat_overlap, x='model-cov', y ='q_score', order=order,  palette = sns.color_palette("Paired", 6))
# ticks = [10**-6, 10**-5, 10**-4, 10**-3, 10**-2, 10**-1, 10**0]
# labels = ['Q60', 'Q50', 'Q40', 'Q30', 'Q20', 'Q10', 'Q1' ]
# plt.yscale('log')
# plt.yticks(ticks, labels)
# plt.savefig('plot2C_meanerrorrate_allreads_overlap.png', bbox_inches='tight')
# plt.close()

plt.figure(3)
fig, ax = plt.subplots(figsize=(16.7, 8.27))
coverage = ['3X','4X','5X','6X','7X','8X','9X','10X','11X','12X','13X', '14X','15X','16X','17X','18X','19X','20X','20+X']
hue_order = ['Cycas Consensus', 'c5', 'c10', 'c15', 'c20', 'c100']
ax = sns.barplot(data=df_concat, x='read-cov', hue='model-cov', y ='score', order=coverage, hue_order=hue_order, palette = sns.color_palette("Paired", 6))
labels_legend = ['Cycas Consensus', 'DNN 3-5X', 'DNN 6-10X', 'DNN 11-15X', 'DNN 16-20X', 'DNN 3-20X']
ax.legend(loc='upper right', bbox_to_anchor=(1,1), labels = labels_legend, title = 'Model type')
plt.xlabel('Nr. copies per CyclomicsSeq read')
plt.ylabel('Per-read error rate')
plt.savefig('plot3_meanerrorrate_allreads_nonoverlap.png', bbox_inches='tight')
plt.close()



# MEAN ERROR RATE ALL READS PER MODEL OVERLAP 
# plt.figure(4)
# plt.figure(figsize=(16.7, 8.27))
# column_order = ['Cycas Consensus', 'dnn_c5', 'dnn_c10', 'dnn_c15', 'dnn_c20', 'dnn_c100', 'cnn_c5', 'cnn_c10', 'cnn_c15', 'cnn_c20', 'cnn_c100']
# ax = sns.barplot(data=df_concat_overlap, x = 'read-cov', y ='q_score', hue = 'model-cov', palette = sns.color_palette("Paired", 6), hue_order=hue_order, order = coverage ) 
# # plt.xlabel('Model type')
# # plt.ylabel('Error rate')
# # plt.ylim(bottom = -0.01)
# ticks = [10**-6, 10**-5, 10**-4, 10**-3, 10**-2, 10**-1, 10**0]
# labels = ['Q60', 'Q50', 'Q40', 'Q30', 'Q20', 'Q10', 'Q1' ]
# plt.yscale('log')
# plt.yticks(ticks, labels)
# labels = [f'Cycas\nConsensus', f'DNN\n3-5X', f'DNN\n6-10X', f'DNN\n11-15X', f'DNN\n16-20X', f'DNN\n3-20X', f'CNN\n3-5X', f'CNN\n6-10X', f'CNN\n11-15X', f'CNN\n16-20X', f'CNN\n3-20X']
# plt.savefig('plot4_mean_qscore_allreads_overlap.png', bbox_inches='tight')
# plt.close()

# plt.figure(5)
# plt.figure(figsize=(16.7, 8.27))
# column_order = ['Cycas Consensus', 'dnn_c5', 'dnn_c10', 'dnn_c15', 'dnn_c20', 'dnn_c100', 'cnn_c5', 'cnn_c10', 'cnn_c15', 'cnn_c20', 'cnn_c100']
# ax = sns.barplot(data=df_concat_overlap, x = 'read-cov', y ='q_score', hue = 'model-cov', palette = sns.color_palette("Paired", 6), hue_order=hue_order, order = coverage ) 
# # plt.xlabel('Model type')
# # plt.ylabel('Error rate')
# # plt.ylim(bottom = -0.01)
# labels = [f'Cycas\nConsensus', f'DNN\n3-5X', f'DNN\n6-10X', f'DNN\n11-15X', f'DNN\n16-20X', f'DNN\n3-20X', f'CNN\n3-5X', f'CNN\n6-10X', f'CNN\n11-15X', f'CNN\n16-20X', f'CNN\n3-20X']
# plt.savefig('plot5_mean_score_allreads_overlap.png', bbox_inches='tight')
# plt.close()

# MEAN ERROR RATE ALL READS PER MODEL NON-OVERLAP

# MEDIAN ERROR RATE ALL READS PER MODEL NON-OVERLAP 

# DF OVERLAP PERFECT
df_concat_perfect_overlap = df_concat_overlap[df_concat_overlap['score'] == 0]
print(f'total number of perfect reads in overlap: {df_concat_perfect_overlap.shape}')

# DF NON-OVERLAP PERFECT
df_concat_perfect = df_concat[df_concat['score'] == 0]
print(f'total number of perfect reads in non overlap: {df_concat_perfect.shape}')

print(df_concat[df_concat['score'] == 0]['score'].shape)

# PERCENTAGE PERFECT READS OVERLAP
df_perc_perfect_overlap = df_concat_perfect_overlap['model-cov'].value_counts().rename_axis('model-cov').reset_index(name='counts_perfect').sort_values(by = 'model-cov')
df_allreadspermodel_overlap = df_concat_overlap['model-cov'].value_counts().rename_axis('model-cov').reset_index(name='counts_total').sort_values(by = 'model-cov')
df_perc_perfect_overlap['counts_total'] = df_concat_overlap['model-cov'].value_counts().rename_axis('model-cov').reset_index(name='counts_total').sort_values(by = 'model-cov')['counts_total']
df_perc_perfect_overlap['perc_correct'] = df_perc_perfect_overlap.apply(lambda row: row['counts_perfect'] / row['counts_total'] * 100, axis = 1)
print(df_perc_perfect_overlap)

plt.figure(6)
plt.figure(figsize=(8,4))
column_order = ['Cycas Consensus', 'c5', 'c10', 'c15', 'c20', 'c100']
ax = sns.barplot(data = df_perc_perfect_overlap, x = 'model-cov', y ='perc_correct', palette = sns.color_palette("Paired", 6), order = column_order)
for i in ax.containers: ax.bar_label(i,)
plt.tight_layout()
plt.xlabel('Model type')
plt.ylabel('Perfect reads (%)')
labels = [f'Cycas\nConsensus', f'DNN\n3-5X', f'DNN\n6-10X', f'DNN\n11-15X', f'DNN\n16-20X', f'DNN\n3-20X']
plt.xticks(np.arange(0, len(labels)), labels)
plt.savefig('plot6_percperfect_overlap.png', bbox_inches='tight')
plt.close()

# PERCENTAGE PERFECT READS NON-OVERLAP
df_perc_perfect = df_concat_perfect['model-cov'].value_counts().rename_axis('model-cov').reset_index(name='counts_perfect').sort_values(by = 'model-cov')
df_allreadspermodel = df_concat['model-cov'].value_counts().rename_axis('model-cov').reset_index(name='counts_total').sort_values(by = 'model-cov')
df_perc_perfect['counts_total'] = df_concat['model-cov'].value_counts().rename_axis('model-cov').reset_index(name='counts_total').sort_values(by = 'model-cov')['counts_total']
df_perc_perfect['perc_correct'] = df_perc_perfect.apply(lambda row: row['counts_perfect'] / row['counts_total'] * 100, axis = 1)
print(df_perc_perfect)


plt.figure(7)
plt.figure(figsize=(8,4))
column_order = ['Cycas Consensus', 'c5', 'c10', 'c15', 'c20', 'c100']
ax = sns.barplot(data = df_perc_perfect, x = 'model-cov', y ='perc_correct', palette = sns.color_palette("Paired", 6), order = column_order)
for i in ax.containers: ax.bar_label(i,)
plt.tight_layout()
plt.xlabel('Model type')
plt.ylabel('Perfect reads (%)')
labels = [f'Cycas\nConsensus', f'DNN\n3-5X', f'DNN\n6-10X', f'DNN\n11-15X', f'DNN\n16-20X', f'DNN\n3-20X']
plt.xticks(np.arange(0, len(labels)), labels)
plt.savefig('plot7_percperfect_nonoverlap.png', bbox_inches='tight')
plt.close()

# PERCENTAGE PERFECT READS OVERLAP PER COVERAGE
df_perc_perfect_overlap = df_concat_perfect_overlap[['model-cov', 'read-cov']].value_counts().reset_index(name='counts_perfect').sort_values(by = ['model-cov', 'read-cov'])
df_allreadspermodel_overlap = df_concat_overlap[['model-cov', 'read-cov']].value_counts().reset_index(name='counts_total').sort_values(by = ['model-cov', 'read-cov'])
df_perc_perfect_overlap['counts_total'] = df_allreadspermodel_overlap['counts_total']
df_perc_perfect_overlap['perc_correct'] = df_perc_perfect_overlap.apply(lambda row: row['counts_perfect'] / row['counts_total'] * 100, axis = 1)
print(df_perc_perfect_overlap)

# plt.figure(8)
# plt.figure(figsize=(16.7, 8.27))
# hue_order = ['Cycas Consensus', 'c5', 'c10', 'c15', 'c20', 'c100']
# coverage = ['3X','4X','5X','6X','7X','8X','9X','10X','11X','12X','13X', '14X','15X','16X','17X','18X','19X','20X','20+X']
# ax = sns.barplot(data = df_perc_perfect_overlap, x = 'read-cov', y ='perc_correct', hue = 'model-cov', palette = sns.color_palette("Paired", 19), order = coverage, hue_order = hue_order)
# plt.tight_layout()
# plt.xlabel('Model type')
# plt.ylabel('Perfect reads (%)')
# labels = [f'Cycas\nConsensus', f'DNN\n3-5X', f'DNN\n6-10X', f'DNN\n11-15X', f'DNN\n16-20X', f'DNN\n3-20X']
# plt.xticks(np.arange(0, len(coverage)), coverage)
# ax.legend(loc='upper left', bbox_to_anchor=(1,1))
# plt.savefig('plot8_percperfect_percov_nonoverlap.png', bbox_inches='tight')
# plt.close()

# PERCENTAGE PERFECT READS NON-OVERLAP PER COVERAGE
df_perc_perfect = df_concat_perfect[['model-cov', 'read-cov']].value_counts().reset_index(name='counts_perfect').sort_values(by = ['model-cov', 'read-cov'])
df_allreadspermodel = df_concat[['model-cov', 'read-cov']].value_counts().reset_index(name='counts_total').sort_values(by = ['model-cov', 'read-cov'])
df_perc_perfect['counts_total'] = df_allreadspermodel['counts_total']
df_perc_perfect['perc_correct'] = df_perc_perfect.apply(lambda row: row['counts_perfect'] / row['counts_total'] * 100, axis = 1)
print(df_perc_perfect)

# plt.figure(9)
# plt.figure(figsize=(16.7, 8.27))
# coverage = ['3X','4X','5X','6X','7X','8X','9X','10X','11X','12X','13X', '14X','15X','16X','17X','18X','19X','20X','20+X']
# hue_order = ['Cycas Consensus', 'c5', 'c10', 'c15', 'c20', 'c100']
# ax = sns.barplot(data = df_perc_perfect, x = 'read-cov', y ='perc_correct', hue = 'model-cov', palette = sns.color_palette("Paired", 19), order = coverage, hue_order = hue_order)
# plt.tight_layout()
# plt.xlabel('Model type')
# plt.ylabel('Perfect reads (%)')
# labels = [f'Cycas\nConsensus', f'DNN\n3-5X', f'DNN\n6-10X', f'DNN\n11-15X', f'DNN\n16-20X', f'DNN\n3-20X']
# plt.xticks(np.arange(0, len(coverage)), coverage)
# ax.legend(loc='upper left', bbox_to_anchor=(1,1))
# plt.savefig('plot9_percperfect_percov_nonoverlap.png', bbox_inches='tight')
# plt.close()


# NON-PERFECT READS Q-SCORE OVERLAP
df_concat_notperfect_overlap = df_concat_overlap[df_concat_overlap['score'] > 0]
plt.figure(10)
plt.figure(figsize=(8,4))
column_order = ['Cycas Consensus', 'c5', 'c10', 'c15', 'c20', 'c100']
ax = sns.boxplot(data=df_concat_notperfect_overlap, x = 'model-cov', y ='score' , showfliers = False, flierprops={"marker": "x"}, palette = sns.color_palette("Paired", 6), **{'showmeans':False}, order = column_order) #
plt.xlabel('Model type')
plt.ylabel('Error rate')
# plt.ylim(bottom = -0.01)
plt.yscale('log')
ticks = [10**-2.3, 10**-2, 10**-1.5]
labels = ['Q23', 'Q20', 'Q15' ]
plt.yticks(ticks, labels)
labels = [f'Cycas\nConsensus', f'DNN\n3-5X', f'DNN\n6-10X', f'DNN\n11-15X', f'DNN\n16-20X', f'DNN\n3-20X']
plt.xticks(np.arange(0, len(labels)), labels)
plt.savefig('plot10_qscoreperread_nonperfect_overlap.png', bbox_inches='tight')
plt.close()

# NON-PERFECT READS Q-SCORE OVERLAP WITH OUTLIERS
plt.figure(11)
plt.figure(figsize=(8,4))
column_order = ['Cycas Consensus', 'c5', 'c10', 'c15', 'c20', 'c100']
ax = sns.boxplot(data=df_concat_notperfect_overlap, x = 'model-cov', y ='score' , showfliers = True, flierprops={"marker": "x"}, palette = sns.color_palette("Paired", 6), **{'showmeans':False}, order = column_order) #
plt.xlabel('Model type')
plt.ylabel('Error rate')
# plt.ylim(bottom = -0.01)
ticks = [10**-2.3, 10**-2, 10**-1, 10**-0.5]
labels = ['Q23', 'Q20', 'Q10', 'Q5']
plt.yscale('log')
plt.yticks(ticks, labels)
labels = [f'Cycas\nConsensus', f'DNN\n3-5X', f'DNN\n6-10X', f'DNN\n11-15X', f'DNN\n16-20X', f'DNN\n3-20X']
plt.xticks(np.arange(0, len(labels)), labels)
plt.savefig('plot11_qscoreperread_nonperfect_overlap_withoutliers.png', bbox_inches='tight')
plt.close()

# NON-PERFECT READS Q-SCORE NON-OVERLAP
df_concat_notperfect_nonoverlap = df_concat[df_concat['score'] > 0]
plt.figure(12)
plt.figure(figsize=(8,4))
column_order = ['Cycas Consensus', 'c5', 'c10', 'c15', 'c20', 'c100']
ax = sns.boxplot(data=df_concat_notperfect_nonoverlap, x = 'model-cov', y ='score' , showfliers = False, flierprops={"marker": "x"}, palette = sns.color_palette("Paired", 6), **{'showmeans':False}, order = column_order) #
plt.xlabel('Model type')
plt.ylabel('Error rate')
# plt.ylim(bottom = -0.01)
ticks = [10**-2.3, 10**-2, 10**-1.5]
labels = ['Q23', 'Q20', 'Q15']
plt.yscale('log')
plt.yticks(ticks, labels)
labels = [f'Cycas\nConsensus', f'DNN\n3-5X', f'DNN\n6-10X', f'DNN\n11-15X', f'DNN\n16-20X', f'DNN\n3-20X']
plt.xticks(np.arange(0, len(labels)), labels)
plt.savefig('plot12_qscoreperread_nonperfect_nonoverlap.png', bbox_inches='tight')
plt.close()

# NON-PERFECT READS Q-SCORE NON-OVERLAP WITH OUTLIERS
plt.figure(13)
plt.figure(figsize=(8,4))
column_order = ['Cycas Consensus', 'c5', 'c10', 'c15', 'c20', 'c100']
ax = sns.boxplot(data=df_concat_notperfect_nonoverlap, x = 'model-cov', y ='score' , showfliers = True, flierprops={"marker": "x"}, palette = sns.color_palette("Paired", 6), **{'showmeans':False}, order = column_order) #
plt.xlabel('Model type')
plt.ylabel('Error rate')
# plt.ylim(bottom = -0.01)
ticks = [10**-2.3, 10**-2, 10**-1, 10**-0.5]
labels = ['Q23', 'Q20', 'Q10', 'Q5' ]
plt.yscale('log')
plt.yticks(ticks, labels)
labels = [f'Cycas\nConsensus', f'DNN\n3-5X', f'DNN\n6-10X', f'DNN\n11-15X', f'DNN\n16-20X', f'DNN\n3-20X']
plt.xticks(np.arange(0, len(labels)), labels)
plt.savefig('plot13_qscoreperread_nonperfect_nonoverlap_withoutliers.png', bbox_inches='tight')
plt.close()


exit()


# NON-PERFECT READS Q-SCORE OVERLAP PER COVERAGE
df_concat_notperfect_overlap = df_concat_overlap[df_concat_overlap['score'] > 0]
plt.figure(14)
plt.figure(figsize=(16.7, 8.27))
coverage = ['3X','4X','5X','6X','7X','8X','9X','10X','11X','12X','13X', '14X','15X','16X','17X','18X','19X','20X','20+X']
hue_order = ['Cycas Consensus', 'c5', 'c10', 'c15', 'c20', 'c100']
ax = sns.boxplot(data=df_concat_notperfect_overlap, x = 'read-cov', y ='score', hue = 'model-cov' , showfliers = False, flierprops={"marker": "x"}, palette = sns.color_palette("Paired", 6), **{'showmeans':False}, order = coverage, hue_order = hue_order)
plt.xlabel('Model type')
plt.ylabel('Error rate')
ticks = [10**-2.3, 10**-2, 10**-1.5]
labels = ['Q23', 'Q20', 'Q15']
plt.yscale('log')
plt.yticks(ticks, labels)
plt.xticks(np.arange(0, len(coverage)), coverage)
ax.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.savefig('plot14_qscoreperreadpercov_nonperfect_overlap.png', bbox_inches='tight')
plt.close()

# NON-PERFECT READS Q-SCORE OVERLAP WITH OUTLIERS PER COVERAGE
plt.figure(15)
plt.figure(figsize=(16.7, 8.27))
coverage = ['3X','4X','5X','6X','7X','8X','9X','10X','11X','12X','13X', '14X','15X','16X','17X','18X','19X','20X','20+X']
hue_order = ['Cycas Consensus', 'c5', 'c10', 'c15', 'c20', 'c100']
ax = sns.boxplot(data=df_concat_notperfect_overlap, x = 'read-cov', y ='score', hue = 'model-cov' , showfliers = True, flierprops={"marker": "x"}, palette = sns.color_palette("Paired", 6), **{'showmeans':False}, order = coverage, hue_order = hue_order)
plt.xlabel('Model type')
plt.ylabel('Error rate')
ticks = [10**-3, 10**-2, 10**-1, 10**0]
labels = ['Q30', 'Q20', 'Q10', 'Q1' ]
plt.yscale('log')
plt.yticks(ticks, labels)
plt.xticks(np.arange(0, len(coverage)), coverage)
ax.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.savefig('plot15_qscoreperreadpercov_nonperfect_overlap_withoutliers.png', bbox_inches='tight')
plt.close()

# # NON-PERFECT READS Q-SCORE NON-OVERLAP PER COVERAGE
df_concat_notperfect_nonoverlap = df_concat[df_concat['score'] > 0]
plt.figure(16)
plt.figure(figsize=(16.7, 8.27))
coverage = ['3X','4X','5X','6X','7X','8X','9X','10X','11X','12X','13X', '14X','15X','16X','17X','18X','19X','20X','20+X']
hue_order = ['Cycas Consensus', 'c5', 'c10', 'c15', 'c20', 'c100']
ax = sns.boxplot(data=df_concat_notperfect_nonoverlap, x = 'read-cov', y ='score', hue = 'model-cov' , showfliers = False, flierprops={"marker": "x"}, palette = sns.color_palette("Paired", 6), **{'showmeans':False}, order = coverage, hue_order = hue_order)
plt.xlabel('Model type')
plt.ylabel('Error rate')
ticks = [10**-3, 10**-2, 10**-1, 10**0]
labels = ['Q30', 'Q20', 'Q10', 'Q1' ]
plt.yscale('log')
plt.yticks(ticks, labels)
plt.xticks(np.arange(0, len(coverage)), coverage)
ax.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.savefig('plot16_qscoreperreadpercov_nonperfect_nonoverlap.png', bbox_inches='tight')
plt.close()

# # NON-PERFECT READS Q-SCORE NON-OVERLAP WITH OUTLIERS PER COVERAGE
plt.figure(17)
plt.figure(figsize=(16.7, 8.27))
coverage = ['3X','4X','5X','6X','7X','8X','9X','10X','11X','12X','13X', '14X','15X','16X','17X','18X','19X','20X','20+X']
hue_order = ['Cycas Consensus', 'c5', 'c10', 'c15', 'c20', 'c100']
ax = sns.boxplot(data=df_concat_notperfect_nonoverlap, x = 'read-cov', y ='score', hue = 'model-cov' , showfliers = True, flierprops={"marker": "x"}, palette = sns.color_palette("Paired", 6), **{'showmeans':False}, order = coverage, hue_order = hue_order)
plt.xlabel('Model type')
plt.ylabel('Error rate')
ticks = [10**-2, 10**-1, 10**0]
labels = ['Q20', 'Q10', 'Q1' ]
plt.yscale('log')
plt.yticks(ticks, labels)
plt.xticks(np.arange(0, len(coverage)), coverage)
ax.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.savefig('plot17_qscoreperreadpercov_nonperfect_nonoverlap_withoutliers.png', bbox_inches='tight')
plt.close()

# # NON-PERFECT READS Q-SCORE NON-OVERLAP WITH OUTLIERS PER COVERAGE
plt.figure(18)
coverage = ['3X','4X','5X','6X','7X','8X','9X','10X','11X','12X','13X', '14X','15X','16X','17X','18X','19X','20X','20+X']
hue_order = ['Cycas Consensus', 'c5', 'c10', 'c15', 'c20', 'c100']
g = sns.catplot(data=df_concat_notperfect_nonoverlap, x = 'read-cov', y ='score', hue = 'model-cov' ,  palette = sns.color_palette("Paired", 6),  order = coverage, hue_order = hue_order)
g.fig.set_size_inches(16.7, 8.27)
plt.xlabel('Model type')
plt.ylabel('Error rate')
ticks = [10**-2, 10**-1, 10**0]
labels = ['Q20', 'Q10', 'Q1' ]
plt.yscale('log')
plt.yticks(ticks, labels)
plt.xticks(np.arange(0, len(coverage)), coverage)
# ax.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.savefig('plot18_qscoreperreadpercov_nonperfect_nonoverlap_withoutliers.png', bbox_inches='tight')
plt.close()

# ACCUMULATIVE HISTOGRAM FOR READ QUALITY OVERLAP ONLY ALL READS 
fig = plt.figure(19)
plt.figure(figsize=(8,4))
labels = [f'Cycas Consensus', f'DNN 3-5X', f'DNN 6-10X', f'DNN 11-15X', f'DNN 16-20X', f'DNN 3-20X']
hue_order = ['Cycas Consensus', 'c5', 'c10', 'c15', 'c20', 'c100']
ax = sns.ecdfplot(data=df_concat_overlap, x = 'q_score', hue = 'model-cov', hue_order = hue_order, complementary = True, palette = sns.color_palette("Paired", 6))
ax.legend(loc='upper left', bbox_to_anchor=(1,1), labels = labels)
ticks = [10**-5, 10**-4, 10**-3, 10**-2, 10**-1, 10**0]
labels = ['Q50', 'Q40', 'Q30', 'Q20', 'Q10', 'Q1' ]
plt.xscale('log')
plt.xticks(ticks, labels)
plt.savefig('plot19_accum_hist_allreads_overlap.png', bbox_inches='tight')
plt.close()

# ACCUMULATIVE HISTOGRAM FOR READ QUALITY NON-OVERLAP ALL READS 
fig = plt.figure(20)
plt.figure(figsize=(8,4))
labels = [f'Cycas Consensus', f'DNN 3-5X', f'DNN 6-10X', f'DNN 11-15X', f'DNN 16-20X', f'DNN 3-20X']
hue_order = ['Cycas Consensus', 'c5', 'c10', 'c15', 'c20', 'c100']
ax = sns.ecdfplot(data=df_concat, x = 'q_score', hue = 'model-cov', hue_order = hue_order, complementary = True, palette = sns.color_palette("Paired", 6), stat='count')
ax.legend(loc='upper left', bbox_to_anchor=(1,1), labels = labels)
ticks = [10**-5, 10**-4, 10**-3, 10**-2, 10**-1, 10**0]
labels = ['Q50', 'Q40', 'Q30', 'Q20', 'Q10', 'Q1' ]
plt.xscale('log')
plt.xticks(ticks, labels)
plt.savefig('plot20_accum_hist_allreads_nonoverlap.png', bbox_inches='tight')
plt.close()

# KDE PLOT OVERLAP ALL READS
fig = plt.figure(21)
plt.figure(figsize=(8,4))
labels = [f'Cycas Consensus', f'DNN 3-5X', f'DNN 6-10X', f'DNN 11-15X', f'DNN 16-20X', f'DNN 3-20X', f'CNN 3-5X', f'CNN 6-10X', f'CNN 11-15X', f'CNN 16-20X', f'CNN 3-20X']
hue_order = ['Cycas Consensus', 'c5', 'c10', 'c15', 'c20', 'c100']
ax = sns.kdeplot(data=df_concat_overlap, x = 'q_score', hue = 'model-cov', hue_order = hue_order, fill = None,  palette = sns.color_palette("Paired", 6) , alpha=1, legend = True, bw_adjust=5, cut = 3)
# ax = sns.displot(data=df_concat_overlap, x = 'score-NM', hue = 'model-cov', hue_order = hue_order, kde=True)
# ax.legend(loc='upper left', bbox_to_anchor=(1,1), labels = labels, title = 'models')
ticks = [10**-5, 10**-4, 10**-3, 10**-2, 10**-1, 10**0]
labels = ['Q50', 'Q40', 'Q30', 'Q20', 'Q10', 'Q1' ]
plt.xscale('log')
plt.xticks(ticks, labels)
plt.savefig('plot21_kde_allreads_overlap.png', bbox_inches='tight')
plt.close()