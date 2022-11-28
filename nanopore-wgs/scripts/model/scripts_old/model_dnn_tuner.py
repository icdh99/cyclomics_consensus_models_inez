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
if coverage_bin == 5: coverage_list = [3,4,5]
if coverage_bin == 10: coverage_list = [6,7,8,9,10]
if coverage_bin == 15: coverage_list = [11,12,13,14,15]
if coverage_bin == 20: coverage_list = [16,17,18,19,20]

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
                    coverage = coverage_list[i%3]
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

# READ MERGED HDF5 WITH MUTATIONS, CONCATENATE, REMOVE EMPTY ROWS
# with h5py.File(path) as f:
#     # print("Keys of merged hdf5 file: %s" % f.keys())
#     x = f['x'][()]
#     y = f['y'][()]
#     print(f'shape of x1 (mutations): {x.shape}')  
#     print(f'shape of y1 (mutations): {y.shape}')
#     list_of_arrays_x = []
#     list_of_arrays_y = []
#     for i in range(len(x)): list_of_arrays_x.append(x[i])
#     for i in range(len(y)): list_of_arrays_y.append(y[i])
#     print(f'{len(list_of_arrays_x)} arrays are concatenated')
#     x = np.concatenate(list_of_arrays_x, axis = 0)
#     y = np.concatenate(list_of_arrays_y, axis = 0)
#     print(f'shape of concatenated x array (mutations): {x.shape}')
#     print(f'shape of concatenated y array (mutations): {y.shape}')
#     nr_emptyrows = len(np.where(~y.any(axis=1))[0])
#     print(f'number of empty rows that are deleted (mutations): {nr_emptyrows}') 
#     x = np.delete(x, np.where(~y.any(axis=1))[0], axis = 0) 
#     y = np.delete(y, np.where(~y.any(axis=1))[0], axis = 0)
#     print(f'{x.shape[0]} mutated samples')

# MAKE TRAIN/TEST DATASETS
x_trainval, x_test, y_trainval, y_test = train_test_split(x, y, test_size=0.5)
x_trainval = x_trainval.astype("float32") 
x_test = x_test.astype("float32")
y_trainval = y_trainval.astype("uint8") 
y_test = y_test.astype("uint8")

# MODEL ARCHITECTURE
def build_model(hp):
    model = keras.Sequential()
    input_shape = (1134,)
    model.add(tf.keras.Input(shape=input_shape))
    # model.add(layers.Dropout(0.5))
    model.add(layers.Dropout(hp.Float('DO1', min_value = 0.2, max_value = 0.8, step = 0.1)))
    model.add(layers.Dense(500, activation='relu'))
    model.add(layers.Dropout(hp.Float('DO2', min_value = 0.2, max_value = 0.8, step = 0.1)))
    # model.add(layers.Dropout(0.5))
    model.add(layers.Dense(300, activation='relu'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dropout(0.2))
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dropout(0.2))
    model.add(layers.Dense(64, activation='relu'))
    # model.add(layers.Dropout(0.2))
    model.add(layers.Dropout(hp.Float('DOlast', min_value = 0.1, max_value = 0.5, step = 0.1)))
    model.add(layers.Dense(6, activation = 'softmax'))
    lr = 0.001
    opt = keras.optimizers.Adam(learning_rate = lr)
    model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=['accuracy'])
    # print(model.summary())
    return model

# TRAIN AND EVALUATE MODEL
x_train, x_val, y_train, y_val = train_test_split(x_trainval, y_trainval, test_size=0.5)
print(f'{x_train.shape[0]} training samples')
print(f'{x_val.shape[0]} validation samples')
print(f'{x_test.shape[0]} test samples')

filepath = "model-{epoch:02d}.h5"
print(filepath)
model_checkpoint_callback = keras.callbacks.ModelCheckpoint(filepath, save_best_only = True, save_weights_only = False, save_freq = 'epoch')
es = keras.callbacks.EarlyStopping(monitor='val_loss', patience=4, restore_best_weights=True)

tuner = kt.Hyperband(build_model, objective='val_accuracy', max_epochs=30)
tuner.search(x=x_train, y=y_train, validation_data=(x_val, y_val), batch_size = 32, callbacks=[es], epochs=30, verbose=0)

bestHP = tuner.get_best_hyperparameters(num_trials = 1)[0]
print("[INFO] optimal dropout in first layer: {}".format(bestHP.get("DO1")))
print("[INFO] optimal dropout in second layer: {}".format(bestHP.get("DO2")))
print("[INFO] optimal dropout in last layer: {}".format(bestHP.get("DOlast")))
# print("[INFO] optimal learning rate: {:.4f}".format(bestHP.get("learning_rate")))

model = tuner.hypermodel.build(bestHP)
batch_size = 32
epochs = 20
history = model.fit(x_train, y_train, validation_data=(x_val, y_val), batch_size=batch_size, epochs=epochs, verbose=0, callbacks=[model_checkpoint_callback, es])

score = model.evaluate(x_test, y_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])

# PREDICT
y_pred = model.predict(x_test,verbose = 0)
y_pred_max = y_pred.argmax(axis=1)
y_test_max = y_test.argmax(axis=1)

print(np.sum(y_pred_max != y_test_max ))
print(np.count_nonzero(y_pred_max != y_test_max)/len(y_test_max) * 100)

# EVALUATE PREDICTIONS
print('Precision with macro is: ', precision_score(y_test_max, y_pred_max, average = 'macro'))
print('Recall with macro is: ', recall_score(y_test_max, y_pred_max, average = 'macro'))
print('F1 score with macro is: ', f1_score(y_test_max, y_pred_max, average = 'macro'))
print(name_model)

# PLOT LEARNING CURVES
# confusion matrix
def base_encode(base):
    mapper = {0: "A", 1:"C", 2:"G", 3:"T", 4:"D", 5:"N"}
    onehot_encoded = [0]*len(base)
    for i, s in enumerate(base): onehot_encoded[i] =  mapper[s]                                                              
    return onehot_encoded

plt.figure(2)
labels = sklearn.utils.multiclass.unique_labels(y_test.argmax(axis=1), y_pred.argmax(axis=1))
labels = base_encode(labels)
y_test_max = base_encode(y_test.argmax(axis=1))
y_pred_max = base_encode(y_pred.argmax(axis=1))
print(f'labels are: {labels}')
ax = plt.subplot() #fig, axis
cm = sklearn.metrics.confusion_matrix(y_test_max, y_pred_max, labels=labels)
sns.heatmap(cm, annot=True, fmt='g', ax=ax)
ax.set_xticklabels(labels)
ax.set_yticklabels(labels)
ax.set_xlabel('Predicted labels')
ax.set_ylabel("True Labels")
ax.set_title(f'{name_model} - Confusion matrix')
plt.savefig(f'{name_model}_cm.png')

# accuracy
plt.figure(3)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title(f'{name_model} - accuracy')
plt.ylim((0.980, 1))
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.savefig(f'{name_model}_accuracy.png')

# loss
plt.figure(4)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title(f'{name_model} - model loss')
plt.ylim((0, 0.040))
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.savefig(f'{name_model}_loss.png')

end = time.time()
print("The time of execution is :", end-start)