import matplotlib.pyplot as plt
import numpy as np

list_F1_scores = [0.999865279507995, 0.9998556764960249, 0.99951952319717, 0.999725495303557, 0.9999694284561833, 0.999976938924301, 0.9999533359203939, 0.99995399095626]
list_modelnames = ['cnn_20', 'cnn_15', 'cnn_10', 'cnn_5', 'dnn_20', 'dnn_15', 'dnn_10', 'dnn_5']


cnn_c5_acc = np.array([0.999893307685852, 0.9998133182525635, 0.9999066591262817, 0.9998799562454224, 0.9999066591262817, 0.9999333024024963, 0.9999333024024963, 0.9985464811325073, 0.9995599389076233, 0.999893307685852])
cnn_c5_mean = np.mean(cnn_c5_acc)
cnn_c5_std = np.std(cnn_c5_acc)

cnn_c10_acc = np.array([0.9996399283409119, 0.9990798830986023, 0.9995465874671936, 0.9996399283409119, 0.9994933009147644, 0.9995465874671936, 0.9995866417884827, 0.9996399283409119, 0.9994799494743347, 0.999519944190979])
cnn_c10_mean = np.mean(cnn_c10_acc)
cnn_c10_std = np.std(cnn_c10_acc)

cnn_c15_acc = np.array([0.9997866153717041, 0.999893307685852, 0.9999200105667114, 0.9998666644096375, 0.9997333288192749, 0.9998266696929932, 0.9999066591262817, 0.9998533129692078, 0.9999066591262817, 0.9998799562454224])
cnn_c15_mean = np.mean(cnn_c15_acc)
cnn_c15_std = np.std(cnn_c15_acc)

cnn_c20_acc = np.array([0.999893307685852, 0.9999333024024963, 0.9999066591262817, 0.9998133182525635, 0.9998666644096375, 0.999893307685852, 0.9998799562454224, 0.999893307685852, 0.9998799562454224, 0.9997066259384155])
cnn_c20_mean = np.mean(cnn_c20_acc)
cnn_c20_std = np.std(cnn_c20_acc)

dnn_c5_acc = np.array([0.9999866485595703, 0.9999600052833557, 0.9999600052833557, 0.9999333024024963, 0.9999600052833557, 0.9999732971191406, 0.9999600052833557, 0.9999866485595703, 0.9999600052833557, 0.9998533129692078])
dnn_c5_mean = np.mean(dnn_c5_acc)
dnn_c5_std = np.std(dnn_c5_acc)

dnn_c10_acc = np.array([0.9999732971191406, 0.999946653842926, 0.9999333024024963, 0.9999199509620667, 0.9999866485595703, 0.999946653842926, 0.9999333024024963, 0.9999600052833557, 0.9999600052833557, 0.9999732971191406])
dnn_c10_mean = np.mean(dnn_c10_acc)
dnn_c10_std = np.std(dnn_c10_acc)

dnn_c15_acc = np.array([0.9999732971191406, 0.9999732971191406, 0.9999732971191406, 0.9999732971191406, 0.9999866485595703, 0.9999866485595703, 0.9999866485595703, 0.9999732971191406, 0.9999600052833557, 0.9999866485595703])
dnn_c15_mean = np.mean(dnn_c15_acc)
dnn_c15_std = np.std(dnn_c15_acc)

dnn_c20_acc = np.array([0.9999732971191406, 0.9999732971191406, 0.999946653842926, 0.9999732971191406, 0.9999732971191406, 0.9999732971191406, 0.9999732971191406, 0.9999732971191406, 0.9999732971191406, 0.9999600052833557])
dnn_c20_mean = np.mean(dnn_c20_acc)
dnn_c20_std = np.std(dnn_c20_acc)

maj_c5_acc = 1 - 0.7667/100
maj_c10_acc = 1 - 0.231/100
maj_c15_acc = 1 - 0.1217/100
maj_c20_acc = 1 - 0.0933/100

print(min(maj_c5_acc, maj_c10_acc, maj_c15_acc, maj_c20_acc))



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
