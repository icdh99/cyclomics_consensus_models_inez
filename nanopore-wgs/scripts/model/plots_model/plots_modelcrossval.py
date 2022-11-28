import matplotlib.pyplot as plt
import numpy as np

# PLOT 1 - F1 scores model crossvalidation

list_modelnames = ['cnn_20', 'cnn_15', 'cnn_10', 'cnn_5', 'dnn_20', 'dnn_15', 'dnn_10', 'dnn_5']

cnn_c5_F1 = np.array([0.9994968231910804, 0.9999248202048159, 0.9998395821267567, 0.9999102064972216, 0.9998892295830746, 0.9999139900703925, 0.9998253151451947, 0.9998304121614565, 0.9997030187989656, 0.9996923375854874])
cnn_c10_F1 = np.array([0.9997099877655324, 0.9997478885649432, 0.9997435680863646, 0.9997752976326376, 0.9997781789414828, 0.9997245881050169, 0.9996543730268375, 0.9997271290228285, 0.9996426666437495, 0.9997591479375136])
cnn_c15_F1 = np.array([0.9999026779645583, 0.9999129594712973, 0.9999283876737903, 0.9999191232367515, 0.9999115741185886, 0.9999327092039636, 0.9999383121743698, 0.9998911102957265, 0.999933221162316, 0.9998981967328187])
cnn_c20_F1 = np.array([0.9998815123864528, 0.9999541169379779, 0.9999479261593754, 0.9999341091769137, 0.9999240152170242, 0.9999276810882646, 0.9999442923796534, 0.9999383083544126, 0.9999541172789465, 0.9999286567220967])
cnn_all_F1 = np.array([0.9994778681398386, 0.9993616087883403, 0.9989307295742667, 0.9986637718723553, 0.9993368087693967, 0.9993617813539402, 0.9993502996269586, 0.9993397219887232, 0.9992415480108756, 0.9992242351242926])
dnn_c5_F1 = np.array([0.9999746105861034, 0.9999743220076929, 0.9999292487697798, 0.9999743371312699, 0.9999695267440668, 0.9999540462174246, 0.9999337698902655, 0.9999543202092449, 0.999964458037272, 0.9999495397087572])
dnn_c10_F1 = np.array([0.9999645268775907, 0.9999695808228077, 0.9999746344655196, 0.9999746344655196, 0.9999746344655196, 0.9999544191551779, 0.9999797366733414, 0.9999746344655196, 0.9999746344655196, 0.9999847904168828])
dnn_c15_F1 = np.array([0.9999797168276421, 0.9999743736610451, 0.9999693027486898, 0.9999743736610451, 0.9999842417102667, 0.9999695765213208, 0.9999698487242195, 0.9999540898120816, 0.9999794445401493, 0.9999540898120816])
dnn_c20_F1 = np.array([0.9999602229537639, 0.9999695513071472, 0.999949536250284, 0.9999898506354994, 0.9999698357784716, 0.9999703724689062, 0.9999746261725466, 0.9999652978770561, 0.9999698357784716, 0.9999698357784716])
dnn_all_F1 = np.array([0.9999540823667253, 0.9999644754411804, 0.9999490070365733, 0.9999484186377767, 0.999949005124953, 0.999944176967478, 0.9999588588266097, 0.99995378686895, 0.9999436371804881, 0.9999639362780793])

names = ['CNN c5', 'CNN c10', 'CNN c15', 'CNN c20', 'CNN all', 'DNN c5', 'DNN c10', 'DNN c15', 'DNN c20', 'DNN all']
columns = [cnn_c5_F1, cnn_c10_F1, cnn_c15_F1, cnn_c20_F1, cnn_all_F1, dnn_c5_F1, dnn_c10_F1, dnn_c15_F1, dnn_c20_F1, dnn_all_F1]
x_pos = np.arange(1,len(columns)+1)

plt.figure(1)
fig, ax = plt.subplots()
plt.style.use('seaborn')
# plt.ylim(0.999, 1)
ax.boxplot(columns, patch_artist=False)
# ax.bar(x_pos, values, yerr=errors, align='center', alpha=0.5, ecolor='black', capsize=5)
ax.set_ylabel('F1 score')
# ax.set_xticks(x_pos)
# ax.set_xticklabels(names)
ax.set_title('10-fold Cross-Validation Models Nanopore WGS data - F1 score')
ax.yaxis.grid(True)
plt.xticks(x_pos, names, rotation = 25)
plt.tight_layout
plt.savefig('Models_crossval_F1scores.png', bbox_inches="tight")

# PLOT 2 - DNN F1 SCORES
names = ['CNN c15', 'CNN c20', 'DNN c5', 'DNN c10', 'DNN c15', 'DNN c20', 'DNN all']
columns = [cnn_c15_F1, cnn_c20_F1, dnn_c5_F1, dnn_c10_F1, dnn_c15_F1, dnn_c20_F1, dnn_all_F1]
x_pos = np.arange(1,len(columns)+1)

plt.figure(2)
fig, ax = plt.subplots()
plt.style.use('seaborn')
# plt.ylim(0.999, 1)
ax.boxplot(columns, patch_artist=False)
# ax.bar(x_pos, values, yerr=errors, align='center', alpha=0.5, ecolor='black', capsize=5)
ax.set_ylabel('F1 score')
# ax.set_xticks(x_pos)
# ax.set_xticklabels(names)
ax.set_title('10-fold Cross-Validation Dense Models Nanopore WGS data - F1 score')
ax.yaxis.grid(True)
plt.xticks(x_pos, names, rotation = 25)
plt.tight_layout
plt.savefig('Models_crossval_F1scores_DNN.png', bbox_inches="tight")

# PLOT 3 - ACCURACY SCORES MODELS AND MAJORITY VOTE
cnn_c5_acc = np.array([0.9994999766349792, 0.9999250173568726, 0.9998399615287781, 0.9999099969863892, 0.9998899698257446, 0.9999150037765503, 0.9998250007629395, 0.9998300075531006, 0.999709963798523, 0.9996949434280396])
cnn_c10_acc = np.array([0.9997149705886841, 0.9997549653053284, 0.9997449517250061, 0.999779999256134, 0.999779999256134, 0.9997299909591675, 0.9996599555015564, 0.9997299909591675, 0.999644935131073, 0.9997649788856506])
cnn_c15_acc = np.array([0.999904990196228, 0.9999150037765503, 0.9999299645423889, 0.9999200105667114, 0.9999150037765503, 0.99993497133255, 0.9999399781227112, 0.9998899698257446, 0.99993497133255, 0.9998999834060669])
cnn_c20_acc = np.array([0.9998849630355835, 0.9999549984931946, 0.9999499917030334, 0.99993497133255, 0.9999250173568726, 0.9999299645423889, 0.9999449849128723, 0.9999399781227112, 0.9999549984931946, 0.9999299645423889])
cnn_all_acc = np.array([0.9994799494743347, 0.9993699193000793, 0.9990049004554749, 0.9986998438835144, 0.9993399381637573, 0.9993649125099182, 0.9993549585342407, 0.9993399381637573, 0.9992449283599854, 0.9992349147796631])
dnn_c5_acc = np.array([0.9999749660491943, 0.9999749660491943, 0.9999299645423889, 0.9999749660491943, 0.999970018863678, 0.9999549984931946, 0.99993497133255, 0.9999549984931946, 0.9999650120735168, 0.9999499917030334])
dnn_c10_acc = np.array([0.9999650120735168, 0.999970018863678, 0.9999749660491943, 0.9999749660491943, 0.9999749660491943, 0.9999549984931946, 0.9999799728393555, 0.9999749660491943, 0.9999749660491943, 0.9999849796295166])
dnn_c15_acc = np.array([0.9999799728393555, 0.9999749660491943, 0.999970018863678, 0.9999749660491943, 0.9999849796295166, 0.999970018863678, 0.999970018863678, 0.9999549984931946, 0.9999799728393555, 0.9999549984931946])
dnn_c20_acc = np.array([0.9999600052833557, 0.999970018863678, 0.9999499917030334, 0.9999899864196777, 0.999970018863678, 0.999970018863678, 0.9999749660491943, 0.9999650120735168, 0.999970018863678, 0.999970018863678])
dnn_all_acc = np.array([0.9999549984931946, 0.9999650120735168, 0.9999499917030334, 0.9999499917030334, 0.9999499917030334, 0.9999449849128723, 0.9999600052833557, 0.9999549984931946, 0.9999449849128723, 0.9999650120735168])
maj_c5 = 1 - 0.5328/100
maj_c10 = 1 - 0.2048/100
maj_c15 = 1 - 0.1265/100
maj_c20 = 1 - 0.1065/100
maj_all = 1 - 0.2228/100

names = ['CNN 3-5X', 'CNN 6-10X', 'CNN 11-15X', 'CNN 16-20X', 'CNN 3-20X', 'DNN 3-5X', 'DNN 6-10X', 'DNN 11-15X', 'DNN 16-20X', 'DNN 3-20X', 'Majority vote 3-5X', 'Majority vote 6-10X', 'Majority vote 11-15X', 'Majority vote 16-20X', 'Majority vote 3-20X']
columns = [cnn_c5_acc, cnn_c10_acc, cnn_c15_acc, cnn_c20_acc, cnn_all_acc, dnn_c5_acc, dnn_c10_acc, dnn_c15_acc, dnn_c20_acc, dnn_all_acc, maj_c5, maj_c10, maj_c15, maj_c20, maj_all]
x_pos = np.arange(1,len(columns)+1)

plt.figure(3)
fig, ax = plt.subplots()
plt.style.use('seaborn')
ax.boxplot(columns, patch_artist=False)
# plt.ylim(0.9, 1)
# ax.bar(x_pos, values, yerr=errors, align='center', alpha=0.5, ecolor='black', capsize=5)
ax.set_ylabel('Accuracy')
# ax.set_xticks(x_pos)
# ax.set_xticklabels(names)
ax.set_title('Models and Majority Vote Nanopore WGS data - Accuracy')
ax.yaxis.grid(True)
plt.yscale("log")
plt.xticks(x_pos, names, rotation = 90)
ax.tick_params(axis = "x", direction="in")
plt.tight_layout
plt.savefig('Models_Acc_Maj_highres.png', bbox_inches="tight", dpi=500)

exit()



# FIGURE WITH MAJORITY VOTE - ACCURACY
names = ['CNN c5', 'CNN c10', 'CNN c15', 'CNN c20', 'DNN c5', 'DNN c10', 'DNN c15', 'DNN c20', 'maj c5', 'maj c10', 'maj c15', 'maj c20']
x_pos = np.arange(len(names))
values = [cnn_c5_mean, cnn_c10_mean, cnn_c15_mean, cnn_c20_mean, dnn_c5_mean, dnn_c10_mean, dnn_c15_mean, dnn_c20_mean, maj_c5_acc, maj_c10_acc, maj_c15_acc, maj_c20_acc]
errors = [cnn_c5_std, cnn_c10_std, cnn_c15_std, cnn_c20_std, dnn_c5_std, dnn_c10_std, dnn_c15_std, dnn_c20_std, 0, 0, 0, 0]

fig, ax = plt.subplots()
plt.ylim(0.992, 1.00025)
ax.bar(x_pos, values, yerr=errors, align='center', alpha=0.5, ecolor='black', capsize=5)
# ax.bar(x_pos, values)
ax.set_ylabel('Accuracy')
ax.set_xticks(x_pos)
ax.set_xticklabels(names)
ax.set_title('Crossvalidated models Nanopore WGS data - Accuracy')
ax.yaxis.grid(True)
plt.xticks(rotation = 90)
plt.tight_layout
plt.savefig('Models_crossval_accuracy_withmajvote.png', bbox_inches="tight")

# FIGURE WITHOUT MAJORITY VOTE - ACCURACY
names = ['CNN c5', 'CNN c10', 'CNN c15', 'CNN c20', 'DNN c5', 'DNN c10', 'DNN c15', 'DNN c20']
x_pos = np.arange(len(names))
values = [cnn_c5_mean, cnn_c10_mean, cnn_c15_mean, cnn_c20_mean, dnn_c5_mean, dnn_c10_mean, dnn_c15_mean, dnn_c20_mean]
errors = [cnn_c5_std, cnn_c10_std, cnn_c15_std, cnn_c20_std, dnn_c5_std, dnn_c10_std, dnn_c15_std, dnn_c20_std]

fig, ax = plt.subplots()
plt.ylim(0.999, 1.00025)
ax.bar(x_pos, values, yerr=errors, align='center', alpha=0.5, ecolor='black', capsize=5)
# ax.bar(x_pos, values)
ax.set_ylabel('Accuracy')
ax.set_xticks(x_pos)
ax.set_xticklabels(names)
ax.set_title('Crossvalidated models Nanopore WGS data - Accuracy')
ax.yaxis.grid(True)
plt.xticks(rotation = 90)
plt.tight_layout
plt.savefig('Models_crossval_accuracy.png', bbox_inches="tight")




# FIGURES WITH F1 scores
# zelfde naam voor variabelen dus laat hieronder staand

cnn_c5_F1 = np.array([0.9998979444004875, 0.9998131561451155, 0.9999059341532379, 0.9998790174286255, 0.9999085838726343, 0.999936537601251, 0.9999341380771576, 0.998513542207611, 0.9995723729792072, 0.9998937261702426])
cnn_c5_mean = np.mean(cnn_c5_F1)
cnn_c5_std = np.std(cnn_c5_F1)

cnn_c10_F1 = np.array([0.9996451721781483, 0.9990792967905157, 0.9995561373270132, 0.9996378757441388, 0.9994928477280203, 0.9995481836361136, 0.9995848126300358, 0.999644079833492, 0.999485091582541, 0.9995217345216811])
cnn_c10_mean = np.mean(cnn_c10_F1)
cnn_c10_std = np.std(cnn_c10_F1)

cnn_c15_F1 = np.array([0.9997840690484766, 0.9998925515896278, 0.9999212028015445, 0.9998677156321495, 0.9997230607018842, 0.9998246388317545, 0.9999065360859121, 0.9998523824090565, 0.9999051618937833, 0.9998794459660586])
cnn_c15_mean = np.mean(cnn_c15_F1)
cnn_c15_std = np.std(cnn_c15_F1)

cnn_c20_F1 = np.array([0.9998929917992954, 0.9999308274874389, 0.9999052637330219, 0.9998141575357645, 0.9998657948770507, 0.9998919060556942, 0.9998786770639887, 0.9998956956654651, 0.9998802959519573, 0.9996971849102728])
cnn_c20_mean = np.mean(cnn_c20_F1)
cnn_c20_std = np.std(cnn_c20_F1)

dnn_c5_F1 = np.array([0.9999864137311448, 0.999961718349581, 0.999960747515026, 0.9999341102800073, 0.9999597767972302, 0.9999740658389662, 0.9999607474147321, 0.9999864137311448, 0.999960747515026, 0.9998551683897412])
dnn_c5_mean = np.mean(dnn_c5_F1)
dnn_c5_std = np.std(dnn_c5_F1)

dnn_c10_F1 = np.array([0.9999743302855882, 0.99994641276224, 0.9999330154965762, 0.9999196180483021, 0.9999866034641731, 0.9999475372137985, 0.9999330154965762, 0.9999598098453537, 0.9999598098453537, 0.9999732067459779])
dnn_c10_mean = np.mean(dnn_c10_F1)
dnn_c10_std = np.std(dnn_c10_F1)

dnn_c15_F1 = np.array([0.9999727874193831, 0.9999733622790787, 0.9999727874193831, 0.9999727880370926, 0.9999866813973535, 0.9999866812254972, 0.9999861061938728, 0.9999733622790787, 0.9999581517667737, 0.9999866812254972])
dnn_c15_mean = np.mean(dnn_c15_F1)
dnn_c15_std = np.std(dnn_c15_F1)

dnn_c20_F1 = np.array([0.9999733248616132, 0.9999733248616132, 0.9999466497232261, 0.9999733252181557, 0.9999733248616132, 0.9999733252181557, 0.9999733248616132, 0.9999733252181557, 0.9999733248616132, 0.9999610348760749])
dnn_c20_mean = np.mean(dnn_c20_F1)
dnn_c20_std = np.std(dnn_c20_F1)

names = ['CNN c5', 'CNN c10', 'CNN c15', 'CNN c20', 'DNN c5', 'DNN c10', 'DNN c15', 'DNN c20']
x_pos = np.arange(len(names))
values = [cnn_c5_mean, cnn_c10_mean, cnn_c15_mean, cnn_c20_mean, dnn_c5_mean, dnn_c10_mean, dnn_c15_mean, dnn_c20_mean]
errors = [cnn_c5_std, cnn_c10_std, cnn_c15_std, cnn_c20_std, dnn_c5_std, dnn_c10_std, dnn_c15_std, dnn_c20_std]

fig, ax = plt.subplots()
plt.ylim(0.999, 1.00025)
ax.bar(x_pos, values, yerr=errors, align='center', alpha=0.5, ecolor='black', capsize=5)
# ax.bar(x_pos, values)
ax.set_ylabel('F1 score')
ax.set_xticks(x_pos)
ax.set_xticklabels(names)
ax.set_title('Crossvalidated models Nanopore WGS data - F1 score')
ax.yaxis.grid(True)
plt.xticks(rotation = 90)
plt.tight_layout
plt.savefig('Models_crossval_F1.png', bbox_inches="tight")
