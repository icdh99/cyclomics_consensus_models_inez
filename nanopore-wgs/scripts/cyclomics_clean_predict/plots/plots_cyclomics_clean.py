import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mlb


"""
Plot read count per coverage number for cyclomics clean datasets
region 2-4
/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/predict_cyclomics_clean --> all DNN files from this folder
region 5 did not complete running, stopped at file 76 
"""

# coverage = ['3X','4X','5X','6X','7X','8X','9X','10X','11X','12X','13X','14X','15X','16X','17X','18X','19X','20X','>20X']
# counts = [10381, 8589,6581,4870,3514,2774,1996,1573,1266,1020,768,630,499,382,325,292,227,221,1305]

# fig = plt.figure(1)
# plt.figure(figsize=(12,4.8))
# fig.set_tight_layout(True)
# plt.style.use('seaborn')
# # plt.style.use('fivethirtyeight')
# pos_x = np.arange(len(coverage))
# plt.bar(pos_x, counts)
# plt.xticks(pos_x, coverage)
# plt.ylabel('Nr. reads')
# plt.xlabel('Coverage number')
# plt.title('Number of reads per coverage number for CyclomicsSeq dataset')
# plt.savefig('Cyclomics_clean_readcount_percoverage.png', bbox_inches='tight', dpi=500)


"""
Plot prediction score per coverage number per model
/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/cyclomics_clean_predict/slurm-14810408_predictionscorepermodelpercov.out
all scores are in percentages
"""
coverage = ['Cycas \nConsensus', '3X','4X','5X','6X','7X','8X','9X','10X','11X','12X','13X','14X','15X','16X','17X','18X','19X','20X','>20X']

consensus = [0]*20
consensus[0] = 0.233129439116805
model_5 = [0, 0.058781945911859555, 0.04141229973862444, 0.04014567791214681, 0.03616742255049668, 0.03509898585762776, 0.03478135115480951, 0.034400312286522884, 0.03163001914745802, 0.03176849129971795, 0.033737326573272754, 0.0300284269108089, 0.024342183955562924, 0.03444949703734325, 0.023853381216787477, 0.025548377678017445, 0.01869149435971528, 0.01897310840899325, 0.0318800202368824, 0.0244635903790788241]
model_10 = [0, 0.12927350685427863, 0.07001037613875515, 0.05348713911381243, 0.04249743843609426, 0.03862570416338069, 0.036200097296342416, 0.03537633713405314, 0.03259828503972714, 0.03270914257110581, 0.03535662282175539, 0.03136323294874447, 0.025811271341514598, 0.03365450864417379, 0.02418499867479459, 0.027981896929290963, 0.025763951685012956, 0.018415075808728743, 0.0339591519914617, 0.025318213623762797]
model_15 = [0, 0.19953967694284727, 0.10469388989272446, 0.0705813887839346, 0.05498823768738221, 0.04500749341177624, 0.04246999641201755, 0.040865718907287275, 0.03590667170166962, 0.034381211347262776, 0.03751616028846958, 0.032030642648133385, 0.026021119075998456, 0.03842443900319056, 0.023853697323085076, 0.027576585856455758, 0.02828997221520586, 0.021205238810051284, 0.03188002023688241, 0.025425041529348297]
model_20 = [0, 0.23885323392050253, 0.12457419764381912, 0.0836967488555538, 0.0637100561866161,0.054411806690301094, 0.04841941279791897, 0.04519676144771143, 0.03945705797202019, 0.03772528053605429, 0.04048501042489018, 0.03419932702397457, 0.028958987358772476,0.0413393964448119,  0.026835409488470713, 0.02960403588171363, 0.029805958160517714,  0.021763271410315792,  0.03188002023688241, 0.02713428801871625 ]
model_100 = [0, 0.18096974776809935, 0.08747079029436827,0.058873008367298085, 0.0462907260540925, 0.04104424347767673, 0.03803085304439038,  0.03671828778110533,0.032033592506882785, 0.032186800485728084, 0.034547022411031296,  0.030028777578512744,0.02560147733115091, 0.03683446221685163, 0.023191171452330548, 0.0263599717745533,  0.026269658039778324, 0.01897310840899325, 0.030493932400496217, 0.025211385718177305 ]

# wrong way of calculating average prediciton score per model
# print(f'consensus: {consensus[0]}%')
# print(f'mean model 5: {sum(model_5)/(len(model_5)-1)}%')
# print(f'mean model 10: {sum(model_10)/(len(model_10)-1)}%')
# print(f'mean model 15: {sum(model_15)/(len(model_15)-1)}%')
# print(f'mean model 20: {sum(model_20)/(len(model_20)-1)}%')
# print(f'mean model 100: {sum(model_100)/(len(model_100)-1)}%')

print(len(coverage))
print(len(consensus))
print(len(model_5))
print(len(model_10))
print(len(model_15))
print(len(model_20))
print(len(model_100))

width = 0.7
x = np.arange(len(coverage)) 

plt.figure(2)
plt.style.use('seaborn')
fig, ax = plt.subplots()

plt.title('Prediction score of Cyclomics reads per coverage bin for each model')
ax.bar(x-3*(width/5), consensus, width/5, label='Cyclomics Consensus score')
ax.bar(x-2*(width/5), model_5, width/5, label='Model DNN 3-5X')
ax.bar(x-(width/5), model_10, width/5, label='Model DNN 6-10X')
ax.bar(x, model_15, width/5, label='Model DNN 11-15X')
ax.bar(x+(width/5), model_20, width/5, label='Model DNN 16-20X')
ax.bar(x+2*(width/5), model_100, width/5, label='Model DNN 3-20X')

ax.set_xlabel('Coverage of Cyclomics split read')
ax.set_xticks(x, coverage)
ax.set_ylabel('Prediction score (%)')
# ax.set_ylim(0,0.005)
ax.legend()
fig.set_size_inches(18.5, 10.5)
plt.savefig('Cyclomics_clean_predictionscore_percovpermodel.png', bbox_inches="tight", dpi=500)


"""
plot average prediction score per model and consensus score
scores: /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/cyclomics_clean_predict/predictionscore_permodelforallcov.txt
all scores in percentages
"""
plt.figure(3)
plt.style.use('seaborn')
fig, ax = plt.subplots()

scores = [0.233129439116805,0.0420223487647382 , 0.06821057197594978,0.09733281951385547, 0.11525441014520281,  0.08587664936907473]
labels = ['Cycas \n Consensus', '3-5X', '6-10X', '11-15X', '16-20X', '3-20X']
x = np.arange(len(labels))

plt.title('Prediction score of Cyclomics reads (all coverages together) for each model')
ax.bar(x, scores, 0.7)
ax.set_xlabel('Coverage of each model')
ax.set_xticks(x, labels)
ax.set_ylabel('Prediction score (%)')
# ax.set_ylim(0,0.005)
# ax.legend()
# fig.set_size_inches(18.5, 10.5)
plt.savefig('Cyclomics_clean_predictionscore_permodel.png', bbox_inches="tight", dpi=500)