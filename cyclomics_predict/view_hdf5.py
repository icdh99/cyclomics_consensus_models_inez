import h5py
import sys
import numpy as np
import gzip

file = sys.argv[1]
# file = '/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_normal/train_data_dnn_merged/train_data_dnn_noref_merged_normal_region2_0-10.hdf5'

with h5py.File(file) as f:
    print('file is opened')
    keys = f.keys()
    print(len(keys))
    for i in keys:
        print(i)
        key = i
        break
    x = f[i][()]
    print(x.shape)
#     y = f['y'][()]
    # print(x.shape, y.shape)

# with h5py.File(file) as f:
#     print("Keys of merged hdf5 file: %s" % f.keys())
#     # x = f['x'][()]
#     y = f['y'][()]
#     # print(f'shape of x merged: {x.shape}')
#     print(f'shape of y merged: {y.shape}')
#     # list_of_arrays_x = []
#     list_of_arrays_y = []
#     # for i in range(len(x)): list_of_arrays_x.append(x[i])
#     for i in range(len(y)): list_of_arrays_y.append(y[i])
#     # print(f'{len(list_of_arrays_x)} arrays are concatenated')
#     # x_conc = np.concatenate(list_of_arrays_x, axis = 0)
#     y_conc = np.concatenate(list_of_arrays_y, axis = 0)
#     # print(f'shape of concatenated x array: {x_conc.shape}')
#     print(f'shape of concatenated y array: {y_conc.shape}')

#     nr_emptyrows = len(np.where(~y_conc.any(axis=1))[0])
#     print(f'number of empty rows that are deleted: {nr_emptyrows}') 
#     # x_conc = np.delete(x_conc, np.where(~y_conc.any(axis=1))[0], axis = 0) # ~ means not 
#     y = np.delete(y_conc, np.where(~y_conc.any(axis=1))[0], axis = 0)
#     # print(f'shape of concatenated x array: {x_conc.shape}')
#     print(f'shape of concatenated y array: {y.shape}')



