import time
start = time.time()
import numpy as np
import h5py
# from sklearn.model_selection import train_test_split
# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras import layers
# import sklearn
# from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, multilabel_confusion_matrix, accuracy_score, confusion_matrix
# from sklearn import metrics
# import matplotlib.pyplot as plt
# import seaborn as sns
# import sys
import os
import datetime

print(f'current time: {datetime.datetime.now()}')


# IN/OUTPUT FILES
# path_to_folder = sys.argv[1]
path_to_folder = '/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/traintest/chr18_dnn'
# name_model = sys.argv[2]

print(f'path to folder: {path_to_folder}')
# print(f'name model: {name_model}')


file = '/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/traintest/traintest_maskedrefbase/chr18_dnn_train/traintest_chr18_dnn_0.hdf5'
with h5py.File(file) as f:
    x = f['x'][()]
    y = f['y'][()]
    print(x.shape, y.shape)

def shuffle_rows(array, rows):
    np.random.shuffle(array[rows[0]:rows[1]+1])

x_list = []
coverage = 6
# for i in range(len(x)):
for i in range(5):
    print(i)
    row = x[i]
    list_x_sample = []
    sample = np.split(row, 9)
    print(len(sample))
    seed = np.random.randint(0,10000)
    print('seed: ', seed)
    for array in sample:
        
        
        np.random.seed(seed)
        print(array.shape)
        # print(array)
        
        c = np.reshape(array, (-1, 6))
        print(c.shape)
        c = np.resize(c, (coverage+1,6))
        print(c.shape)
        d = c.copy()
        d.resize(21,6)
        print(d.shape)
        shuffle_rows(d, [1,21])
        # print(d)
        print(np.where(np.any(d != 0, axis=1)))
        e = d.flatten()
        print(e.shape)
        list_x_sample.append(e)
        
        print('\n')
    print('len x list sample', len(list_x_sample))
    print(list_x_sample[0].shape)
    x_sample = np.concatenate(list_x_sample, axis=0)
    print(x_sample.shape)
    x_list.append(x_sample)
    print('len x list ', len(x_list))


print('\n')
print(len(x_list))
x = np.stack(x_list, axis=0)
print(x.shape)
print(x[0].shape)



# coverage for cnn samples
file = '/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/traintest/traintest_maskedrefbase/traintest_chr18_cnn_0.hdf5'
with h5py.File(file) as f:
    x = f['x'][()]
    y = f['y'][()]
    print(x.shape, y.shape)

print(x[0].shape)
print(y[0].shape)
coverage = 10

x_list = []
print(len(x))
for i in range(len(x)):
    sample = x[i]
    c = np.resize(sample, (coverage+1, 9, 6))
    print(c.shape)
    d = c.copy()

    length = d.shape[0]
    to_add = 21 - length

    new = np.zeros((to_add, 9, 6))
    print(new.shape)
    q = np.concatenate((d, new), axis=0)
    print(q.shape)
    print(q)
    shuffle_rows(q, [1,21])
    print(q.shape)
    print(q)
    print(np.where(np.any(q != 0, axis=1)))
    x_list.append(q)
    break

print('\n')
print(len(x_list))
x = np.stack(x_list, axis=0)
print(x.shape)
exit()

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
    lr = 0.001
    opt = keras.optimizers.Adam(learning_rate = lr)
    model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=['accuracy'])
    print(model.summary())
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