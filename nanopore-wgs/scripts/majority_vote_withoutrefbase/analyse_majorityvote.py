import os
import matplotlib.pyplot as plt
import sklearn
from sklearn import metrics
import seaborn as sns
import pandas as pd
import numpy as np
import sys


file = sys.argv[1]

with open(f'{file}', 'r') as f:
    lines = [line.rstrip() for line in f]
    print(f'header: {lines[0]}')
    lines=lines[1:]
print(f'number of entries in {file}: {len(lines)}')

acc_maj = []
nr_wrong = 0
list_ref = []
list_maj = []
nr_bases_wrong = 0

for line in lines:
    line = line.split('\t')
    pos = line[0]
    ref = line[1]
    maj = line[2][0]
    if ref != maj:
        nr_wrong += 1
    list_ref.append(ref)
    list_maj.append(maj)
    
print(f'number of samples wrongly predicted by majority vote in {file}: {nr_wrong}')
print(f'percentage predicted wrongly by majority vote: {round(nr_wrong / len(lines) * 100, 4)}%')
acc_maj.append(nr_wrong / len(lines) * 100)

plt.figure(2)
ax = plt.subplot() #fig, axis
labels = sklearn.utils.multiclass.unique_labels(list_ref, list_maj)
print(labels)
cm = sklearn.metrics.confusion_matrix(list_ref, list_maj, labels=labels)
sns.heatmap(cm, annot=True, fmt='g', ax=ax, cmap = 'Greens')
ax.set_xlabel('Predicted labels')
ax.set_ylabel("True labels")
ax.set_title(f'{file} - Confusion matrix')
ax.xaxis.set_ticklabels(labels)
ax.yaxis.set_ticklabels(labels)
plt.savefig(f'{file}_cm.png')

def perf_measure(y_actual, y_pred):
    class_id = set(y_actual).union(set(y_pred))
    TP = []
    FP = []
    TN = []
    FN = []

    for index ,_id in enumerate(class_id):
        TP.append(0)
        FP.append(0)
        TN.append(0)
        FN.append(0)
        for i in range(len(y_pred)):
            if y_actual[i] == y_pred[i] == _id:
                TP[index] += 1
            if y_pred[i] == _id and y_actual[i] != y_pred[i]:
                FP[index] += 1
            if y_actual[i] == y_pred[i] != _id:
                TN[index] += 1
            if y_pred[i] != _id and y_actual[i] != y_pred[i]:
                FN[index] += 1
    return class_id,TP, FP, TN, FN

class_id, tp, fp, tn, fn = perf_measure(list_ref, list_maj)
print(f'classes: {class_id}')
print(f'tp, fp, tn, fn: {tp, fp, tn, fn}')

fpr_list = []
for f, t in zip(fp, tn):
    fpr = f/(f+t)
    fpr_list.append(fpr)

print(f'fpr list: {fpr_list}')

fpr_list = [x*100 for x in fpr_list]

for i,j in zip(class_id, fpr_list):
    print(i,j)

mean_fpr = sum(fpr_list)/len(fpr_list)
print(f'mean fpr: {mean_fpr}')


print(f'file: {file}')
print(f'accuracy of majority vote: {acc_maj}')
print(f'F1 score of majority vote: {sklearn.metrics.f1_score(list_ref, list_maj, average = "macro")}')

f1_scores=sklearn.metrics.f1_score(list_ref, list_maj, average = None, labels=labels)
print(f'F1 score of majority vote: {f1_scores}')
f1_scores_with_labels = {label:score for label,score in zip(labels, f1_scores)}
print(f1_scores_with_labels)






