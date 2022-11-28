import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


'''
Plot False Positive Rate for DNN crosstest model coverage vs. test data coverage
coverage of model on x axis --> better view of data
'''
model_dnn_5 = [ 0.001229902473845455, 0.0008521885394569295, 0.0020400583438191094, 0.00203547159764064, 0.0013850474749999434] #alle scores
model_dnn_10 = [0.0013834836433216, 0.0018895196047686515,  0.001558322829083152, 0.0013565357334410768, 0.001913575932693817 ]
model_dnn_15 = [0.002538270952725832, 0.0017163714245560257,0.0013896546310461855,0.001567274524456318,  0.0017253232455268887 ]
model_dnn_20 = [0.005929468558213777, 0.0020759615822403166, 0.0013743996872078016, 0.0008791381234358278,  0.002760851325556583 ]
model_dnn_all = [ 0.002433025521287399,0.0027552605058317817,  0.0018744180221152667,  0.001212028867064674, 0.002586589349792491]
majority_vote = [0.08264720854621975, 0.03853642259079844, 0.02533773010834777, 0.021338958792814083, 0.04014444123937523]

test_dnn_5 = [model_dnn_5[0], model_dnn_10[0], model_dnn_15[0], model_dnn_20[0], model_dnn_all[0], majority_vote[0] ]
test_dnn_10 = [model_dnn_5[1], model_dnn_10[1], model_dnn_15[1], model_dnn_20[1], model_dnn_all[1], majority_vote[1] ]
test_dnn_15 = [model_dnn_5[2], model_dnn_10[2], model_dnn_15[2], model_dnn_20[2], model_dnn_all[2], majority_vote[2] ]
test_dnn_20 = [model_dnn_5[3], model_dnn_10[3], model_dnn_15[3], model_dnn_20[3], model_dnn_all[3], majority_vote[3] ]
test_dnn_all = [model_dnn_5[4], model_dnn_10[4], model_dnn_15[4], model_dnn_20[4], model_dnn_all[4], majority_vote[4]]


labels = ['3-5X', '6-10X','11-15X','16-20','3-20X', 'Majority vote']

plt.figure(3)
x = np.arange(len(labels)) # label locations
width = 0.7
plt.style.use('seaborn-muted')
# cmap = sns.color_palette("Set2")
# sns.color_palette("Set2")
fig, ax = plt.subplots()
ax.set_yscale('log')
plt.title('False positive rate (FPR) for prediction of test data\n with DNN trained on different coverages')
# plt.ylim(0,0.005)
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
plt.savefig('Crosstest_DNN.png', bbox_inches="tight", dpi=500)




'''
Plot False Positive Rate for CNN crosstest model coverage vs. test data coverage
'''
plt.figure(7)
plt.style.use('seaborn-muted')
fig, ax = plt.subplots()

model_cnn_5 = [0.0018262301264249672,0.0015070236798100422,  0.002194784791497539, 0.012495992712562999,0.00575087357732309]
model_cnn_10 = [0.3054206836783206, 0.01987803083023828, 0.0030470974066314207,  0.0028694630017919234,  0.05833963471044422]
model_cnn_15 = [0.03736056900969292, 0.006670594510467162,0.0031690446747802553,  0.0028572638275782313, 0.009246537267916062 ]
model_cnn_20 = [0.09128647582475102, 0.009708406980644853, 0.0034154474157329236,0.004220725751217746, 0.02060535375352642 ]
model_cnn_all = [0.007053757825066057, 0.002907227609896222,0.002577479906643763, 0.010704988970859306,  0.004943001623336341 ]
majority_vote = [0.08264720854621975, 0.03853642259079844, 0.02533773010834777, 0.021338958792814083, 0.04014444123937523]

test_cnn_5 = [model_cnn_5[0], model_cnn_10[0], model_cnn_15[0], model_cnn_20[0], model_cnn_all[0], majority_vote[0]  ]
test_cnn_10 = [model_cnn_5[1], model_cnn_10[1], model_cnn_15[1], model_cnn_20[1], model_cnn_all[1] , majority_vote[1] ]
test_cnn_15 = [model_cnn_5[2], model_cnn_10[2], model_cnn_15[2], model_cnn_20[2], model_cnn_all[2] , majority_vote[2] ]
test_cnn_20 = [model_cnn_5[3], model_cnn_10[3], model_cnn_15[3], model_cnn_20[3], model_cnn_all[3] , majority_vote[3] ]
test_cnn_all = [model_cnn_5[4], model_cnn_10[4], model_cnn_15[4], model_cnn_20[4], model_cnn_all[4], majority_vote[4]  ]



plt.title('False positive rate (FPR) for prediction of test data\n with CNN trained on different coverages')
ax.bar(x-2*(width/5), test_cnn_5, width/5, label='Test set CNN 3-5X')
ax.bar(x-width/5, test_cnn_10, width/5, label='Test set CNN 6-10X')
ax.bar(x, test_cnn_15, width/5, label='Test set CNN 11-15X')
ax.bar(x+width/5, test_cnn_20, width/5, label='Test set CNN 16-20X')
ax.bar(x+2*(width/5), test_cnn_all, width/5, label='Test set CNN 3-20X')
# sns.color_palette("Set2")
# plt.ylim(0,1)
fig.supylabel('False Positive Rate (%)')
ax.set_xlabel('Coverage of model')
ax.set_xticks(x, labels)
ax.legend()
ax.set_yscale('log')

plt.savefig('Crosstest_CNN.png', bbox_inches="tight", dpi=500)




'''
Plot heatmap DNN crosstest model coverage vs. test data coverage --> nr samples wrong
'''
# data = np.array([[8,6,6,6,5], [19,7,8,8,13], [23,8,8,6,14], [27,8,8,6,15], [16,9,5,3,9]])
# plt.figure(1)
# print(data.shape)
# ax = sns.heatmap(data, annot=True, fmt='d', xticklabels=['3-5X','6-10X','11-15X','16-20X','3-20X'], yticklabels=['3-5X','6-10X','11-15X','16-20X','3-20X'])
# ax.set_ylabel('Model')
# ax.set_xlabel('Coverage of test set')
# ax.set_title('Crosstest DNN models on different coverages in test set - Nr. samples wrong')
# plt.savefig('DNN_crosstest_heatmap.png', bbox_inches="tight", dpi=500)

