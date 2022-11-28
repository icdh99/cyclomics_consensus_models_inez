import time
start = time.time()
import numpy as np
import h5py
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import sklearn
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, multilabel_confusion_matrix, accuracy_score, confusion_matrix
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os
import keras_tuner as kt
import datetime

print(f'current time: {datetime.datetime.now()}')

print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
print(tf.config.list_physical_devices('GPU'))
print(tf.config.list_physical_devices('CPU'))

# IN/OUTPUT FILES
path_to_folder = sys.argv[1]
name_model = sys.argv[2]
coverage_bin = int(sys.argv[3])

print(f'path to folder: {path_to_folder}')
print(f'name model: {name_model}')
print(f'coverage bin: {coverage_bin}')

# JOIN MATRICES
# list_x = []
# list_y = []
# folder = [os.path.join(path_to_folder, file) for file in os.listdir(path_to_folder)]
# for file in folder:
#     print(file)
#     if file.endswith('.hdf5'):
#         with h5py.File(file) as f:
#             x = f['x'][()]
#             y = f['y'][()]
#             print(x.shape, y.shape)
#             list_x.append(x)
#             list_y.append(y)
# print(len(list_x), len(list_y))
# x = np.concatenate(list_x, axis=0)
# y = np.concatenate(list_y, axis=0)

# print(f'shape of concatenated x array: {x.shape}')
# print(f'shape of concatenated y array: {y.shape}')
if coverage_bin == 5: coverage_list = [3,4,5]
if coverage_bin == 10: coverage_list = [6,7,8,9,10]
if coverage_bin == 15: coverage_list = [11,12,13,14,15]
if coverage_bin == 20: coverage_list = [16,17,18,19,20]
if coverage_bin == 100: coverage_list = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

list_x = []
list_y = []
folder = [os.path.join(path_to_folder, file) for file in os.listdir(path_to_folder)]
for file in folder:
    print(file)
    if file.endswith('.hdf5'):
        with h5py.File(file) as f:
            x = f['x'][()]
            y = f['y'][()]
            print(x.shape, y.shape)

            x_list = []
            coverage = 3
            for i in range(len(x)):
                # print(i)
                row = x[i]
                list_x_sample = []
                sample = np.split(row, 9)
                for array in sample:
                    coverage = coverage_list[i%len(coverage_list)]
                    c = np.reshape(array, (-1, 6))
                    c = np.resize(c, (coverage,6))
                    d = c.copy()
                    d.resize(21,6)
                    e = d.flatten()
                    list_x_sample.append(e)
                x_sample = np.concatenate(list_x_sample, axis=0)
                # print(x_sample.shape)
                # x_list.append(x_sample)

                x_list.append(x_sample)
            x_good = np.stack(x_list, axis=0)
            list_x.append(x_good)
            list_y.append(y)
print(len(list_x), len(list_y))
x = np.concatenate(list_x, axis=0)
y = np.concatenate(list_y, axis=0)

print(f'shape of concatenated x array: {x.shape}')
print(f'shape of concatenated y array: {y.shape}')
# MAKE TRAIN/TEST DATASETS
x_trainval, x_test, y_trainval, y_test = train_test_split(x, y, test_size=0.5)
x_trainval = x_trainval.astype("float32") 
x_test = x_test.astype("float32")
y_trainval = y_trainval.astype("uint8") 
y_test = y_test.astype("uint8")

# MODEL ARCHITECTURE
def build_model():
    model = keras.Sequential()
    input_shape = (1134,)
    model.add(tf.keras.Input(shape=input_shape))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(500, activation='relu'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(300, activation='relu'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dropout(0.2))
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dropout(0.2))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dropout(0.2))
    model.add(layers.Dense(6, activation = 'softmax'))
    # initial_learning_rate = 0.001
    # lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
    #     initial_learning_rate,
    #     decay_steps=100000,
    #     decay_rate=0.96,
    #     staircase=True)
    # lr = hp.Choice("learning_rate", values = [1e-1, 1e-2, 1e-3, 1e-4])
    lr = 0.001
    opt = keras.optimizers.Adam(learning_rate = lr)
    model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=['accuracy'])
    print(model.summary())
    return model

# TRAIN AND EVALUATE MODEL
from sklearn.model_selection import StratifiedKFold
kfold = StratifiedKFold(n_splits=10, shuffle = False, random_state = None)
cvscores_acc = []
cvscores_loss = []
cvscores_nrwrong = []
cvscores_percwrong = []
cvscores_F1 = []

for train, val in kfold.split(x_trainval, y_trainval.argmax(1)):
    es = keras.callbacks.EarlyStopping(monitor='val_loss', patience = 5, restore_best_weights = True)

    model = build_model()
    history = model.fit(x_trainval[train], y_trainval[train], validation_data=(x_trainval[val], y_trainval[val]), batch_size=32, epochs=20, callbacks = [es], verbose=0)
    test_scores = model.evaluate(x_test, y_test, verbose=0)
    print(f"\nTest loss: {test_scores[0]}")
    print(f"Test accuracy: {test_scores[1]}")

    # PREDICT
    y_pred = model.predict(x_test,verbose = 0)
    y_pred_max = y_pred.argmax(axis=1)
    y_test_max = y_test.argmax(axis=1)
    print(np.sum(y_pred_max != y_test_max)/x_test.shape[0]*100)
    print(np.count_nonzero(y_pred_max != y_test_max))

    # EVALUATE PREDICTIONS
    print('Precision with macro is: ', precision_score(y_test_max, y_pred_max, average = 'macro'))
    print('Recall with macro is: ', recall_score(y_test_max, y_pred_max, average = 'macro'))
    print('F1 score with macro is: ', f1_score(y_test_max, y_pred_max, average = 'macro'))
    print(f'accuracy is: {accuracy_score(y_test_max, y_pred_max)}')
    print('\n')
    cvscores_acc.append(test_scores[1])
    cvscores_loss.append(test_scores[0])
    cvscores_nrwrong.append(np.count_nonzero(y_pred_max != y_test_max))
    cvscores_percwrong.append(np.sum(y_pred_max != y_test_max)/x_test.shape[0]*100)
    cvscores_F1.append(f1_score(y_test_max, y_pred_max, average = 'macro'))

print(f'\n 10-fold crossvalidation scores')
print(f'Accuracy: {np.mean(cvscores_acc)} +/- {np.std(cvscores_acc)}')
print(f'Loss: {np.mean(cvscores_loss)} +/- {np.std(cvscores_loss)}')
print(f'Percentage wrong: {np.mean(cvscores_percwrong)} +/- {np.std(cvscores_percwrong)}')
print(f'F1 score: {np.mean(cvscores_F1)} +/- {np.std(cvscores_F1)}')

print(f'\n Raw 10-fold crossvalidation scores')
print(f'Accuracy:{cvscores_acc}')
print(f'Loss: {cvscores_loss}')
print(f'Percentage wrong: {cvscores_percwrong}')
print(f'F1 score: {cvscores_F1}')
print(f'Nr. of samples wrong: {cvscores_nrwrong}')

end = time.time()
print("The time of execution is :", end-start)


