import time
start = time.time()
import random
from collections import defaultdict

file = '/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/ref_per_chromosome/chr18_v1.1.txt'

with open(file, 'r') as f: 
    lines = [line.rstrip('\n') for line in f]
    header = lines[0]; 
    ref_chr18 = ''.join(lines[1:])
print(f'number of bases of complete chromosome 18: {len(ref_chr18)}')

# print(f'forward kmers for complete chromosome 18')
# # all forward positions on chr18
# # 3mer
# d = defaultdict(int)
# for i in range(1, len(ref_chr18)-1):
#     kmer = ref_chr18[i-1:i+2]
#     d[kmer] += 1
# keys_list_chr18=list(d.keys())
# print(f'number of entries in kmer dictionary 3mer: {len(d)}')
# # 5mer
# d = defaultdict(int)
# for i in range(2, len(ref_chr18)-2):
#     kmer = ref_chr18[i-2:i+3]
#     d[kmer] += 1
# keys_list_chr18=list(d.keys())
# print(f'number of entries in kmer dictionary 5mer: {len(d)}')
# # 7mer
# d = defaultdict(int)
# for i in range(3, len(ref_chr18)-3):
#     kmer = ref_chr18[i-3:i+4]
#     d[kmer] += 1
# keys_list_chr18=list(d.keys())
# print(f'number of entries in kmer dictionary 7mer: {len(d)}')
# # 9mer
# d = defaultdict(int)
# for i in range(4, len(ref_chr18)-4):
#     kmer = ref_chr18[i-4:i+5]
#     d[kmer] += 1
# keys_list_chr18=list(d.keys())
# print(f'number of entries in kmer dictionary 9mer: {len(d)}')

print('\n')


# hyperparamater optimization region of chr18
# 7mer
ref_subset_hypopt = ref_chr18[50000000:50100000]
d_hypopt = defaultdict(int)
for i in range(3, len(ref_subset_hypopt)-3):
    kmer = ref_subset_hypopt[i-3:i+4]
    d_hypopt[kmer] += 1
keys_list_hypopt=list(d_hypopt.keys())
print(f'forward kmers for hyperparamater optimization region')
# all forward positions on hyp opt region chr18
# 3mer
d = defaultdict(int)
for i in range(1, len(ref_subset_hypopt)-1):
    kmer = ref_subset_hypopt[i-1:i+2]
    d[kmer] += 1
keys_list_chr18_hypopt_3mer=list(d.keys())
print(f'number of entries in kmer dictionary 3mer: {len(d)}')
# 5mer
d = defaultdict(int)
for i in range(2, len(ref_subset_hypopt)-2):
    kmer = ref_subset_hypopt[i-2:i+3]
    d[kmer] += 1
keys_list_chr18_hypopt_5mer=list(d.keys())
print(f'number of entries in kmer dictionary 5mer: {len(d)}')
# 7mer
d = defaultdict(int)
for i in range(3, len(ref_subset_hypopt)-3):
    kmer = ref_subset_hypopt[i-3:i+4]
    d[kmer] += 1
keys_list_chr18_hypopt_7mer=list(d.keys())
print(f'number of entries in kmer dictionary 7mer: {len(d)}')
# 9mer
d = defaultdict(int)
for i in range(4, len(ref_subset_hypopt)-4):
    kmer = ref_subset_hypopt[i-4:i+5]
    d[kmer] += 1
keys_list_chr18_hypopt_9mer=list(d.keys())
print(f'number of entries in kmer dictionary 9mer: {len(d)}')
print('\n')

# train region of chr18
# 7mer
ref_subset_train = ref_chr18[50100001:50400000]
print(f'forward kmers for train region')
# 3mer
d = defaultdict(int)
for i in range(1, len(ref_subset_train)-1):
    kmer = ref_subset_train[i-1:i+2]
    d[kmer] += 1
keys_list_chr18_train_3mer=list(d.keys())
print(f'number of entries in kmer dictionary 3mer: {len(d)}')
# 5mer
d = defaultdict(int)
for i in range(2, len(ref_subset_train)-2):
    kmer = ref_subset_train[i-2:i+3]
    d[kmer] += 1
keys_list_chr18_train_5mer=list(d.keys())
print(f'number of entries in kmer dictionary 5mer: {len(d)}')
# 7mer
d = defaultdict(int)
for i in range(3, len(ref_subset_train)-3):
    kmer = ref_subset_train[i-3:i+4]
    d[kmer] += 1
keys_list_chr18_train_7mer=list(d.keys())
print(f'number of entries in kmer dictionary 7mer: {len(d)}')
# 9mer
d = defaultdict(int)
for i in range(4, len(ref_subset_train)-4):
    kmer = ref_subset_train[i-4:i+5]
    d[kmer] += 1
keys_list_chr18_train_9mer=list(d.keys())
print(f'number of entries in kmer dictionary 9mer: {len(d)}')
print('\n')

# test region of chr18, forward kmers
ref_subset_test = ref_chr18[50400001:50600000]
print(f'forward kmers for test region')
# 3mer
d = defaultdict(int)
for i in range(1, len(ref_subset_test)-1):
    kmer = ref_subset_test[i-1:i+2]
    d[kmer] += 1
keys_list_chr18_test_3mer=list(d.keys())
print(f'number of entries in kmer dictionary 3mer: {len(d)}')
# 5mer
d = defaultdict(int)
for i in range(2, len(ref_subset_test)-2):
    kmer = ref_subset_test[i-2:i+3]
    d[kmer] += 1
keys_list_chr18_test_5mer=list(d.keys())
print(f'number of entries in kmer dictionary 5mer: {len(d)}')
# 7mer
d = defaultdict(int)
for i in range(3, len(ref_subset_test)-3):
    kmer = ref_subset_test[i-3:i+4]
    d[kmer] += 1
keys_list_chr18_test_7mer=list(d.keys())
print(f'number of entries in kmer dictionary 7mer: {len(d)}')
# 9mer
d = defaultdict(int)
for i in range(4, len(ref_subset_test)-4):
    kmer = ref_subset_test[i-4:i+5]
    d[kmer] += 1
keys_list_chr18_test_9mer=list(d.keys())
print(f'number of entries in kmer dictionary 9mer: {len(d)}')
print('\n')

print(len(list(set(keys_list_chr18_train_3mer) & set(keys_list_chr18_test_3mer))))
print(len(list(set(keys_list_chr18_train_5mer) & set(keys_list_chr18_test_5mer))))
print(len(list(set(keys_list_chr18_train_7mer) & set(keys_list_chr18_test_7mer))))
print(len(list(set(keys_list_chr18_train_9mer) & set(keys_list_chr18_test_9mer))))
print('\n')
print(len(list(set(keys_list_chr18_train_3mer) & set(keys_list_chr18_hypopt_3mer))))
print(len(list(set(keys_list_chr18_train_5mer) & set(keys_list_chr18_hypopt_5mer))))
print(len(list(set(keys_list_chr18_train_7mer) & set(keys_list_chr18_hypopt_7mer))))
print(len(list(set(keys_list_chr18_train_9mer) & set(keys_list_chr18_hypopt_9mer))))
print('\n')
print(len(list(set(keys_list_chr18_test_3mer) & set(keys_list_chr18_hypopt_3mer))))
print(len(list(set(keys_list_chr18_test_5mer) & set(keys_list_chr18_hypopt_5mer))))
print(len(list(set(keys_list_chr18_test_7mer) & set(keys_list_chr18_hypopt_7mer))))
print(len(list(set(keys_list_chr18_test_9mer) & set(keys_list_chr18_hypopt_9mer))))


# read in sequence of chr17
file = '/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/ref_per_chromosome/chr17_v1.1.txt'
with open(file, 'r') as f: 
    lines = [line.rstrip('\n') for line in f]
    header = lines[0]; 
    # print(header)
    ref_chr17 = ''.join(lines[1:])

# kmers on genomic region of tp53
print(f'\nchromosome 17 region 1')
ref_subset_region1 = ref_chr17[7574728:7574828]
d_tp53_region1_3mer = defaultdict(int)
for i in range(1, len(ref_subset_region1)-1):
    kmer = ref_subset_region1[i-1:i+2]
    d_tp53_region1_3mer[kmer] += 1
keys_list_tp53_region1_3mer=list(d_tp53_region1_3mer.keys())
d_tp53_region1_5mer = defaultdict(int)
for i in range(2, len(ref_subset_region1)-2):
    kmer = ref_subset_region1[i-2:i+3]
    d_tp53_region1_5mer[kmer] += 1
keys_list_tp53_region1_5mer=list(d_tp53_region1_5mer.keys())
d_tp53_region1_7mer = defaultdict(int)
for i in range(3, len(ref_subset_region1)-3):
    kmer = ref_subset_region1[i-3:i+4]
    d_tp53_region1_7mer[kmer] += 1
keys_list_tp53_region1_7mer=list(d_tp53_region1_7mer.keys())
d_tp53_region1_9mer = defaultdict(int)
for i in range(4, len(ref_subset_region1)-4):
    kmer = ref_subset_region1[i-4:i+5]
    d_tp53_region1_9mer[kmer] += 1
keys_list_tp53_region1_9mer=list(d_tp53_region1_9mer.keys())
print(f'number of entries in kmer dictionary 3mer: {len(keys_list_tp53_region1_3mer)}')
print(f'number of entries in kmer dictionary 5mer: {len(keys_list_tp53_region1_5mer)}')
print(f'number of entries in kmer dictionary 7mer: {len(keys_list_tp53_region1_7mer)}')
print(f'number of entries in kmer dictionary 9mer: {len(keys_list_tp53_region1_9mer)}')

# region 3
print(f'\nchromosome 17 region 3')
ref_subset_region3 = ref_chr17[7577813:7577958]
d_tp53_region3_3mer = defaultdict(int)
for i in range(1, len(ref_subset_region3)-1):
    kmer = ref_subset_region3[i-1:i+2]
    d_tp53_region3_3mer[kmer] += 1
keys_list_tp53_region3_3mer=list(d_tp53_region3_3mer.keys())

d_tp53_region3_5mer = defaultdict(int)
for i in range(2, len(ref_subset_region3)-2):
    kmer = ref_subset_region3[i-2:i+3]
    d_tp53_region3_5mer[kmer] += 1
keys_list_tp53_region3_5mer=list(d_tp53_region3_5mer.keys())

d_tp53_region3_7mer = defaultdict(int)
for i in range(3, len(ref_subset_region3)-3):
    kmer = ref_subset_region3[i-3:i+4]
    d_tp53_region3_7mer[kmer] += 1
keys_list_tp53_region3_7mer=list(d_tp53_region3_7mer.keys())

d_tp53_region3_9mer = defaultdict(int)
for i in range(4, len(ref_subset_region3)-4):
    kmer = ref_subset_region3[i-4:i+5]
    d_tp53_region3_9mer[kmer] += 1
keys_list_tp53_region3_9mer=list(d_tp53_region3_9mer.keys())
print(f'number of entries in kmer dictionary 3mer: {len(keys_list_tp53_region3_3mer)}')
print(f'number of entries in kmer dictionary 5mer: {len(keys_list_tp53_region3_5mer)}')
print(f'number of entries in kmer dictionary 7mer: {len(keys_list_tp53_region3_7mer)}')
print(f'number of entries in kmer dictionary 9mer: {len(keys_list_tp53_region3_9mer)}')

# region 4
print(f'\nchromosome 17 region 4')
ref_subset_region4 = ref_chr17[7578281:7578443]
d_tp53_region4_3mer = defaultdict(int)
for i in range(1, len(ref_subset_region4)-1):
    kmer = ref_subset_region4[i-1:i+2]
    d_tp53_region4_3mer[kmer] += 1
keys_list_tp53_region4_3mer=list(d_tp53_region4_3mer.keys())

d_tp53_region4_5mer = defaultdict(int)
for i in range(2, len(ref_subset_region4)-2):
    kmer = ref_subset_region4[i-2:i+3]
    d_tp53_region4_5mer[kmer] += 1
keys_list_tp53_region4_5mer=list(d_tp53_region4_5mer.keys())

d_tp53_region4_7mer = defaultdict(int)
for i in range(3, len(ref_subset_region4)-3):
    kmer = ref_subset_region4[i-3:i+4]
    d_tp53_region4_7mer[kmer] += 1
keys_list_tp53_region4_7mer=list(d_tp53_region4_7mer.keys())

d_tp53_region4_9mer = defaultdict(int)
for i in range(4, len(ref_subset_region4)-4):
    kmer = ref_subset_region4[i-4:i+5]
    d_tp53_region4_9mer[kmer] += 1
keys_list_tp53_region4_9mer=list(d_tp53_region4_9mer.keys())
print(f'number of entries in kmer dictionary 3mer: {len(keys_list_tp53_region4_3mer)}')
print(f'number of entries in kmer dictionary 5mer: {len(keys_list_tp53_region4_5mer)}')
print(f'number of entries in kmer dictionary 7mer: {len(keys_list_tp53_region4_7mer)}')
print(f'number of entries in kmer dictionary 9mer: {len(keys_list_tp53_region4_9mer)}')

# region 5
print(f'\nchromosome 17 region 5')
ref_subset_region5 = ref_chr17[7579211:7579352]
d_tp53_region5_3mer = defaultdict(int)
for i in range(1, len(ref_subset_region5)-1):
    kmer = ref_subset_region5[i-1:i+2]
    d_tp53_region5_3mer[kmer] += 1
keys_list_tp53_region5_3mer=list(d_tp53_region5_3mer.keys())

d_tp53_region5_5mer = defaultdict(int)
for i in range(2, len(ref_subset_region5)-2):
    kmer = ref_subset_region5[i-2:i+3]
    d_tp53_region5_5mer[kmer] += 1
keys_list_tp53_region5_5mer=list(d_tp53_region5_5mer.keys())

d_tp53_region5_7mer = defaultdict(int)
for i in range(3, len(ref_subset_region5)-3):
    kmer = ref_subset_region5[i-3:i+4]
    d_tp53_region5_7mer[kmer] += 1
keys_list_tp53_region5_7mer=list(d_tp53_region5_7mer.keys())

d_tp53_region5_9mer = defaultdict(int)
for i in range(4, len(ref_subset_region5)-4):
    kmer = ref_subset_region5[i-4:i+5]
    d_tp53_region5_9mer[kmer] += 1
keys_list_tp53_region5_9mer=list(d_tp53_region5_9mer.keys())

print(f'number of entries in kmer dictionary 3mer: {len(keys_list_tp53_region5_3mer)}')
print(f'number of entries in kmer dictionary 5mer: {len(keys_list_tp53_region5_5mer)}')
print(f'number of entries in kmer dictionary 7mer: {len(keys_list_tp53_region5_7mer)}')
print(f'number of entries in kmer dictionary 9mer: {len(keys_list_tp53_region5_9mer)}')

print('\n')
print('region 1 overlap with test set')
print(len(list(set(keys_list_chr18_train_3mer) & set(keys_list_tp53_region1_3mer))))
print(len(list(set(keys_list_chr18_train_5mer) & set(keys_list_tp53_region1_5mer))))
print(len(list(set(keys_list_chr18_train_7mer) & set(keys_list_tp53_region1_7mer))))
print(len(list(set(keys_list_chr18_train_9mer) & set(keys_list_tp53_region1_9mer))))

print('region 3 overlap with test set')
print(len(list(set(keys_list_chr18_train_3mer) & set(keys_list_tp53_region3_3mer))))
print(len(list(set(keys_list_chr18_train_5mer) & set(keys_list_tp53_region3_5mer))))
print(len(list(set(keys_list_chr18_train_7mer) & set(keys_list_tp53_region3_7mer))))
print(len(list(set(keys_list_chr18_train_9mer) & set(keys_list_tp53_region3_9mer))))

print('region 4 overlap with test set')
print(len(list(set(keys_list_chr18_train_3mer) & set(keys_list_tp53_region4_3mer))))
print(len(list(set(keys_list_chr18_train_5mer) & set(keys_list_tp53_region4_5mer))))
print(len(list(set(keys_list_chr18_train_7mer) & set(keys_list_tp53_region4_7mer))))
print(len(list(set(keys_list_chr18_train_9mer) & set(keys_list_tp53_region4_9mer))))

print('region 5 overlap with test set')
print(len(list(set(keys_list_chr18_train_3mer) & set(keys_list_tp53_region5_3mer))))
print(len(list(set(keys_list_chr18_train_5mer) & set(keys_list_tp53_region5_5mer))))
print(len(list(set(keys_list_chr18_train_7mer) & set(keys_list_tp53_region5_7mer))))
print(len(list(set(keys_list_chr18_train_9mer) & set(keys_list_tp53_region5_9mer))))


exit()


start = 50000000   # keep this 446000000
end = start + 600000    

nr_pos = end - start
print(f'nr positions: {nr_pos}')
print(f'start: {start}\t end: {end}')

# position for every kmer 60x 
ref_subset = refseq[start:end]
d = defaultdict(int)
steps = 0
positions = [0]
for i in range(3, len(ref_subset)-3):
    kmer = ref_subset[i-3:i+4]
    # if d[kmer] < 3:
        # if i > positions[-1] + 1000:
    positions.append(i)
    d[kmer] += 1
    steps += 1
keys_list_subset=list(d.keys())



print(f'number of pos: {steps}')
print(f'number unique kmers on chr18: {len(keys_list_chr18)}')
print(f'number of unique kmers of chr18: {len(keys_list_subset)}')
print(f'number of kmers missing in the subset: {len(set(keys_list_chr18)-set(keys_list_subset))}')
# print(f'number of kmers missing in the subset start 3: {(set(keys_list_chr18)-set(keys_list_subset))}')
print(f'are all tp53 kmers present in the subset: {(set(keys_list_tp53).issubset(set(keys_list_subset)))}')


exit()
# kmers between 1,000,000 and 4,000,000
ref_subset = refseq[start:end]
d = defaultdict(int)
for i in range(3, len(ref_subset)-3, 4):
    kmer = ref_subset[i-3:i+4]
    d[kmer] += 1
keys_list_subset=list(d.keys())
print(f'number of entries in subset kmer dictionary start 3: {len(d)}')
print(f'number of kmers missing in the subset start 3: {len(set(keys_list)-set(keys_list_subset))}')
print(f'number of kmers missing in the subset start 3: {(set(keys_list)-set(keys_list_subset))}')
print(f'are all tp53 kmers present in the subset: {set(list(d.keys())).issubset(keys_list_subset)}')


ref_subset = refseq[start:end]
d = defaultdict(int)
for i in range(4, len(ref_subset)-3, 4):
    kmer = ref_subset[i-3:i+4]
    d[kmer] += 1
keys_list_subset=list(d.keys())
print(f'number of entries in subset kmer dictionary start 4: {len(d)}')
print(f'number of kmers missing in the subset start 4: {len(set(keys_list)-set(keys_list_subset))}')
print(f'number of kmers missing in the subset start 4: {(set(keys_list)-set(keys_list_subset))}')
print(f'are all tp53 kmers present in the subset: {set(list(d.keys())).issubset(keys_list_subset)}')



ref_subset = refseq[start:end]
d = defaultdict(int)
for i in range(5, len(ref_subset)-3, 4):
    kmer = ref_subset[i-3:i+4]
    d[kmer] += 1
keys_list_subset=list(d.keys())
print(f'number of entries in subset kmer dictionary start 5: {len(d)}')
print(f'number of kmers missing in the subset start 5: {len(set(keys_list)-set(keys_list_subset))}')
print(f'number of kmers missing in the subset start 5: {(set(keys_list)-set(keys_list_subset))}')
print(f'are all tp53 kmers present in the subset: {set(list(d.keys())).issubset(keys_list_subset)}')



ref_subset =refseq[start:end]
d = defaultdict(int)
for i in range(6, len(ref_subset)-3, 4):
    kmer = ref_subset[i-3:i+4]
    d[kmer] += 1
keys_list_subset=list(d.keys())
print(f'number of entries in subset kmer dictionary start 6: {len(d)}')
print(f'number of kmers missing in the subset start 6: {len(set(keys_list)-set(keys_list_subset))}')
print(f'number of kmers missing in the subset start 6: {(set(keys_list)-set(keys_list_subset))}')
print(f'are all tp53 kmers present in the subset: {set(list(d.keys())).issubset(keys_list_subset)}')



# print((set(keys_list)-set(keys_list_subset)))
# print(f'number of kmers missing in the subset: {len(set(keys_list)-set(keys_list_subset))}')


# tp53 = 'GAAGCCAAAGGGTGAAGAGGAATCCCAAAGTTCCAAACAAAAGAAATGCAGGGGGATACGGCCAGGCATTGAAGTCTCATGGAAGCCAGCCCCTCAGGGCAACTGACCGTGCAAGTCACAGACTTGGCTGTCCCAGAATGCAAGAAGCCCAG'
# d = defaultdict(int)
# for i in range(3, len(tp53)-3):
#     kmer = tp53[i-3:i+4]
#     d[kmer] += 1

# # print((set(keys_list)-set(list(d.keys()))))
# print(f'are all tp53 kmers presentset(list(d.keys())).issubset(keys_list_subset))

end = time.time()
print("The time of execution is :", end-start)