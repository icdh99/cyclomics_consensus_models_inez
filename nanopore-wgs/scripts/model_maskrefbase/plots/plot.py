import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# PLOT 3 - ACCURACY SCORES MODELS AND MAJORITY VOTE
# cnn_c5_acc = np.array([1,1,1,1,1,1,1,1,1,1])
# cnn_c10_acc = np.array([1,1,1,1,1,1,1,1,1,1])
# cnn_c15_acc = np.array([1,1,1,1,1,1,1,1,1,1])
# cnn_c20_acc = np.array([1,1,1,1,1,1,1,1,1,1])
# cnn_all_acc = np.array([1,1,1,1,1,1,1,1,1,1])
# dnn_c5_acc = np.array([0.9999666810035706, 0.9999666810035706, 0.9999533295631409, 0.9999799728393555, 0.999946653842926, 0.9999666810035706, 0.9999666810035706, 0.9999666810035706, 0.9999600052833557, 0.9999666810035706])
# dnn_c10_acc = np.array([0.9999666810035706, 0.9999666810035706, 0.9999533295631409, 0.9999799728393555, 0.999946653842926, 0.9999666810035706, 0.9999666810035706, 0.9999666810035706, 0.9999600052833557, 0.9999666810035706])
# dnn_c15_acc = np.array([0.9999266862869263, 0.9999399781227112, 0.9999333024024963, 0.999946653842926, 0.9999600052833557, 0.999946653842926, 0.9999399781227112, 0.999946653842926, 0.9999266862869263, 0.9999333024024963])
# dnn_c20_acc = np.array([0.9999333024024963, 0.9999666810035706, 0.9999533295631409, 0.999946653842926, 0.9999733567237854, 0.9999600052833557, 0.9999600052833557, 0.9999666810035706, 0.9999200105667114, 0.9999533295631409])
# dnn_all_acc = np.array([0.9999600052833557, 0.9999600052833557, 0.9999600052833557, 0.9999200105667114, 0.9999600052833557, 0.9999666810035706, 0.9999666810035706, 0.9999600052833557, 0.9999333024024963, 0.9999600052833557])
# maj_c5 = 1 - 0.5328/100
# maj_c10 = 1 - 0.2048/100
# maj_c15 = 1 - 0.1265/100
# maj_c20 = 1 - 0.1065/100
# maj_all = 1 - 0.2228/100

# names = ['CNN 3-5X', 'CNN 6-10X', 'CNN 11-15X', 'CNN 16-20X', 'CNN 3-20X', 'DNN 3-5X', 'DNN 6-10X', 'DNN 11-15X', 'DNN 16-20X', 'DNN 3-20X', 'Majority vote 3-5X', 'Majority vote 6-10X', 'Majority vote 11-15X', 'Majority vote 16-20X', 'Majority vote 3-20X']
# columns = [cnn_c5_acc, cnn_c10_acc, cnn_c15_acc, cnn_c20_acc, cnn_all_acc, dnn_c5_acc, dnn_c10_acc, dnn_c15_acc, dnn_c20_acc, dnn_all_acc, maj_c5, maj_c10, maj_c15, maj_c20, maj_all]
# x_pos = np.arange(1,len(columns)+1)

# plt.figure(3)
# fig, ax = plt.subplots()
# plt.style.use('seaborn')
# ax.boxplot(columns, patch_artist=False)
# # plt.ylim(0.9, 1)
# ax.set_ylabel('Accuracy')
# ax.set_title('Models and Majority Vote Nanopore WGS data - Accuracy')
# ax.yaxis.grid(True)

# ax.set_yscale('log')
# # plt.yscale("log")

# plt.xticks(x_pos, names, rotation = 90)
# ax.tick_params(axis = "x", direction="in")
# plt.tight_layout
# plt.savefig('Models_Acc_Maj_log.png', bbox_inches="tight", dpi=500)


# plt.figure(4)
# fig, ax = plt.subplots()
# plt.style.use('seaborn')
# ax.boxplot(columns, patch_artist=False)
# # plt.ylim(0.9, 1)
# ax.set_ylabel('Accuracy')
# ax.set_title('Models and Majority Vote Nanopore WGS data - Accuracy')
# ax.yaxis.grid(True)

# ax.set_yscale('linear')
# # plt.yscale("log")

# plt.xticks(x_pos, names, rotation = 90)
# ax.tick_params(axis = "x", direction="in")
# plt.tight_layout
# plt.savefig('Models_Acc_Maj_linear.png', bbox_inches="tight", dpi=500)





# # PLOT 5 - COMPARE ACCURACY DNN WITH REF BASE AND WITH MASKED REF BASE (WITH TUNING)

# dnn_old_c5_acc = np.array([0.9999749660491943, 0.9999749660491943, 0.9999299645423889, 0.9999749660491943, 0.999970018863678, 0.9999549984931946, 0.99993497133255, 0.9999549984931946, 0.9999650120735168, 0.9999499917030334])
# dnn_old_c10_acc = np.array([0.9999650120735168, 0.999970018863678, 0.9999749660491943, 0.9999749660491943, 0.9999749660491943, 0.9999549984931946, 0.9999799728393555, 0.9999749660491943, 0.9999749660491943, 0.9999849796295166])
# dnn_old_c15_acc = np.array([0.9999799728393555, 0.9999749660491943, 0.999970018863678, 0.9999749660491943, 0.9999849796295166, 0.999970018863678, 0.999970018863678, 0.9999549984931946, 0.9999799728393555, 0.9999549984931946])
# dnn_old_c20_acc = np.array([0.9999600052833557, 0.999970018863678, 0.9999499917030334, 0.9999899864196777, 0.999970018863678, 0.999970018863678, 0.9999749660491943, 0.9999650120735168, 0.999970018863678, 0.999970018863678])
# dnn_old_all_acc = np.array([0.9999549984931946, 0.9999650120735168, 0.9999499917030334, 0.9999499917030334, 0.9999499917030334, 0.9999449849128723, 0.9999600052833557, 0.9999549984931946, 0.9999449849128723, 0.9999650120735168])
# dnn_c5_acc = np.array([0.9999666810035706, 0.9999666810035706, 0.9999533295631409, 0.9999799728393555, 0.999946653842926, 0.9999666810035706, 0.9999666810035706, 0.9999666810035706, 0.9999600052833557, 0.9999666810035706])
# dnn_c10_acc = np.array([0.9999666810035706, 0.9999666810035706, 0.9999533295631409, 0.9999799728393555, 0.999946653842926, 0.9999666810035706, 0.9999666810035706, 0.9999666810035706, 0.9999600052833557, 0.9999666810035706])
# dnn_c15_acc = np.array([0.9999266862869263, 0.9999399781227112, 0.9999333024024963, 0.999946653842926, 0.9999600052833557, 0.999946653842926, 0.9999399781227112, 0.999946653842926, 0.9999266862869263, 0.9999333024024963])
# dnn_c20_acc = np.array([0.9999333024024963, 0.9999666810035706, 0.9999533295631409, 0.999946653842926, 0.9999733567237854, 0.9999600052833557, 0.9999600052833557, 0.9999666810035706, 0.9999200105667114, 0.9999533295631409])
# dnn_all_acc = np.array([0.9999600052833557, 0.9999600052833557, 0.9999600052833557, 0.9999200105667114, 0.9999600052833557, 0.9999666810035706, 0.9999666810035706, 0.9999600052833557, 0.9999333024024963, 0.9999600052833557])


# names = ['DNN old 3-5X', 'DNN old 6-10X', 'DNN old 11-15X', 'DNN old 16-20X', 'DNN old 3-20X', 'DNN 3-5X', 'DNN 6-10X', 'DNN 11-15X', 'DNN 16-20X', 'DNN 3-20X']
# columns = [dnn_old_c5_acc, dnn_old_c10_acc, dnn_old_c15_acc, dnn_old_c20_acc, dnn_old_all_acc, dnn_c5_acc, dnn_c10_acc, dnn_c15_acc, dnn_c20_acc, dnn_all_acc]
# x_pos = np.arange(1,len(columns)+1)

# plt.figure(5)
# fig, ax = plt.subplots()
# plt.style.use('seaborn')
# ax.boxplot(columns, patch_artist=False)
# plt.ylim(0.99988, 1)
# ax.set_ylabel('Accuracy')
# ax.set_title('Models Nanopore WGS data - Accuracy')
# ax.yaxis.grid(True)

# # ax.set_yscale('linear')
# # plt.yscale("log")

# plt.xticks(x_pos, names, rotation = 90)
# ax.tick_params(axis = "x", direction="in")
# plt.tight_layout
# plt.savefig('Models_Acc_compare_maskedrefbase_DNN.png', bbox_inches="tight", dpi=500)





'''
plot dnn cnn majority vote masked ref base box plot with F1 scores
'''

# plt.figure(6)
# fig, ax = plt.subplots()
# df = pd.read_csv('/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/model_maskrefbase/plots/values_crossval_dnn_cnn_mv.csv')
# print(df)
# sns.color_palette("Set2")
# # def dolog(x): return -1 * (np.log10(x))
# # df['value'] = df['value'].map(dolog)

# def minus(x): return 1-x
# df['value'] = df['value'].map(minus)
# print(df)
# ax.set_yscale('log')
# plt.gca().invert_yaxis()
# # plt.ylim(0.9996, 1)
# sns.boxplot(x='coverage', hue='type', y='value', data=df, palette="Set2", order = ['3-5X', '6-10X', '11-15X', '16-20X', '3-20X'])
# ax.set(ylabel='1 - F1 score')
# plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
# plt.savefig('t2t_crossval_-log10_yinv.png', bbox_inches="tight")

# plt.figure(7)
# fig, ax = plt.subplots()
# df = pd.read_csv('/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/model_maskrefbase/plots/values_crossval_dnn_cnn_mv.csv')
# sns.color_palette("Set2")
# # plt.ylim(0.9996, 1)
# sns.boxplot(x='coverage', hue='type', y='value', data=df, palette="Set2", order = ['3-5X', '6-10X', '11-15X', '16-20X', '3-20X'])
# ax.set(ylabel='F1 score')
# plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
# plt.savefig('t2t_crossval_normal.png', bbox_inches="tight")



'''
plot dnn cnn majority vote masked ref base box plot with F1 scores
also f1 score per class for the majority vote
'''

# plt.figure(8)
# fig, ax = plt.subplots()
df = pd.read_csv('/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/model_maskrefbase/plots/values_crossval_dnn_cnn_mv_withf1perclass.csv')
print(df)
print(df[(df["type"] == "DNN") & ( df["coverage"] == "3-5X" )]['value'].median())
print(df[(df["type"] == "CNN") & ( df["coverage"] == "3-5X" )]['value'].median())
print(df[(df["type"] == "DNN") & ( df["coverage"] == "6-10X" )]['value'].median())
print(df[(df["type"] == "CNN") & ( df["coverage"] == "6-10X" )]['value'].median())

# sns.color_palette("Set2")
# # def dolog(x): return -1 * (np.log10(x))
# # df['value'] = df['value'].map(dolog)

# def minus(x): return 1-x
# df['value'] = df['value'].map(minus)
# ax.set_yscale('log')
# plt.gca().invert_yaxis()
# # plt.ylim(0.9996, 1)
# sns.boxplot(data=df, x='coverage', hue='type', y='value', palette="Set2", order = ['3-5X', '6-10X', '11-15X', '16-20X', '3-20X'])
# ax.set(ylabel='1 - F1 score')
# plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
# plt.savefig('fig1_boxplotF1_scores_allboxplot', bbox_inches="tight")
# plt.close()

# print(df)
# print(df['type'].value_counts())

# df['Data4'] = df['Data3'].groupby(df['Date']).transform('sum')

df_maj_bases = df[(df['type'] == 'majority_vote_A') | (df['type'] == 'majority_vote_C') | (df['type'] == 'majority_vote_G') | (df['type'] == 'majority_vote_T') ]
# print(df_maj_bases)

df_maj_bases['majority_vote_bases'] = df_maj_bases['value'].groupby(df_maj_bases['coverage']).transform('mean')
print(df_maj_bases)

# plt.figure(9)
# fig, ax = plt.subplots()
# sns.color_palette("Set2")
# ax.set_yscale('log')
# plt.gca().invert_yaxis()
# sns.boxplot(data = df[(df['type'] == 'DNN') | (df['type'] == 'CNN')],  x='coverage', hue='type', y='value', palette="Set2", order = ['3-5X', '6-10X', '11-15X', '16-20X', '3-20X'])
# ax.set(ylabel='1 - F1 score')
# plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
# plt.savefig('fig2_boxplot_onlydnncnn.png', bbox_inches="tight")
# plt.close()

# plt.figure(9)
# fig, ax = plt.subplots()
# sns.color_palette("Set2")
# ax.set_yscale('log')
# plt.gca().invert_yaxis()
# sns.scatterplot(data = df[(df['type'] == 'majority_vote_A') | (df['type'] == 'majority_vote_C') | (df['type'] == 'majority_vote_G') | (df['type'] == 'majority_vote_T') | (df['type'] == 'majority_vote_del')  | (df['type'] == 'majority_vote')],  x='coverage', hue='type', y='value', palette="Set2")
# ax.set(ylabel='1 - F1 score')
# plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
# plt.savefig('fig2_boxplot_onlymajvote.png', bbox_inches="tight")
# plt.close()

# plt.figure(10)
# fig, ax = plt.subplots()
# sns.color_palette("Set2")
# ax.set_yscale('log')
# plt.gca().invert_yaxis()
# ax = sns.boxplot(data = df[(df['type'] == 'DNN') | (df['type'] == 'CNN')],  x='coverage', hue='type', y='value', palette="Set2", order = ['3-5X', '6-10X', '11-15X', '16-20X', '3-20X'])
# ax = sns.scatterplot(data = df_maj_bases[df_maj_bases['type'] == 'majority_vote_A'],  x='coverage', y='value',  label = 'Majority vote mismatch only', color = 'black')
# ax = sns.scatterplot(data = df[df['type'] == 'majority_vote_del'],  x='coverage', y='value',  label = 'Majority vote deletion only', color = 'black', marker = 's')
# ax = sns.scatterplot(data = df[df['type'] == 'majority_vote'],  x='coverage', y='value',  label = 'Majority vote', color = 'black', marker = 'X')
# ax.set(ylabel='1 - F1 score', xlabel = 'Coverage of model')
# plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
# plt.savefig('fig3_combine_box_scatter.png', bbox_inches="tight", dpi = 200)
# plt.close()


