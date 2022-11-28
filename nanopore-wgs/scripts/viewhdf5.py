import h5py
import os
import numpy as np
from natsort import natsorted

# file = '/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/test_cnnc5.hdf5'
# with h5py.File(file) as p:
#     print(f"Number of keys: {len(p.keys())}")
#     x1 = p['x'][()]
#     print(x1.shape)

# file = '/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/test_cnnc5.hdf5_gzip.hdf5'
# with h5py.File(file) as p:
#     print(f"Number of keys: {len(p.keys())}")
#     x2 = p['x'][()]
#     print(x2.shape)

# print(np.array_equal(x1, x2))

folder = '/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/predict_cyclomics_clean'
folder = '/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_hdf5'

cnn_region1 = 0
cnn_region2 = 0
cnn_region3 = 0
cnn_region4 = 0
cnn_region5 = 0
dnn_region1 = 0
dnn_region2 = 0
dnn_region3 = 0
dnn_region4 = 0
dnn_region5 = 0

paths = [os.path.join(folder, file) for file in os.listdir(folder)]
paths = natsorted(paths)
for file in paths:
    # print(file)
    with h5py.File(file) as p:
        nr = len(p.keys())
        print(f'File: {file}\tNumber of keys: {nr}')
        # a = p.keys()[0
        if 'cnn' in file:
            if 'region1' in file:
                cnn_region1 += nr
            if 'region2' in file:
                cnn_region2 += nr
            if 'region3' in file:
                cnn_region3 += nr
            if 'region4' in file:
                cnn_region4 += nr
            if 'region5' in file:
                cnn_region5 += nr
        if 'dnn' in file:
            if 'region1' in file:
                dnn_region1 += nr
            if 'region2' in file:
                dnn_region2 += nr
            if 'region3' in file:
                dnn_region3 += nr
            if 'region4' in file:
                dnn_region4 += nr
            if 'region5' in file:
                dnn_region5 += nr  

        # for i in p.keys():
        #     a = i 
        # x = p[a][()]
        # print(x.shape)

print(f'cnn region1: {cnn_region1}')
print(f'cnn region2: {cnn_region2}')
print(f'cnn region3: {cnn_region3}')
print(f'cnn region4: {cnn_region4}')
print(f'cnn region5: {cnn_region5}')
print(f'dnn region1: {dnn_region1}')
print(f'dnn region2: {dnn_region2}')
print(f'dnn region3: {dnn_region3}')
print(f'dnn region4: {dnn_region4}')
print(f'dnn region5: {dnn_region5}')