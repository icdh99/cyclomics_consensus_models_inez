import matplotlib.pyplot as plt
import numpy as np


"""
AANPASSEN
# plot average prediction score per model and consensus score
# scores: /hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/scripts/cyclomics_clean_predict/predictionscore_permodelforallcov.txt
# all scores in percentages
"""

plt.figure(1)
plt.style.use('seaborn')
fig, ax = plt.subplots()

scores = [0.4960230235738520 , 0.464648, 0.5012101649660285, 0.5248049430633771, 0.5367538511307097, 0.519775149291565]
labels = ['Cycas \n Consensus', '3-5X', '6-10X', '11-15X', '16-20X', '3-20X']
x = np.arange(len(labels))

plt.title('Prediction score of Genome-Wide Cyclomics reads (all coverages together) for each model')
ax.bar(x, scores, 0.7)
ax.set_xlabel('Coverage of each model')
ax.set_xticks(x, labels)
ax.set_ylabel('Prediction score (%)')
# ax.set_ylim(0,0.005)
# ax.legend()
# fig.set_size_inches(18.5, 10.5)
plt.savefig('Cyclomics_genomewide_predictionscore_permodel.png', bbox_inches="tight", dpi=500)

"""
Cyclomics WGS predict with masked reference baesa
# all scores in percentages
"""

plt.figure(2)
plt.style.use('seaborn')
fig, ax = plt.subplots()

scores = [0.4960230235738520 , 0.4782624524551967, 0.5054231262627907,0.5456961647444832, 0.5913587224100175, 0.5204766664316861]
labels = ['Cycas \n Consensus', '3-5X', '6-10X', '11-15X', '16-20X', '3-20X']
x = np.arange(len(labels))

plt.title('Error rate of Genome-Wide Cyclomics reads (all coverages together) for each model')
ax.bar(x, scores, 0.7)
ax.set_xlabel('Coverage of each model')
ax.set_xticks(x, labels)
ax.set_ylabel('Error rate (%)')
# ax.set_ylim(0,0.005)
# ax.legend()
# fig.set_size_inches(18.5, 10.5)
plt.savefig('Cyclomics_genomewide_predictionscore_permodel_maskedrefbase.png', bbox_inches="tight", dpi=500)

"""
Cyclomics WGS predict with masked reference baesa
# all scores in percentages
calculate score per read, add to list, plot boxplot per model
"""





