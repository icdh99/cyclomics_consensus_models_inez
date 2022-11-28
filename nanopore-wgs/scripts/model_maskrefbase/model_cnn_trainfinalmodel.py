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
print(f'path to folder: {path_to_folder}')
name_model = sys.argv[2]
print(f'name model: {name_model}')
coverage_bin = int(sys.argv[3])
print(f'coverage bin: {coverage_bin}')

# JOIN MATRICES

# add dropout parameters for every coverage bin

if coverage_bin == 5: 
    dropout_1 = 0.3
    dropout_2 = 0.3
    dropout_last = 0.1
    coverage_list = [3,4,5]
if coverage_bin == 10: 
    dropout_1 = 0.3
    dropout_2 = 0.1
    dropout_last = 0.3
    coverage_list = [6,7,8,9,10]
if coverage_bin == 15: 
    dropout_1 = 0.4
    dropout_2 = 0.4
    dropout_last = 0.4
    coverage_list = [11,12,13,14,15]
if coverage_bin == 20: 
    dropout_1 = 0.4
    dropout_2 = 0.2
    dropout_last = 0.3
    coverage_list = [16,17,18,19,20]
if coverage_bin == 100: 
    dropout_1 = 0.3
    dropout_2 = 0.4
    dropout_last = 0.2
    coverage_list = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

list_x = []
list_y = []
folder = [os.path.join(path_to_folder, file) for file in os.listdir(path_to_folder)]


def shuffle_rows(array, rows):
    np.random.shuffle(array[rows[0]:rows[1]+1])

    
for file in folder:
    print(file)
    if file.endswith('.hdf5'):
        with h5py.File(file) as f:
            x = f['x'][()]
            y = f['y'][()]
            print(x.shape, y.shape)
            x_list = []
            for i in range(len(x)):
                sample = x[i]
                coverage = coverage_list[i%len(coverage_list)]
                i += 1
                c = np.resize(sample, (coverage + 1, 9, 6))
                d = c.copy()
                length = d.shape[0]
                to_add = 21 - length
                new = np.zeros((to_add, 9, 6))
                q = np.concatenate((d, new), axis=0)
                shuffle_rows(q, [1,21])
                x_list.append(q)
            x_sample = np.stack(x_list, axis=0)
            print(x_sample.shape)
            list_x.append(x_sample)
            list_y.append(y)


print(len(list_x), len(list_y))
x = np.concatenate(list_x, axis=0)
y = np.concatenate(list_y, axis=0)

print(f'shape of concatenated x array: {x.shape}')
print(f'shape of concatenated y array: {y.shape}')

# MAKE TRAIN/TEST DATASETS
# x_trainval, x_test, y_trainval, y_test = train_test_split(x, y, test_size=0.5)
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2)

x_train = x_train.astype("float32") 
x_val = x_val.astype("float32")
y_train = y_train.astype("uint8") 
y_val = y_val.astype("uint8")

# MODEL ARCHITECTURE
def build_model():
    model = keras.Sequential()
    input_shape = (21, 9, 6)
    input_shape = input_shape
    model.add(layers.Dropout(dropout_1))
    model.add(layers.Conv2D(256, kernel_size=(2, 2), padding='same', activation="relu"))
    model.add(layers.Dropout(dropout_2))
    model.add(layers.Conv2D(1024, kernel_size=(2, 2), padding='same', activation="relu"))
    model.add(layers.Dropout(0.2))
    model.add(layers.Conv2D(1024, kernel_size=(2, 2), padding='same', activation="relu"))
    model.add(layers.Dropout(0.2))
    model.add(layers.Conv2D(1024, kernel_size=(2, 2), padding='same', activation="relu"))
    model.add(layers.Dropout(0.2))
    model.add(layers.Conv2D(1024, kernel_size=(2, 2), padding='same', activation="relu"))
    model.add(layers.Flatten())
    model.add(layers.Dropout(dropout_last))
    model.add(layers.Dense(6, activation="softmax"))
    opt = keras.optimizers.Adam(learning_rate = 0.001)
    model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=["accuracy"])
    return model

# TRAIN AND EVALUATE MODEL
# x_train, x_val, y_train, y_val = train_test_split(x_trainval, y_trainval, test_size=0.5)
print(f'{x_train.shape[0]} training samples')
print(f'{x_val.shape[0]} validation samples')
# print(f'{x_test.shape[0]} test samples')

filepath = "model-{epoch:02d}.h5"
print(filepath)
model_checkpoint_callback = keras.callbacks.ModelCheckpoint(filepath, save_best_only = True, save_weights_only = False, save_freq = 'epoch')
es = keras.callbacks.EarlyStopping(monitor='val_loss', patience = 4, restore_best_weights = True)

model = build_model()
history = model.fit(x_train, y_train, validation_data=(x_val, y_val), batch_size = 32, epochs = 20, callbacks = [es, model_checkpoint_callback], verbose = 2)
print(model.summary())
# score = model.evaluate(x_test, y_test, verbose=0)
# print("Test loss:", score[0])
# print("Test accuracy:", score[1])

# # PREDICT
# y_pred = model.predict(x_test,verbose = 0)
# y_pred_max = y_pred.argmax(axis=1)
# y_test_max = y_test.argmax(axis=1)

# print(np.sum(y_pred_max != y_test_max ))
# print(np.count_nonzero(y_pred_max != y_test_max)/len(y_test_max) * 100)

# # EVALUATE PREDICTIONS
# print('Precision with macro is: ', precision_score(y_test_max, y_pred_max, average = 'macro'))
# print('Recall with macro is: ', recall_score(y_test_max, y_pred_max, average = 'macro'))
# print('F1 score with macro is: ', f1_score(y_test_max, y_pred_max, average = 'macro'))
# print(name_model)

# # PLOT LEARNING CURVES
# # confusion matrix
# def base_encode(base):
#     mapper = {0: "A", 1:"C", 2:"G", 3:"T", 4:"D", 5:"N"}
#     onehot_encoded = [0]*len(base)
#     for i, s in enumerate(base): onehot_encoded[i] =  mapper[s]                                                              
#     return onehot_encoded

# plt.figure(2)
# labels = sklearn.utils.multiclass.unique_labels(y_test.argmax(axis=1), y_pred.argmax(axis=1))
# labels = base_encode(labels)
# y_test_max = base_encode(y_test.argmax(axis=1))
# y_pred_max = base_encode(y_pred.argmax(axis=1))
# print(f'labels are: {labels}')
# ax = plt.subplot() #fig, axis
# cm = sklearn.metrics.confusion_matrix(y_test_max, y_pred_max, labels=labels)
# sns.heatmap(cm, annot=True, fmt='g', ax=ax)
# ax.set_xticklabels(labels)
# ax.set_yticklabels(labels)
# ax.set_xlabel('Predicted labels')
# ax.set_ylabel("True Labels")
# ax.set_title(f'{name_model} - Confusion matrix')
# plt.savefig(f'{name_model}_cm.png')

# # accuracy
# plt.figure(3)
# plt.plot(history.history['accuracy'])
# plt.plot(history.history['val_accuracy'])
# plt.title(f'{name_model} - accuracy')
# plt.ylim((0.980, 1))
# plt.ylabel('accuracy')
# plt.xlabel('epoch')
# plt.legend(['train', 'test'], loc='upper left')
# plt.savefig(f'{name_model}_accuracy.png')

# # loss
# plt.figure(4)
# plt.plot(history.history['loss'])
# plt.plot(history.history['val_loss'])
# plt.title(f'{name_model} - model loss')
# plt.ylim((0, 0.040))
# plt.ylabel('loss')
# plt.xlabel('epoch')
# plt.legend(['train', 'test'], loc='upper left')
# plt.savefig(f'{name_model}_loss.png')

end = time.time()
print("The time of execution is :", end-start)