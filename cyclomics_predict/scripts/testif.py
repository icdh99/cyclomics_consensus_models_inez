# for i in range(10):
#     # print(i)
#     if i > 2:
#         print(i)
#         if i > 3:
#             print(i)
#     else: 
#         print('a')


seq = ['A', 'G', 'C', 'T-1', 'A+4', 'T', 'G']
print(seq)

for i in range(len(seq)):
    if len(seq[i]) > 1:
        if seq[i][1] == '+': 
            print(seq[i]) 
            print(i)  
            continue  
   
    print(seq[i])
    print(i)
