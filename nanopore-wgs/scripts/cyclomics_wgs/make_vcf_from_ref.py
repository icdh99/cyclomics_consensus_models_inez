

# chromosomes = ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr20', 'chr21', 'chr21', 'chrX', 'chrY']

# for chromosome in chromosomes:
#     input_fasta = f'/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_wgs_ref/{chromosome}.fa'


#     with open(input_fasta, "r") as fasta:
#         lines = [line.rstrip('\n') for line in fasta]
#         header = lines[0]
#         print(header)
#         seq = ''.join(lines[1:])
#         print(len(seq), 'bases')
#         print((len(seq)))

#     chunks = [(seq[x:x+5000000]) for x in range(0, len(seq), 5000000)]

#     print(len(chunks))

#     for nr, chunk in enumerate(chunks):
#         output_vcf = f'/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_wgs_vcf/{chromosome}_{nr}.vcf'
#         with open(output_vcf, 'w') as file:
#             file.truncate(0)
#             file.write('##fileformat=VCFv4.2'); file.write('\n')
#             file.write('#CHROM	POS	ID	REF	ALT'); file.write('\n')
#             for pos in range(len(chunk)):
#                 base = chunk[pos]
#                 if base == 'N': continue
#                 line = [chromosome, str(pos), ".", base, base]
#                 file.write("\t".join(line))
#                 file.write('\n')

chromosome = 'chr1'

input_fasta = f'/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_wgs_ref/{chromosome}.fa'

with open(input_fasta, "r") as fasta:
    lines = [line.rstrip('\n') for line in fasta]
    header = lines[0]
    print(header)
    seq = ''.join(lines[1:])
    print(len(seq), 'bases')
    print((len(seq)))

# chunks = [(seq[x:x+5000000]) for x in range(0, len(seq), 5000000)]

# print(len(chunks))

# for nr, chunk in enumerate(chunks):
output_vcf = f'/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_wgs_vcf/{chromosome}.vcf'
with open(output_vcf, 'w') as file:
    file.truncate(0)
    file.write('##fileformat=VCFv4.2'); file.write('\n')
    file.write('#CHROM	POS	ID	REF	ALT'); file.write('\n')
    for pos in range(len(seq)):
        base = seq[pos]
        # if base == 'N': continue
        line = [chromosome, str(pos), ".", base, base]
        file.write("\t".join(line))
        file.write('\n')