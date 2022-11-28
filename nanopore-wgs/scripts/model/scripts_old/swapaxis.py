import h5py
import numpy as np

file = '/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/traintest/chr18_cnn/tune/traintest_chr18_cnn_0.hdf5'

with h5py.File(file) as f:
    x_data = f['x'][()]
    y_data = f['y'][()]
    print(x_data.shape, y_data.shape)

x = x_data[0]
print(x)
print(x.shape)

x_swap = np.swapaxes(x, 0, 2)
print(x_swap.shape)
    
print(x.shape)
x_rot90 = np.rot90(x, k=1, axes=(2, 0))
print(x_rot90.shape)


print(x_data.shape)
x = np.transpose(x_data, (0, 3, 2, 1))
print(x.shape)
