import time
start = time.time()

seq = ''
with open('/hpc/compgen/GENOMES/CHM13_t2t/chm13.draft_v1.1.fa', 'r') as fp:
    for line in iter(fp.readline, '>chr17\n'):
        pass
    for line in iter(fp.readline, '>chr18\n'):
        # print(type(line.rstrip()))
        seq += line.rstrip()
print(len(seq))

region1 = seq[7574727:7574828]
cons_region1 = 'CACCTGGAGTGAGCCCTGCTCCCCCCTGGCTCCTTCCCAGCCTGGGCATCCTTGAGTTCCAAGGCCTCATTCAGCTCTCGGAACATCTCGAAGCGCTCACG'
# print(cons_region1 == region1)

region2 = seq[7577658:7577787]
cons_region2 = 'CTGAAGGGTGAAATATTCTCCATCCAGTGGTTTCTTCTTTGGCTGGGGAGAGGAGCTGGTGTTGTTGGGCAGTGCTAGGAAAGAGGCAAGGAAAGGTGATAAAAGTGAATCTGAGGCATAACTGCACCC'
# print(cons_region2 == region2)

region3 = seq[7577815:7577956]
cons_region3 = 'CTTGCTTACCTCGCTTAGTGCTCCCTGGGGGCAGCTCGTGGTGAGGCTCCCCTTTCTTGCGGAGATTCTCTTCCTCTGTGCGCCGGTCTCTCCCAGGACAGGCACAAACACGCACCTCAAAGCTGTTCCGTCCCAGTAGAT'
# print(cons_region3 == region3)
# print(region3)
# print(cons_region3)

region4 = seq[7578282:7578442]
cons_region4 = 'AGGGTGGCAAGTGGCTCCTGACCTGGAGTCTTCCAGTGTGATGATGGTGAGGATGGGCCTCCGGTTCATGCCGCCCATGCAGGAACTGTTACACATGTAGTTGTAGTGGATGGTGGTACAGTCAGAGCCAACCTAGGAGATAACACAGGCCCAAGATGAG'
# print(cons_region4 == region4)
# print(region4)
# print(cons_region4)

region5 = seq[7579212:7579351]
cons_region5 = 'GCCTCACAACCTCCGTCATGTGCTGTGACTGCTTGTAGATGGCCATGGCGCGGACGCGGGTGCCGGGCGGGGGTGTGGAATCAACCCACAGCTGCACAGGGCAGGTCTTGGCCAGTTGGCAAAACATCTTGTTGAGGGC'
# print(cons_region5 == region5)
# print(region5)
# print(cons_region5)

print(len(seq))

seq = seq[:7579301] + seq[7579301+1:]
print(len(seq))
seq = seq[:7579250] + 'C' + seq[7579250:]
print(len(seq))
seq = seq[:7579223] + 'T' + seq[7579223:]
print(len(seq))

seq = seq[:7578435] + 'A' + seq[7578435:]
print(len(seq))
seq = seq[:7578378] + seq[7578378+1:]
print(len(seq))
seq = seq[:7578299] + 'G' + seq[7578299:]
print(len(seq))

seq = seq[:7577930] + seq[7577930+1:]
print(len(seq))
seq = seq[:7577890] + 'A' + seq[7577890:]
print(len(seq))
seq = seq[:7577833] + seq[7577833+1:]
print(len(seq))

seq = seq[:7577777] + seq[7577777+1:]
print(len(seq))
seq = seq[:7577720] + 'A' + seq[7577720:]
print(len(seq))
seq = seq[:7577670] + seq[7577670+1:]
print(len(seq))

seq = seq[:7574810] + 'C' + seq[7574810:]
print(len(seq))
seq = seq[:7574795] + seq[7574795+1:]
print(len(seq))
seq = seq[:7574750] + 'A' + seq[7574750:]
print(len(seq))

chunks_seq = [(seq[x:x+60]) for x in range(0, len(seq), 60)]
print(len(chunks_seq))

region1 = seq[7574727:7574828]
cons_region1 = 'CACCTGGAGTGAGCCCTGCTCCCCCCTGGCTCCTTCCCAGCCTGGGCATCCTTGAGTTCCAAGGCCTCATTCAGCTCTCGGAACATCTCGAAGCGCTCACG'
print(cons_region1 == region1)

region2 = seq[7577658:7577787]
cons_region2 = 'CTGAAGGGTGAAATATTCTCCATCCAGTGGTTTCTTCTTTGGCTGGGGAGAGGAGCTGGTGTTGTTGGGCAGTGCTAGGAAAGAGGCAAGGAAAGGTGATAAAAGTGAATCTGAGGCATAACTGCACCC'
print(cons_region2 == region2)

region3 = seq[7577815:7577956]
cons_region3 = 'CTTGCTTACCTCGCTTAGTGCTCCCTGGGGGCAGCTCGTGGTGAGGCTCCCCTTTCTTGCGGAGATTCTCTTCCTCTGTGCGCCGGTCTCTCCCAGGACAGGCACAAACACGCACCTCAAAGCTGTTCCGTCCCAGTAGAT'
print(cons_region3 == region3)
print(region3)
print(cons_region3)

region4 = seq[7578282:7578442]
cons_region4 = 'AGGGTGGCAAGTGGCTCCTGACCTGGAGTCTTCCAGTGTGATGATGGTGAGGATGGGCCTCCGGTTCATGCCGCCCATGCAGGAACTGTTACACATGTAGTTGTAGTGGATGGTGGTACAGTCAGAGCCAACCTAGGAGATAACACAGGCCCAAGATGAG'
print(cons_region4 == region4)
print(region4)
print(cons_region4)

region5 = seq[7579212:7579351]
cons_region5 = 'GCCTCACAACCTCCGTCATGTGCTGTGACTGCTTGTAGATGGCCATGGCGCGGACGCGGGTGCCGGGCGGGGGTGTGGAATCAACCCACAGCTGCACAGGGCAGGTCTTGGCCAGTTGGCAAAACATCTTGTTGAGGGC'
print(cons_region5 == region5)
print(region5)
print(cons_region5)


with open('chm13.draft_v1.1_alt.fa', 'w') as out:
    with open('/hpc/compgen/GENOMES/CHM13_t2t/chm13.draft_v1.1.fa', 'r') as old:
        for line in iter(old.readline, '>chr17\n'):
            out.write(line)
        out.write('>chr17\n')
        for line_new in chunks_seq:
            out.write(line_new)
            out.write('\n')
    with open('/hpc/compgen/GENOMES/CHM13_t2t/chm13.draft_v1.1.fa', 'r') as old:
        for line_new2 in old.readlines()[43261360:]:
            out.write(line_new2)


# # Open File in Read Mode
# file_1 = open("new_ref.fa", 'r')
# file_2 = open('/hpc/compgen/GENOMES/CHM13_t2t/chm13.draft_v1.1.fa', 'r')
 
# print("Comparing files ", " @ " + 'file1.txt', " # " + 'file2.txt', sep='\n')
 
# file_1_line = file_1.readline()
# file_2_line = file_2.readline()
 
# # Use as a COunter
# line_no = 1
 
# print()
 
# with open('new_ref.fa') as file1:
#     with open('/hpc/compgen/GENOMES/CHM13_t2t/chm13.draft_v1.1.fa') as file2:
#         same = set(file1).intersection(file2)
 
# print("Common Lines in Both Files")
 
# # for line in same:
#     # print(line, end='')
 
# print('\n')
# print("Difference Lines in Both Files")
# while file_1_line != '' or file_2_line != '':
 
#     # Removing whitespaces
#     file_1_line = file_1_line.rstrip()
#     file_2_line = file_2_line.rstrip()
#     e = 0
#     # Compare the lines from both file
#     if file_1_line != file_2_line:
#         if file_1_line.startswith('>') or file_2_line.startswith('>'):
       
#             # otherwise output the line on file1 and use @ sign
#             if file_1_line == '':
#                 print("@", "Line-%d" % line_no, file_1_line)
#             else:
#                 print("@-", "Line-%d" % line_no, file_1_line)
                
#             # otherwise output the line on file2 and use # sign
#             if file_2_line == '':
#                 print("#", "Line-%d" % line_no, file_2_line)
#             else:
#                 print("#+", "Line-%d" % line_no, file_2_line)
    
#             # Print a empty line
#             print('a difference')
#             e += 1
            
 
#     # Read the next line from the file
#     file_1_line = file_1.readline()
#     file_2_line = file_2.readline()
 
#     line_no += 1
 
# file_1.close()
# file_2.close()

# print(f'{e} different lines')
end = time.time()
print("The time of execution is :", end-start)




