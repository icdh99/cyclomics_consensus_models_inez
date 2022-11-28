import time
start = time.time()
import numpy as np
import h5py
from keras.models import load_model
import sys
import tensorflow as tf

print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
print(tf.config.list_physical_devices('GPU'))
print(tf.config.list_physical_devices('CPU'))

modelname = sys.argv[1]   #'/hpc/compgen/projects/gw_cfdna/snv_qs/lambda_analysis/scripts_cyclomics/models/dnn_lambda_c20_noref.h5'
fastqname = sys.argv[2] #'/hpc/compgen/projects/gw_cfdna/snv_qs/lambda_analysis/scripts_cyclomics/predictions/dnn_noref_runid0_0_bigbam.fa'
hdf5name = sys.argv[3] #'/hpc/compgen/projects/gw_cfdna/snv_qs/lambda_analysis/scripts_cyclomics/runid_c3ceed_0_0_c20.hdf5'

print('model name: ', modelname)
print('fastq name: ', fastqname)
print('hdf5 name: ', hdf5name)

def base_deencode(encoded):
    mapper = {0: "A", 1: "C", 2: "G", 3: "T", 4: "D", 5: "N"}; str = ""
    for i,s in enumerate(encoded): str += mapper[s]  
    seq = "".join(str)
    return seq

def prob_to_phredq(prob, readid):
    if prob >= 0.9999999995:
        return 93
    error = 1 - prob
    phredq = -10 * np.log10(error)
    if phredq > 93: 
        # print(phredq, prob)
        return 93
    # if phredq <= 2: print(f'Low PhredQS: {phredq} in {readid}')
    return phredq 

def phredq_to_ascii(phredq):
    ascii = chr(phredq+33)
    return ascii

model = load_model(modelname)

with open(fastqname, 'w') as fastq:
    fastq.truncate(0)
    with h5py.File(hdf5name) as f:
        keys = f.keys()
        print(f'number of readids: {len(keys)}')
        skip = 0
        t = 0 
        for i,j in enumerate(keys):
            x = f[j][()]
            # print(i, j, x.shape)
            
            # if len(x.shape) != 2:
            #     print(f'readid {j} has incorrect shape {x.shape}')
            #     skip += 1
            #     continue
            try:
                y = model.predict(x, verbose = 0)
                max_scores = np.max(y, axis=1)
                a = np.array([(phredq_to_ascii(round(prob_to_phredq(score, j)))) for score in max_scores])
                qs = ''.join(list(a))
                y_pred_max = y.argmax(axis=1)
                seq = base_deencode(y_pred_max)
                fastq.write(f'@{j}'); fastq.write('\n'); fastq.write(seq); fastq.write('\n'); fastq.write('+'); fastq.write('\n'); fastq.write(qs); fastq.write('\n')
            except Exception as e: 
                print(e)
                print(f'readid {j} has incorrect shape {x.shape}')
                skip += 1


print(f'{skip} readids are skipped because of incorrect size (empty matrix)')
end = time.time()
print("The time of execution is :", end-start)