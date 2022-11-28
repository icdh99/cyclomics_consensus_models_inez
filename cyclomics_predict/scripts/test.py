import pysam
import os
import subprocess
os.system('date')


# pos = 7578450
# output = subprocess.getoutput(f'samtools faidx /hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/chm13.draft_v1.1_altv2.fa chr17:{pos}-{pos}')
# print((output))
# print(output.split()[-1])



# with open('chr17.txt', 'r') as f:
#     refseq = f.read().rstrip()

import numpy as np

label = [0,1,2,3,4,5]
# print(label)

# def label_encode(label):
#     label_new = []
#     mapper = {0: "A", 1:"C", 2:"G", 3:"T", 4:"D", 5:"N"}
#     for i, s in enumerate(label): 
#         label_new.append(mapper[i])
#     return label_new  

# print(label_encode(label))

# def base_deencode(encoded):
#     mapper = {0: "A", 1: "C", 2: "G", 3: "T", 4: "D", 5: "I"}; str = ""
#     for i,s in enumerate(encoded): str += mapper[s]  
#     seq = "".join(str)
#     return seq

a = np.ones(50)
# a = [2]*50
print(a)
print(type(a))



def base_encode(base):
    mapper = {0: "A", 1:"C", 2:"G", 3:"T", 4:"D", 5:"N"}
    onehot_encoded = [0]*len(base)
    for i, s in enumerate(base): 
        print(i,int(s))
        onehot_encoded[i] =  mapper[s]                                                              
    return onehot_encoded

print(base_encode(a))
print(base_encode(label))