import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

names = ['DNN c20 no ref', 'DNN c20 ref', 'CNN c20 no ref', 'CNN c20 ref']
perc_wrong = [0.210, 0.209, 0.155, 0.138]

acc = [0.998239, 0.998650, 0.998447, 0.99861]
f1 = [0.998238,0.99865, 0.99844, 0.998610]
loss = [0.009354, 0.007484, 0.006568, 0.0059]

# plt.figure(1)
# plt.style.use('seaborn')
# plt.ylim(0.995, 1)
# plt.title('Accuracy - model performance ')
# sns.barplot(x=names, y=acc)
# plt.savefig('1209_acc.png')

# plt.figure(2)
# plt.style.use('seaborn')
# plt.ylim(0.995, 1)
# plt.ylabel('F1 score')
# plt.title('F1 score - model performance')
# sns.barplot(x=names, y=f1)
# plt.savefig('1209_F1.png')

# plt.figure(3)
# plt.ylim(0, 0.015)
# plt.ylabel('Loss')
# plt.title('Loss - model performance')
# sns.barplot(x=names, y=loss)
# plt.savefig('1209_loss.png')

names = ['DNN\n c20 no ref', 'DNN \nc20 ref', 'CNN \nc20 no ref', 'CNN \nc20 ref', 'Cycas\n Consensus \nv1', 'Cycas \nConsensus \nv25', 'Cyclomics \nnew \nCNN \nc20 no ref', 'Cyclomics \nnew \nDNN \nc20 no ref']
pred = [0.73, 0.34, 0.78, 0.67, 0.415,  0.233129, 0, 0]
perc = [0.176, 0.134, 0.155, 0.138, 0, 0, 0, 0]
perc2 = [0,0,0,0,0,0,0.17927096474337692, 0.1438594161520926]

fig = plt.figure(4)
fig.set_tight_layout(True)
plt.style.use('seaborn')
# plt.rcParams["figure.autolayout"] = True
plt.grid(True)
plt.ylim(0, 0.8)
plt.title('Prediction score (Cyclomics) vs. Model performance (Lambda)')
plt.ylabel('% samples predicted wrong')
width = 0.27
pos_x = np.arange(len(pred))
b = plt.bar(pos_x - 0.5*width, pred, 0.4, label = 'Prediction score')
b[-3].set_color('steelblue')
b[-4].set_color('steelblue')
plt.bar(pos_x + width, perc, 0.4, label = 'Model performance lambda')
plt.bar(pos_x + 2*width, perc2, 0.4, label = 'Model performance new cyclomics')
plt.xticks(pos_x, names)
plt.legend()

plt.savefig('1909_perc.png', bbox_inches='tight')
