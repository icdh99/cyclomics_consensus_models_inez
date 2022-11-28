import time
start = time.time()

ref = '/hpc/compgen/GENOMES/CHM13_t2t_v2/chm13v2.0.fa'
seq = ''
ref_chr17 = '/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/ref_per_chromosome/chr17_v2.txt'
with open(ref, 'r') as fp:
    with open(ref_chr17, 'w') as fo:
        # for line in iter(fp.readline, '>chr17\n'):
            
        for line in iter(fp.readline, '>chr17 CP068261.2 Homo sapiens isolate CHM13 chromosome 17\n'):  
            pass
        fo.write('>chr17\n')
        # for line in iter(fp.readline, '>chr18\n'):
        for line in iter(fp.readline, '>chr18 CP068260.2 Homo sapiens isolate CHM13 chromosome 18\n'):
            # print(type(line.rstrip()))
            seq += line.rstrip()
            fo.write(line.upper())
    print(len(seq))

# ref = '/hpc/compgen/GENOMES/CHM13_t2t/chm13.draft_v1.1.fa'
# seq = ''
# ref_chr18 = '/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/ref_per_chromosome/chr18_v1.1.txt'
# with open(ref, 'r') as fp:
#     with open(ref_chr18, 'w') as fo:
#         for line in iter(fp.readline, '>chr18\n'):
#             pass
#         fo.write('>chr18\n')
#         for line in iter(fp.readline, '>chr19\n'):
#             # print(type(line.rstrip()))
#             seq += line.rstrip()
#             fo.write(line)
#     print(len(seq))



end = time.time()
print(f'time passed: {end-start}')




