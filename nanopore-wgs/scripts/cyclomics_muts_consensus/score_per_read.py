import pysam

regions=['region1', 'region2', 'region3', 'region4', 'region5']

with open('cycl_mut_consensus_properties_per_read.csv', 'w') as file:
    file.truncate(0)
    header = ['region', 'cons-readid', 'cons-NM', 'cons-YM', 'cons-YR', 'cons-cigar']
    file.write(','.join(header))
    file.write('\n')

nr_reads_check = 0 
for region in regions:
    bamfile = pysam.AlignmentFile(f'/hpc/compgen/projects/gw_cfdna/snv_qs/nanopore-wgs/data/cyclomics_muts_bam_perregion/consensus/cyclomics_muts_consensus_{region}.bam', 'rb')
    i = 0
    with open('cycl_mut_consensus_properties_per_read.csv', 'a') as file:
        for read in bamfile.fetch('chr17'):
            # print(read.query_name)
            # print(f'NM tag: {read.get_tag("NM")}')
            nm = read.get_tag('NM')
            # print(read.cigarstring)
            if read.has_tag('YM'):
                # print(f'YM tag: {read.get_tag("YM")}')
                # print(f'YR tag: {read.get_tag("YR")}')
                line = [region, read.query_name, str(read.get_tag('NM')), str(read.get_tag('YM')), read.get_tag('YR'), read.cigarstring]
                file.write(','.join(line))
                file.write('\n')
                nr_reads_check += 1

            i += 1

    print(i)

print(nr_reads_check)

