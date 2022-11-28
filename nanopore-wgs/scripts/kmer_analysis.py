import time
start = time.time()
import random
from collections import defaultdict

file = '/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/ref_per_chromosome/chr18_v1.1.txt'
with open(file, 'r') as f: 
    lines = [line.rstrip('\n') for line in f]
    header = lines[0]; 
    # print(header)
    refseq = ''.join(lines[1:])

print(f'number of bases: {len(refseq)}')

# all forward positions on chr18
d = defaultdict(int)
for i in range(3, len(refseq)-3):
    kmer = refseq[i-3:i+4]
    d[kmer] += 1

keys_list_chr18=list(d.keys())
print(f'number of entries in kmer dictionary: {len(d)}')

# read in sequence of chr17
file = '/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/ref_per_chromosome/chr17_v1.1.txt'
with open(file, 'r') as f: 
    lines = [line.rstrip('\n') for line in f]
    header = lines[0]; 
    # print(header)
    ref17 = ''.join(lines[1:])

# kmers on genomic region of tp53
ref_subset = ref17[7574000:7580000]
d_tp53 = defaultdict(int)
for i in range(3, len(ref_subset)-3):
    kmer = ref_subset[i-3:i+4]
    d_tp53[kmer] += 1
keys_list_tp53=list(d_tp53.keys())


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