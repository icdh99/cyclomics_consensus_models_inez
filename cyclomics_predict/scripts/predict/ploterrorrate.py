import matplotlib.pyplot as plt
import pandas as pd
import os
import sys
import math
import pylab as plt
import numpy as np
import matplotlib.patches as patches
import Bio
from Bio import SeqIO
import gzip as gz

name_csv = sys.argv[1]
name_fastq = sys.argv[2]

print(name_csv,name_fastq)
df = pd.read_csv(f'perbase/{name_csv}.csv', sep='\t')   #perbase/

list_pos = []
list_error_A = []
list_error_C = []
list_error_G = []
list_error_T = []

error = 0
total = 0   

for idx, row in df.iterrows():
    ref = row['REF_BASE']
    total += row['DEPTH']
    error_toadd = row['DEPTH']
    error += error_toadd
    if ref == 'A': 
        list_error_A.append(0)
        list_error_C.append(row['C']/ row['DEPTH'] * 100)
        list_error_G.append(row['G']/ row['DEPTH'] * 100)
        list_error_T.append(row['T']/ row['DEPTH'] * 100)
    if ref == 'C': 
        list_error_C.append(0)
        list_error_A.append(row['A']/ row['DEPTH'] * 100)
        list_error_G.append(row['G']/ row['DEPTH'] * 100)
        list_error_T.append(row['T']/ row['DEPTH'] * 100)
    if ref == 'G': 
        list_error_G.append(0)
        list_error_A.append(row['A']/ row['DEPTH'] * 100)
        list_error_C.append(row['C']/ row['DEPTH'] * 100)
        list_error_T.append(row['T']/ row['DEPTH'] * 100)
    if ref == 'T': 
        list_error_T.append(0)
        list_error_A.append(row['A']/ row['DEPTH'] * 100)
        list_error_C.append(row['C']/ row['DEPTH'] * 100)
        list_error_G.append(row['G']/ row['DEPTH'] * 100)

list_pos = [i for i in range(len(list_error_A))]

plt.figure(2, figsize=(20,4.8))
plt.rcParams['figure.figsize'] = 10, 4.8
fig, ax = plt.subplots()
ax.bar(list_pos, list_error_A, width = 0.55, label='A')
ax.bar(list_pos, list_error_T, width = 0.55, label='T')
ax.bar(list_pos, list_error_G, width = 0.55, label='G')
ax.bar(list_pos, list_error_C, width = 0.55, label='C')
ax.legend()
ax.set_ylim(top = 6)
# if name_csv[7:10] == 'CNN':
#     ax.set_ylim(top = 90)
# else:
#     ax.set_ylim(top = 25)
ax.set_ylabel('Error rate (%)')
ax.set_xlabel("Position on TP53 amplicon")
ax.set_title(f'Error rate per position per base -  {name_csv}')
plt.savefig(f'/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/results/predict/plotserrorrate/error_rate_perpos_{name_csv}.png')

def plot_fastq_qualities(filename, ax=None):
    fastq_parser = SeqIO.parse((filename), "fastq")
    res=[]
    for record in fastq_parser:
        score=record.letter_annotations["phred_quality"]
        res.append(score)

    df = pd.DataFrame(res)
    df2 = df.mean(axis=0)
    l = len(df.T)+1
    if ax==None:
        f,ax=plt.subplots(figsize=(12,5))
    rect = patches.Rectangle((0,0),l,20,linewidth=0,facecolor='r',alpha=.4)
    ax.add_patch(rect)
    rect = patches.Rectangle((0,20),l,8,linewidth=0,facecolor='yellow',alpha=.4)
    ax.add_patch(rect)
    rect = patches.Rectangle((0,28),l,72,linewidth=0,facecolor='g',alpha=.4)
    ax.add_patch(rect)
    df.mean().plot(ax=ax,c='black')
    boxprops = dict(linestyle='-', linewidth=1, color='black')
    df.plot(kind='box', ax=ax, grid=False, showfliers=False,
            color=dict(boxes='black',whiskers='black')  )
    ax.set_xticks(np.arange(0, l, 5))
    ax.set_xticklabels(np.arange(0, l, 5))
    ax.set_xlabel('position(bp)')
    ax.set_xlim((0,l))
    ax.set_ylim((0,100))
    ax.set_title(f'per base sequence quality - {name_fastq}.test')    
    f.savefig(f'/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/results/predict/plotserrorrate/qs_perpos_{name_fastq}.png')
    return

plot_fastq_qualities(name_fastq)
