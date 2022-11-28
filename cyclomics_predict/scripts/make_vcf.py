import sys

print(f'all arguments: {sys.argv}')
input = ''.join(sys.argv[3:])
region_nr = sys.argv[1]
region = sys.argv[2]
print(f'sequence: {input}')
print(f'length of sequence: {len(input)}')


region = region.replace('-', ':')
region = region.split(':')
start = int(region[1])
print(start)

with open(f'/hpc/compgen/projects/gw_cfdna/snv_qs/cyclomics_predict/data/vcf_normalref/vcf_{region_nr}.vcf', 'w') as file:
    file.truncate(0)
    file.write('##fileformat=VCFv4.2'); file.write('\n')
    header = ["#CHROM", 'POS', 'ID', 'REF', 'ALT']
    file.write('\t'.join(header))
    file.write('\n')
    for base in input:
        # print(base)
        line = ["chr17", str(start), ".", base, base]
        file.write('\t'.join(line))
        file.write('\n')
        start += 1
    # for pileupcolumn in consensus_file.pileup('chr17', min_base_quality = 0 ):
    #     base = pileupcolumn.get_query_sequences(add_indels=True)[0][0].upper()  # first item of list is first base, first item of base is base in case of indel 'T-1N'
    #     line = ["chr17", str(pileupcolumn.pos), ".", base, base]
    #     

print(start)