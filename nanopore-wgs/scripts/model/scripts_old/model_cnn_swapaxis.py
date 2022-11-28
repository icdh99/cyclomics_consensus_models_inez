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
# import keras_tuner as kt
import datetime

print(f'current time: {datetime.datetime.now()}')

# print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
# print(tf.config.list_physical_devices('GPU'))
# print(tf.config.list_physical_devices('CPU'))

# IN/OUTPUT FILES
path_to_folder = sys.argv[1]
print(f'path to folder: {path_to_folder}')
name_model = sys.argv[2]
print(f'name model: {name_model}')
coverage_bin = int(sys.argv[3])
print(f'coverage bin: {coverage_bin}')

# JOIN MATRICES

if coverage_bin == 5: 
    coverage_list = [3,4,5]
    dropout_1 = 0.3
    dropout_2 = 0.1
    dropout_last = 0.3
if coverage_bin == 10: 
    coverage_list = [6,7,8,9,10]
    dropout_1 = 0.1
    dropout_2 = 0.4
    dropout_last = 0.3
if coverage_bin == 15: 
    coverage_list = [11,12,13,14,15]
if coverage_bin == 20: 
    coverage_list = [16,17,18,19,20]

list_x = []
list_y = []
folder = [os.path.join(path_to_folder, file) for file in os.listdir(path_to_folder)]
i = 0
for file in folder:
    print(file)
    if file.endswith('.hdf5'):
        with h5py.File(file) as f:
            x = f['x'][()]
            y = f['y'][()]
            print(x.shape, y.shape)

            # x = np.swapaxes(x, 1, 3)
            # x = np.rot90(x, k=1, axes=(3, 1))
            # x = np.transpose(x1, (0, 3, 2, 1))

            print(x.shape) # (9993, 6, 9, 21)


            x_list = []
            for i in range(len(x)):
                sample = x[i]
                # print(sample.shape)
                coverage = coverage_list[i%3]
                # print(coverage)
                i += 1
                c = np.resize(sample, (6, 9, coverage))
                # print(c.shape)
                d = c.copy()
                length = d.shape[2]
                to_add = 21 - length
                # print(length, to_add)
                new = np.zeros((6, 9, to_add))
                # print(new.shape)
                q = np.concatenate((d, new), axis=2)
                # print(q.shape)
                x_list.append(q)
                
            x_sample = np.stack(x_list, axis=0)
            # print(x_sample.shape)
            list_x.append(x_sample)
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
def build_model():
    filter_size = (2,2)
    model = keras.Sequential()
    input_shape = (6, 9, 21)
    input_shape = input_shape
    # model.add(layers.Dropout(0.3))
    model.add(layers.Dropout(dropout_1))
    model.add(layers.Conv2D(256, kernel_size=filter_size, padding='same', activation="relu"))
    # model.add(layers.Dropout(0.2))
    model.add(layers.Dropout(dropout_2))
    model.add(layers.Conv2D(1024, kernel_size=filter_size, padding='same', activation="relu"))
    model.add(layers.Dropout(0.2))
    model.add(layers.Conv2D(1024, kernel_size=filter_size, padding='same', activation="relu"))
    model.add(layers.Dropout(0.2))
    model.add(layers.Conv2D(1024, kernel_size=filter_size, padding='same', activation="relu"))
    model.add(layers.Dropout(0.2))
    model.add(layers.Conv2D(1024, kernel_size=filter_size, padding='same', activation="relu"))
    model.add(layers.Flatten())
    # model.add(layers.Dropout(0.5))
    model.add(layers.Dropout(dropout_last))
    model.add(layers.Dense(6, activation="softmax"))
    opt = keras.optimizers.Adam(learning_rate = 0.001)
    model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=["accuracy"])
    return model

# TRAIN AND EVALUATE MODEL
x_train, x_val, y_train, y_val = train_test_split(x_trainval, y_trainval, test_size=0.5)
print(f'{x_train.shape[0]} training samples')
print(f'{x_val.shape[0]} validation samples')
print(f'{x_test.shape[0]} test samples')

filepath = "model-{epoch:02d}.h5"
print(filepath)
model_checkpoint_callback = keras.callbacks.ModelCheckpoint(filepath, save_best_only = True, save_weights_only = False, save_freq = 'epoch')
es = keras.callbacks.EarlyStopping(monitor='val_loss', patience = 4, restore_best_weights = True)

model = build_model()

history = model.fit(x_train, y_train, validation_data=(x_val, y_val), batch_size = 32, epochs = 20, callbacks = [es, model_checkpoint_callback], verbose = 2)
score = model.evaluate(x_test, y_test, verbose=0)
print(model.summary())
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