import h5py
import os
import numpy as np
from datetime import datetime

# MERGE CNN
print(datetime.now())
folder = '/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_normal/train_data_cnn'
merged_name = 'train_data_cnn_noref_merged_normal_region2_0-10.hdf5'
nr_samples = 500 

print(folder, merged_name)

with h5py.File(f"{folder}/{merged_name}", "w") as f_dst:
    h5files = [f for f in os.listdir(f'{folder}') if f.endswith(".hdf5")]
    h5files.remove(f'{merged_name}')
    print(f'files that will be merged: {len(h5files)}')
    print(len(h5files))
    dsetx = f_dst.create_dataset("x", shape=(len(h5files), nr_samples, 21, 9, 6)) 
    dsety = f_dst.create_dataset("y", shape=(len(h5files), nr_samples, 6))
    t = 0
    for i, filename in enumerate(h5files):  
        with h5py.File(f'{folder}/{filename}') as f_src:
            dsetx[t] = f_src['x'][()]       
            dsety[t] = f_src['y'][()]
            t += 1
print(f'{t} files are merged')

# MERGE DNN
# folder = '/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/train_data_dnn'
# merged_name = 'train_data_dnn_ref_merged_insaltv2_0-10.hdf5'
folder = '/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/data_normal/train_data_dnn'
merged_name = 'train_data_dnn_noref_merged_normal_region2_0-10.hdf5'
nr_samples = 500 
print(datetime.now())
print(folder, merged_name)

with h5py.File(f"{folder}/{merged_name}", "w") as f_dst:
    h5files = [f for f in os.listdir(f'{folder}') if f.endswith(".hdf5")]
    h5files.remove(f'{merged_name}')
    print(f'files that will be merged: {len(h5files)}')
    print(len(h5files))
    dsetx = f_dst.create_dataset("x", shape=(len(h5files), nr_samples, 1134)) 
    dsety = f_dst.create_dataset("y", shape=(len(h5files), nr_samples, 6))
    t = 0
    for i, filename in enumerate(h5files):
        with h5py.File(f'{folder}/{filename}') as f_src:
            dsetx[t] = f_src['x'][()]      
            dsety[t] = f_src['y'][()]
            t += 1
print(f'{t} files are merged')