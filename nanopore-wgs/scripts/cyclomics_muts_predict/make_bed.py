with open('region1.bed', 'w') as f:
    f.truncate(0)
    line = ['chr17', str(7574728), str(7574828)]
    f.write('\t'.join(line))

with open('region2.bed', 'w') as f:
    f.truncate(0)
    line = ['chr17', str(7577651), str(7577788)]
    f.write('\t'.join(line))


with open('region3.bed', 'w') as f:
    f.truncate(0)
    line = ['chr17', str(7577813), str(7577958)]
    f.write('\t'.join(line))


with open('region4.bed', 'w') as f:
    f.truncate(0)
    line = ['chr17', str(7578281), str(7578443)]
    f.write('\t'.join(line))


with open('region5.bed', 'w') as f:
    f.truncate(0)
    line = ['chr17', str(7579211), str(7579352)]
    f.write('\t'.join(line))

