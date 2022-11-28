import matplotlib.pyplot as plt
import pandas as pd
import sys
import pylab as plt
import numpy as np
import matplotlib.patches as patches

first = ['DNN', 'CNN']
second = ['3-5X', '6-10X', '11-15X', '16-20X', '3-20X']
combis = [(f,s) for f in first for s in second]
print(combis)

mutations_25 = [7578324, 7578387]   # region 4
mutations_50 = [7577900,7577926, 7577927]   # region 3


# name = sys.argv[1]
# region = sys.argv[2] # make into list for all regions
def get_cov(cov):
    if cov == '3-5X': cov_ret = 'c5'
    if cov == '6-10X': cov_ret = 'c10'
    if cov == '11-15X': cov_ret = 'c15'
    if cov == '16-20X': cov_ret = 'c20'
    if cov == '3-20X': cov_ret = 'c100'
    return cov_ret

def calculate_errors(csv):
    df = pd.read_csv(csv, sep='\t')   
    list_error_A = []; list_error_C = []; list_error_G = []; list_error_T = []; list_pos_chr = []
    for idx, row in df.iterrows():
        ref = row['REF_BASE'].upper()
        list_pos_chr.append(row['POS'])
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
    return list_error_A, list_error_C, list_error_G, list_error_T, list_pos_chr

fig, ax = plt.subplots(len(combis)+1, 4, sharex='col', sharey = 'row', figsize = (15, 15), constrained_layout=True)
# fig.tight_layout()
fig.tight_layout(rect=[0.07, 0.03, 1, 0.95])

fig.subplots_adjust(top=0.95)

for col, region in enumerate(['region1','region3', 'region4', 'region5']):
    for row, combi in enumerate(combis):
            cov = get_cov(combi[1])
            model= combi[0]
            print(region,model, combi[1], model.lower(), cov)
            print(row, col)
            name = f'predict_cycl_muts_{model.lower()}_{cov}_merged'
            print(f'{name}_{region}')
            csv = f'perbase_subsetreads/{name}_{region}.csv'
            list_error_A, list_error_C, list_error_G, list_error_T, list_pos_chr = calculate_errors(csv)
            list_pos = [i for i in range(len(list_error_A))]
            ax[row+1, col].bar(np.asarray(list_pos,float), list_error_A, width = 0.55, label='A')
            ax[row+1, col].bar(np.asarray(list_pos,float), list_error_T, width = 0.55, label='T')
            ax[row+1, col].bar(np.asarray(list_pos,float), list_error_G, width = 0.55, label='G')
            ax[row+1, col].bar(np.asarray(list_pos,float), list_error_C, width = 0.55, label='C')
            ax[row+1, col].set_yscale('log')
            ax[row+1, col].set_ylim(bottom = 0.001, top = 100)
            ax[row+1, col].set_xticks(ticks = list_pos,labels=list_pos_chr)
            ax[row+1, col].xaxis.set_major_locator(plt.MaxNLocator(3))  

            if col == 0:
                ax[row+1, col].set_ylabel(f'{combi[0]} {combi[1]}')
            if row == 9:
                ax[row+1, col].set_xlabel(region)

            if region == 'region3':
                for x in mutations_50: 
                    ax[row+1, col].axvspan(x-list_pos_chr[0]-0.1, x-list_pos_chr[0]+0.1, facecolor='b', alpha=0.5)
                    ax[row+1, col].text(x-list_pos_chr[0], .8, '*', fontsize=12)
            
            if region == 'region4':
                for x in mutations_25: 
                    ax[row+1, col].axvspan(x-list_pos_chr[0]-0.1, x-list_pos_chr[0]+0.1, facecolor='b', alpha=0.5)
                    ax[row+1, col].text(x-list_pos_chr[0], .8, '*', fontsize=12)
            
for col, region in enumerate(['region1', 'region3', 'region4', 'region5']):
    row = 0
    csv = f'perbase_subsetreads/cycl_muts_consensus_{region}.csv'
    list_error_A, list_error_C, list_error_G, list_error_T, list_pos_chr = calculate_errors(csv)
    list_pos = [i for i in range(len(list_error_A))]
    ax[row, col].bar(np.asarray(list_pos,float), list_error_A, width = 0.55, label='A')
    ax[row, col].bar(np.asarray(list_pos,float), list_error_T, width = 0.55, label='T')
    ax[row, col].bar(np.asarray(list_pos,float), list_error_G, width = 0.55, label='G')
    ax[row, col].bar(np.asarray(list_pos,float), list_error_C, width = 0.55, label='C')
    ax[row, col].set_yscale('log')
    ax[row, col].set_ylim(bottom = 0.001, top = 100)
    ax[row, col].set_xticks(ticks = list_pos,labels=list_pos_chr)
    ax[row, col].xaxis.set_major_locator(plt.MaxNLocator(3))  
    if col == 0:
        ax[row, col].set_ylabel('Cycas \nConsensus')

    if region == 'region3':
        for x in mutations_50: 
            ax[row, col].axvspan(x-list_pos_chr[0]-0.1, x-list_pos_chr[0]+0.1, facecolor='b', alpha=0.5)
            print(x)
            
            ax[row, col].text(x-list_pos_chr[0], .8, '*', fontsize=12)
            
    if region == 'region4':
        for x in mutations_25: 
            ax[row, col].axvspan(x-list_pos_chr[0]-0.1, x-list_pos_chr[0]+0.1, facecolor='b', alpha=0.5)
            print(x)
            print()
            ax[row, col].text(x-list_pos_chr[0], .8, '*', fontsize=12)
    
labels = ['A', 'T', 'G', 'C']
fig.legend(labels, loc='lower right', bbox_to_anchor=(1,-0.1), ncol=len(labels))

plt.suptitle('Error rate per position for each region')
fig.supxlabel('Genomic coordinate on chromosome 17')
fig.supylabel('Error rate (%)')
# ax.set_ylabel('Error rate (%)')
# ax.set_xlabel("Genomic coordinate on chromosome 17")
# ax.set_title(f'Error rate per position per base - {name} - {region}')
plt.savefig(f'plots_errorrate/all_subsetreads.png' , bbox_inches="tight", dpi=400)





