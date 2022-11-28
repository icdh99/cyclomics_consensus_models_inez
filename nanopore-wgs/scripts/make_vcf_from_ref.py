with open("/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/ref_per_chromosome/chr18_v1.1.txt", "r") as fasta:
    lines = [line.rstrip('\n') for line in fasta]
    header = lines[0]
    print(header)
    seq = ''.join(lines[1:])
    print(len(seq), 'bases')
    print((len(seq)))

start = 50000000 + 200001
end = start + 400000

step = 0

with open(f"/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/ref_per_chromosome/chr18_subset_1.vcf", 'w') as file:
    file.truncate(0)
    file.write('##fileformat=VCFv4.2'); file.write('\n')
    file.write('#CHROM	POS	ID	REF	ALT'); file.write('\n')
    for pos in range(start, end):
        step += 1
        base = seq[pos]
        line = ["chr18", str(pos), ".", base, base]
        file.write("\t".join(line))
        file.write('\n')

print(step)

positions = list(range(start, end))
print(f'number of positions: {len(positions)}')
chunks = [(positions[x:x+10000]) for x in range(0, len(positions), 10000)]
print(len(chunks))
print(len(chunks[0]))

for i, chunk in enumerate(chunks):
    print(i+20, len(chunk))
    with open(f"/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/ref_per_chromosome/chr18_subset_{i+20}.vcf", 'w') as file:
        file.truncate(0)
        file.write('##fileformat=VCFv4.2'); file.write('\n')
        file.write('#CHROM	POS	ID	REF	ALT'); file.write('\n')
        for pos in chunk:
            base = seq[pos]
            line = ["chr18", str(pos), ".", base, base]
            file.write("\t".join(line))
            file.write('\n')

exit()

l_c5 = list(range(start, end, 4))
print(len(l_c5))
chunks_c5 = [(l_c5[x:x+500000]) for x in range(0, len(l_c5), 500000)]
print(len(chunks_c5))
print(len(chunks_c5[0]))
print(chunks_c5[0][0])

for i, chunk in enumerate(chunks_c5):
    print(i, len(chunk))
    with open(f"/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/ref_per_chromosome/chr18_subset_c5/chr18_subset_c5_{i}.vcf", 'w') as file:
        file.truncate(0)
        file.write('##fileformat=VCFv4.2'); file.write('\n')
        file.write('#CHROM	POS	ID	REF	ALT'); file.write('\n')
        for n in chunk: #len(seq)
            base = seq[n]
            line = ["chr18", str(n), ".", base, base]
            file.write("\t".join(line))
            file.write('\n')

l_c10 = list(range(start + 1, end, 4))
print(len(l_c10))
chunks_c10 = [(l_c10[x:x+500000]) for x in range(0, len(l_c10), 500000)]
print(len(chunks_c10))
print(len(chunks_c10[0]))
print(chunks_c10[0][0])

for i, chunk in enumerate(chunks_c10):
    print(i, len(chunk))
    with open(f"/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/ref_per_chromosome/chr18_subset_c10/chr18_subset_c10_{i}.vcf", 'w') as file:
        file.truncate(0)
        file.write('##fileformat=VCFv4.2'); file.write('\n')
        file.write('#CHROM	POS	ID	REF	ALT'); file.write('\n')
        for n in chunk: #len(seq)
            base = seq[n]
            line = ["chr18", str(n), ".", base, base]
            file.write("\t".join(line))
            file.write('\n')

l_c15 = list(range(start + 2, end, 4))
print(len(l_c15))
chunks_c15 = [(l_c15[x:x+500000]) for x in range(0, len(l_c15), 500000)]
print(len(chunks_c15))
print(len(chunks_c15[0]))
print(chunks_c15[0][0])

for i, chunk in enumerate(chunks_c15):
    print(i, len(chunk))
    with open(f"/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/ref_per_chromosome/chr18_subset_c15/chr18_subset_c15_{i}.vcf", 'w') as file:
        file.truncate(0)
        file.write('##fileformat=VCFv4.2'); file.write('\n')
        file.write('#CHROM	POS	ID	REF	ALT'); file.write('\n')
        for n in chunk: #len(seq)
            base = seq[n]
            line = ["chr18", str(n), ".", base, base]
            file.write("\t".join(line))
            file.write('\n')

l_c20 = list(range(start + 3, end, 4))
print(len(l_c20))
chunks_c20 = [(l_c20[x:x+500000]) for x in range(0, len(l_c20), 500000)]
print(len(chunks_c20))
print(len(chunks_c20[0]))
print(chunks_c20[0][0])

for i, chunk in enumerate(chunks_c20):
    print(i, len(chunk))
    with open(f"/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/ref_per_chromosome/chr18_subset_c20/chr18_subset_c20_{i}.vcf", 'w') as file:
        file.truncate(0)
        file.write('##fileformat=VCFv4.2'); file.write('\n')
        file.write('#CHROM	POS	ID	REF	ALT'); file.write('\n')
        for n in chunk: #len(seq)
            base = seq[n]
            line = ["chr18", str(n), ".", base, base]
            file.write("\t".join(line))
            file.write('\n')

exit()
a = 0
b = 0
c = 0
d = 0


count_file = 0 
for i in range(start, end, 4): #len(seq)
    if a%500000 == 0:
        count_file += 1
        print(count_file)
    a += 1
    # base = seq[i]
    # line = ["chr18", str(i + 1), ".", base, base]
    # file.write("\t".join(line))
    # file.write('\n')

exit()
with open("/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/ref_per_chromosome/chr18_subset_c5.vcf", "w") as file:
    file.truncate(0)
    file.write('##fileformat=VCFv4.2'); file.write('\n')
    file.write('#CHROM	POS	ID	REF	ALT'); file.write('\n')
    for i in range(start, end, 4): #len(seq)
        a += 1
        base = seq[i]
        line = ["chr18", str(i + 1), ".", base, base]
        file.write("\t".join(line))
        file.write('\n')

with open("/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/ref_per_chromosome/chr18_subset_c10.vcf", "w") as file:
    file.truncate(0)
    file.write('##fileformat=VCFv4.2'); file.write('\n')
    file.write('#CHROM	POS	ID	REF	ALT'); file.write('\n')
    for i in range(start + 1 , end, 4): #len(seq)
        b += 1
        base = seq[i]
        line = ["chr18", str(i + 1), ".", base, base]
        file.write("\t".join(line))
        file.write('\n')

with open("/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/ref_per_chromosome/chr18_subset_c15.vcf", "w") as file:
    file.truncate(0)
    file.write('##fileformat=VCFv4.2'); file.write('\n')
    file.write('#CHROM	POS	ID	REF	ALT'); file.write('\n')
    for i in range(start + 2 , end, 4): #len(seq)
        c += 1
        base = seq[i]
        line = ["chr18", str(i + 1), ".", base, base]
        file.write("\t".join(line))
        file.write('\n')

with open("/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/ref_per_chromosome/chr18_subset_c20.vcf", "w") as file:
    file.truncate(0)
    file.write('##fileformat=VCFv4.2'); file.write('\n')
    file.write('#CHROM	POS	ID	REF	ALT'); file.write('\n')
    for i in range(start + 3, end, 4): #len(seq)
        d += 1
        base = seq[i]
        line = ["chr18", str(i + 1), ".", base, base]
        file.write("\t".join(line))
        file.write('\n')

print(a)
print(b)
print(c)
print(d)

