import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mlb


"""
Plot read count per coverage number for cyclomics clean datasets with masked reference base
region 1-5
/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/predict_cyclomics_clean_bam_masked ref base --> all DNN files from this folder
run predictions for CNN as well? --> no

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
model_5 = [0, 0.06572106599995417, 0.04225388416001738, 0.036170323627905517, 0.03473633926657689, 0.03353095058910089, 0.03282831524719355, 0.03425713068555488, 0.030855966410156317, 0.030423081423532755, 0.03520524220225684, 0.03173638181143768, 0.023838869530374267, 0.031636431580377766, 0.02264784963934616, 0.027608697064383483, 0.023945173808934028,0.022612974420203335, 0.028906554005225415, 0.02674325516811228]
model_10 = [0, 0.1317350726453869, 0.07440448374818368, 0.05023052419632195, 0.04194507501959327,0.03812277884089666, 0.03601950041466441,  0.03523877954069833, 0.031306888675022904, 0.03067387237997489, 0.035314313741518846,  0.03227210337785812, 0.024853289510390196, 0.03482130724283191, 0.023701425245704774, 0.029233022921938082,0.029725288789437615,  0.022612974420203335, 0.03057423981321919, 0.027004589909168757 ]
model_15 = [0, 0.2544877603904541,0.13778522426869544,  0.07851703162061166,0.0568818263237712,  0.04701299304576118, 0.04243859425182629, 0.04117744928523506, 0.034592380013721, 0.03435170968709855, 0.038257214918351906, 0.03213840941655396,0.025698682942499197, 0.0346089821986683, 0.025281653420133676,  0.028258405251516048,  0.02931267959176933, 0.022612974420203335, 0.030018511415372814, 0.028224225793806353]
model_20 = [0, 0.35770710794587507, 0.15025795610614176 , 0.0947412212395675, 0.07087623168357868, 0.0615627104037777, 0.05274553726171433, 0.05020915573525493, 0.0419360948026298, 0.04003507038733722, 0.04239925272679513, 0.03602180055438756,0.027051290938324746, 0.040129433346922136,  0.026861756758892033, 0.032805734832219775 , 0.029725534233906926, 0.024422012373819604, 0.03224210485354858, 0.029356756017481642]
model_100 = [0, 0.1945678454384404, 0.10468678228287626, 0.06732365585646884, 0.05271023251325541, 0.04562474938423941, 0.0421084292052034,  0.03990139007019798, 0.03542972063987364, 0.03334851707753322, 0.03596832171810863, 0.03267391831252603, 0.02451514951705155, 0.032485731757032205, 0.022384797299076692, 0.027608786739986943, 0.025596987812530964, 0.021256195954991137, 0.028906554005225415, 0.026307697266351494]

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

plt.title('Error rate of Cyclomics reads per coverage bin for each model')
ax.bar(x-3*(width/5), consensus, width/5, label='Cyclomics Consensus score')
ax.bar(x-2*(width/5), model_5, width/5, label='Model DNN 3-5X')
ax.bar(x-(width/5), model_10, width/5, label='Model DNN 6-10X')
ax.bar(x, model_15, width/5, label='Model DNN 11-15X')
ax.bar(x+(width/5), model_20, width/5, label='Model DNN 16-20X')
ax.bar(x+2*(width/5), model_100, width/5, label='Model DNN 3-20X')

ax.set_xlabel('Coverage of Cyclomics split read')
ax.set_xticks(x, coverage)
ax.set_ylabel('Error rate (%)')
# ax.set_ylim(0,0.005)
ax.legend()
fig.set_size_inches(18.5, 10.5)
plt.savefig('Cyclomics_clean_maskedrefbase_predictionscore_percovpermodel.png', bbox_inches="tight", dpi=500)


"""
plot average prediction score per model and consensus score
scores: /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/cyclomics_clean_predict/predictionscore_permodelforallcov.txt
all scores in percentages

"""
# plt.figure(3)
# plt.style.use('seaborn')
# fig, ax = plt.subplots()

# scores = [0.233129439116805,0.0420223487647382 , 0.06821057197594978,0.09733281951385547, 0.11525441014520281,  0.08587664936907473]
# labels = ['Cycas \n Consensus', '3-5X', '6-10X', '11-15X', '16-20X', '3-20X']
# x = np.arange(len(labels))

# plt.title('Prediction score of Cyclomics reads (all coverages together) for each model')
# ax.bar(x, scores, 0.7)
# ax.set_xlabel('Coverage of each model')
# ax.set_xticks(x, labels)
# ax.set_ylabel('Prediction score (%)')
# # ax.set_ylim(0,0.005)
# # ax.legend()
# # fig.set_size_inches(18.5, 10.5)
# plt.savefig('Cyclomics_clean_predictionscore_permodel.png', bbox_inches="tight", dpi=500)