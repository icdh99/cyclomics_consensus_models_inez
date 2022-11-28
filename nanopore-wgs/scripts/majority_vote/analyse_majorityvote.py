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

print(file)
print(acc_maj)




