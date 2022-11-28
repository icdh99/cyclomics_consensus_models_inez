import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt



'''
Plot heatmap DNN crosstest model coverage vs. test data coverage
'''
data = np.array([[8,6,6,6,5], [19,7,8,8,13], [23,8,8,6,14], [27,8,8,6,15], [16,9,5,3,9]])
plt.figure(1)
print(data.shape)
ax = sns.heatmap(data, annot=True, fmt='d', xticklabels=['3-5X','6-10X','11-15X','16-20X','3-20X'], yticklabels=['3-5X','6-10X','11-15X','16-20X','3-20X'])
ax.set_ylabel('Model')
ax.set_xlabel('Coverage of test set')
ax.set_title('Crosstest DNN models on different coverages in test set - Nr. samples wrong')
plt.savefig('DNN_crosstest_heatmap.png', bbox_inches="tight", dpi=500)

'''
Plot heatmap DNN crosstest model coverage vs. test data coverage
'''
data = np.array([[64,32,600,9531, 2860], [764,81,45,96,218], [1279,71,18,14,260], [10348,168,21,13,1786], [740,63,27,23,178,]])
plt.figure(2)
print(data.shape)
ax = sns.heatmap(data, annot=True, fmt='d', xticklabels=['3-5X','6-10X','11-15X','16-20X','3-20X'], yticklabels=['3-5X','6-10X','11-15X','16-20X','3-20X'])
ax.set_ylabel('Model')
ax.set_xlabel('Coverage of test set')
ax.set_title('Crosstest CNN models on different coverages in test set - Nr. samples wrong')
plt.savefig('CNN_crosstest_heatmap.png', bbox_inches="tight", dpi=500)


'''
Plot False Positive Rate for DNN crosstest model coverage vs. test data coverage
coverage test data on x axis
'''
model_dnn_5 = [ 0.0013566962502991908, 0.0010238926360016491, 0.0010238926360016491 ,0.0010238926360016491, 0.0008507252662754613] #alle scores
model_dnn_10 = [ 0.0031496704305799335, 0.0011819584179131382, 0.001370236771126401,  0.001370236771126401,0.0021952371643826256 ]
model_dnn_15 = [0.0037594161319272562, 0.0013264896765435576,0.0013596079755490795, 0.001028373161117608, 0.0023548856501632524 ]
model_dnn_20 = [0.004560767551225838,0.001370237770410631, 0.001370237770410631,  0.0010434804085884908,0.0025566902099261454 ]
model_dnn_all = [0.0026105636892442387, 0.0014845446830873943,0.0008220862973849901,  0.0005043915260946803, 0.001498069992629288]

labels = ['3-5X', '6-10X','11-15X','16-20','3-20X',]
x = np.arange(len(labels)) # label locations
width = 0.7
plt.figure(3)
plt.style.use('seaborn')
fig, ax = plt.subplots()
plt.title('False positive rate (FPR) for prediction of test data\n with DNN trained on different coverages')
rects1 = ax.bar(x-2*(width/5), model_dnn_5, width/5, label='Model DNN 3-5X')
rects2 = ax.bar(x-width/5, model_dnn_10, width/5, label='Model DNN 6-10X')
rects3 = ax.bar(x, model_dnn_15, width/5, label='Model DNN 11-15X')
rects4 = ax.bar(x+width/5, model_dnn_20, width/5, label='Model DNN 16-20X')
rects5 = ax.bar(x+2*(width/5), model_dnn_all, width/5, label='Model DNN 3-20X')
ax.set_ylabel('False Positive Rate (%)')
ax.set_xlabel('Coverage of test data')
ax.set_xticks(x, labels)
ax.legend()
# fig.tight_layout()
plt.savefig('Crosstest_DNN_covtestdataonx.png', bbox_inches="tight", dpi=500)


'''
Plot False Positive Rate for DNN crosstest model coverage vs. test data coverage
coverage of model on x axis --> better view of data
'''
model_dnn_5 = [ 0.0013566962502991908, 0.0010238926360016491, 0.0010238926360016491 ,0.0010238926360016491, 0.0008507252662754613] #alle scores
model_dnn_10 = [ 0.0031496704305799335, 0.0011819584179131382, 0.001370236771126401,  0.001370236771126401,0.0021952371643826256 ]
model_dnn_15 = [0.0037594161319272562, 0.0013264896765435576,0.0013596079755490795, 0.001028373161117608, 0.0023548856501632524 ]
model_dnn_20 = [0.004560767551225838,0.001370237770410631, 0.001370237770410631,  0.0010434804085884908,0.0025566902099261454 ]
model_dnn_all = [0.0026105636892442387, 0.0014845446830873943,0.0008220862973849901,  0.0005043915260946803, 0.001498069992629288]

test_dnn_5 = [model_dnn_5[0], model_dnn_10[0], model_dnn_15[0], model_dnn_20[0], model_dnn_all[0] ]
test_dnn_10 = [model_dnn_5[1], model_dnn_10[1], model_dnn_15[1], model_dnn_20[1], model_dnn_all[1] ]
test_dnn_15 = [model_dnn_5[2], model_dnn_10[2], model_dnn_15[2], model_dnn_20[2], model_dnn_all[2] ]
test_dnn_20 = [model_dnn_5[3], model_dnn_10[3], model_dnn_15[3], model_dnn_20[3], model_dnn_all[3] ]
test_dnn_all = [model_dnn_5[4], model_dnn_10[4], model_dnn_15[4], model_dnn_20[4], model_dnn_all[4] ]

labels = ['3-5X', '6-10X','11-15X','16-20','3-20X']

x = np.arange(len(labels)) # label locations
width = 0.7
plt.figure(4)
plt.style.use('seaborn')
fig, ax = plt.subplots()
plt.title('False positive rate (FPR) for prediction of test data\n with DNN trained on different coverages')
plt.ylim(0,0.005)
rects1 = ax.bar(x-2*(width/5),test_dnn_5, width/5, label='Test set DNN 3-5X')
rects2 = ax.bar(x-width/5,test_dnn_10, width/5, label='Test set DNN 6-10X')
rects3 = ax.bar(x,test_dnn_15, width/5, label='Test set DNN 11-15X')
rects4 = ax.bar(x+width/5,test_dnn_20, width/5, label='Test set DNN 16-20X')
rects5 = ax.bar(x+2*(width/5),test_dnn_all, width/5, label='Test set DNN 3-20X')
ax.set_ylabel('False Positive Rate (%)')
ax.set_xlabel('Coverage of model')
ax.set_xticks(x, labels)
ax.legend()
# fig.tight_layout()
plt.savefig('Crosstest_DNN_covmodelonx.png', bbox_inches="tight", dpi=500)


'''
Plot False Positive Rate for CNN crosstest model coverage vs. test data coverage 
split in Y axis
test data coverage on x axis
'''
model_cnn_5 = [ 0.01061206206037043, 0.005469971688438734,  0.06743633958388799, 0.8993948105411252, 0.2677498735873048 ]
model_cnn_10 = [0.1297141916754807,  0.013806881195643505, 0.007583488835795617,  0.015710853377944697,  0.03684884075125446]
model_cnn_15 = [0.21196044934784555,  0.011800035205571038, 0.003004995030296307,  0.0023545728518126184, 0.04326859992260976]
model_cnn_20 = [1.8329095888565206, 0.029100291130513118,  0.0035981200914143685, 0.002227971762716747,  0.30905601820525136]
model_cnn_all = [0.12603183315116478, 0.010785257877780636, 0.004612991812208138, 0.003950573467957092,0.030483964843798384 ]
labels = ['3-5X', '6-10X','11-15X','16-20','3-20X',]
x = np.arange(len(labels)) # label locations
width = 0.7
plt.figure(5)
plt.style.use('seaborn')
fig, (ax, ax2) = plt.subplots(2, 1, sharex=True)

plt.suptitle('False positive rate (FPR) for prediction of test data\n with CNN trained on different coverages')
ax.bar(x-2*(width/5), model_cnn_5, width/5, label='Model CNN 3-5X')
ax.bar(x-width/5, model_cnn_10, width/5, label='Model CNN 6-10X')
ax.bar(x, model_cnn_15, width/5, label='Model CNN 11-15X')
ax.bar(x+width/5, model_cnn_20, width/5, label='Model CNN 16-20X')
ax.bar(x+2*(width/5), model_cnn_all, width/5, label='Model CNN 3-20X')
ax2.bar(x-2*(width/5), model_cnn_5, width/5, label='Model CNN 3-5X')
ax2.bar(x-width/5, model_cnn_10, width/5, label='Model CNN 6-10X')
ax2.bar(x, model_cnn_15, width/5, label='Model CNN 11-15X')
ax2.bar(x+width/5, model_cnn_20, width/5, label='Model CNN 16-20X')
ax2.bar(x+2*(width/5), model_cnn_all, width/5, label='Model CNN 3-20X')
# plt.gca().set_title('title')
plt.subplots_adjust(hspace=0.1)

ax.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax.xaxis.tick_top()
ax.tick_params(labeltop=False)  # don't put tick labels at the top
ax2.xaxis.tick_bottom()

# plt.ylim(0,1)
fig.supylabel('False Positive Rate (%)')
ax2.set_xlabel('Coverage of test data')
ax2.set_xticks(x, labels)
ax2.set_ylim(0,0.35)
ax.set_ylim(0.8, 1.9)
ax.legend()

d = .015  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
ax.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal
# fig.tight_layout()
plt.savefig('Crosstest_CNN_covtestdataonx_splitaxis.png', bbox_inches="tight", dpi=500)


'''
Plot False Positive Rate for CNN crosstest model coverage vs. test data coverage 
split in Y axis
test data coverage on x axis
'''
model_cnn_5 = [ 0.01061206206037043, 0.005469971688438734,  0.06743633958388799, 0.8993948105411252, 0.2677498735873048 ]
model_cnn_10 = [0.1297141916754807,  0.013806881195643505, 0.007583488835795617,  0.015710853377944697,  0.03684884075125446]
model_cnn_15 = [0.21196044934784555,  0.011800035205571038, 0.003004995030296307,  0.0023545728518126184, 0.04326859992260976]
model_cnn_20 = [1.8329095888565206, 0.029100291130513118,  0.0035981200914143685, 0.002227971762716747,  0.30905601820525136]
model_cnn_all = [0.12603183315116478, 0.010785257877780636, 0.004612991812208138, 0.003950573467957092,0.030483964843798384 ]

test_cnn_5 = [model_cnn_5[0], model_cnn_10[0], model_cnn_15[0], model_cnn_20[0], model_cnn_all[0] ]
test_cnn_10 = [model_cnn_5[1], model_cnn_10[1], model_cnn_15[1], model_cnn_20[1], model_cnn_all[1] ]
test_cnn_15 = [model_cnn_5[2], model_cnn_10[2], model_cnn_15[2], model_cnn_20[2], model_cnn_all[2] ]
test_cnn_20 = [model_cnn_5[3], model_cnn_10[3], model_cnn_15[3], model_cnn_20[3], model_cnn_all[3] ]
test_cnn_all = [model_cnn_5[4], model_cnn_10[4], model_cnn_15[4], model_cnn_20[4], model_cnn_all[4] ]

labels = ['3-5X', '6-10X','11-15X','16-20','3-20X',]
x = np.arange(len(labels)) # label locations
width = 0.7
plt.figure(6)
plt.style.use('seaborn')
fig, (ax, ax2) = plt.subplots(2, 1, sharex=True)

plt.suptitle('False positive rate (FPR) for prediction of test data\n with CNN trained on different coverages')
ax.bar(x-2*(width/5), test_cnn_5, width/5, label='Test set CNN 3-5X')
ax.bar(x-width/5, test_cnn_10, width/5, label='Test set CNN 6-10X')
ax.bar(x, test_cnn_15, width/5, label='Test set CNN 11-15X')
ax.bar(x+width/5, test_cnn_20, width/5, label='Test set CNN 16-20X')
ax.bar(x+2*(width/5), test_cnn_all, width/5, label='Test set CNN 3-20X')
ax2.bar(x-2*(width/5), test_cnn_5, width/5, label='Test set CNN 3-5X')
ax2.bar(x-width/5, test_cnn_10, width/5, label='Test set CNN 6-10X')
ax2.bar(x, test_cnn_15, width/5, label='Test set CNN 11-15X')
ax2.bar(x+width/5, test_cnn_20, width/5, label='Test set CNN 16-20X')
ax2.bar(x+2*(width/5), test_cnn_all, width/5, label='Test set CNN 3-20X')
# plt.gca().set_title('title')
plt.subplots_adjust(hspace=0.1)

ax.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax.xaxis.tick_top()
ax.tick_params(labeltop=False)  # don't put tick labels at the top
ax2.xaxis.tick_bottom()

# plt.ylim(0,1)
fig.supylabel('False Positive Rate (%)')
ax2.set_xlabel('Coverage of model')
ax2.set_xticks(x, labels)
ax2.set_ylim(0,0.35)
ax.set_ylim(0.8, 1.9)
ax.legend()

d = .015  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
ax.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal
# fig.tight_layout()
plt.savefig('Crosstest_CNN_covmodelonx_splitaxis.png', bbox_inches="tight", dpi=500)


'''
Plot False Positive Rate for CNN crosstest model coverage vs. test data coverage
'''
plt.figure(7)
plt.style.use('seaborn')
fig, ax = plt.subplots()


test_cnn_5 = [model_cnn_5[0], model_cnn_10[0], model_cnn_15[0], model_cnn_20[0], model_cnn_all[0] ]
test_cnn_10 = [model_cnn_5[1], model_cnn_10[1], model_cnn_15[1], model_cnn_20[1], model_cnn_all[1] ]
test_cnn_15 = [model_cnn_5[2], model_cnn_10[2], model_cnn_15[2], model_cnn_20[2], model_cnn_all[2] ]
test_cnn_20 = [model_cnn_5[3], model_cnn_10[3], model_cnn_15[3], model_cnn_20[3], model_cnn_all[3] ]
test_cnn_all = [model_cnn_5[4], model_cnn_10[4], model_cnn_15[4], model_cnn_20[4], model_cnn_all[4] ]


plt.title('False positive rate (FPR) for prediction of test data\n with CNN trained on different coverages')
ax.bar(x-2*(width/5), test_cnn_5, width/5, label='Test set CNN 3-5X')
ax.bar(x-width/5, test_cnn_10, width/5, label='Test set CNN 6-10X')
ax.bar(x, test_cnn_15, width/5, label='Test set CNN 11-15X')
ax.bar(x+width/5, test_cnn_20, width/5, label='Test set CNN 16-20X')
ax.bar(x+2*(width/5), test_cnn_all, width/5, label='Test set CNN 3-20X')


# plt.ylim(0,1)
fig.supylabel('False Positive Rate (%)')
ax.set_xlabel('Coverage of model')
ax.set_xticks(x, labels)
ax.set_ylim(0,0.005)
ax.legend()

plt.savefig('Crosstest_CNN_covmodelonx_limity.png', bbox_inches="tight", dpi=500)


