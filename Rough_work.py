import numpy as np
import pandas as pd
input_list = [('R001', 2), ('R002', 9), ('R003', 4), ('R004', 7), ('R005', 6), ('R006', 9), ('R007', 13)]

print_output =[['R007', 'R007', 'R007', 'R007', 'R007'], ['R007', 'R007', 'R007', 'R007', 'R007'], ['R007', 'R007', 'R007', 'R004', 'R004'],
               ['R002', 'R002', 'R002', 'R002', 'R002'], ['R002', 'R002', 'R002', 'R002', 'R005'], ['R006', 'R006', 'R006', 'R006', 'R006'],
               ['R006', 'R006', 'R006', 'R006', 'R001'], ['R004', 'R004', 'R004', 'R004', 'R004'], ['R005', 'R005', 'R005', 'R005', 'R005'],
               ['R003', 'R003', 'R003', 'R003', 'R001']]

W = 200
wt = wt1 = [100, 100, 190]
val = ['R001','R002','R003','R004','R005','R006','R007']
n = len(wt1)

def knapSack(W, wt, wt1, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(wt1[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    res = K[n][W]
    #print(res)
    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == K[i - 1][w]:
            continue
        else:
            print(wt[i - 1])
            res = res - wt1[i - 1]
            w = w - wt[i - 1]
#return [K[n][W], n, W, K]

#knapSack(W, wt, wt1, n)


allocated={}
for i in  input_list:
    allocated[i[0]]=[]


s=64+len(print_output)

for i in print_output:
    for j in range(len(i)):
        position=chr(s)+str(j+1)
        allocated[i[j]].append(position)
    s=s-1

# import pickle
# with open('myfile.txt', 'w') as fp:
#     pickle.dump(allocated, fp)
allocations = []
for key, value in allocated.items():
    allocations.append([key] + value)
pd.DataFrame(allocations).to_csv("myfile.txt",header=None, sep=" ", index=None)
print(allocations)

import os

def get_filepaths(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths

full_file_paths = get_filepaths(r"C:\Users\Jyoti\Documents\Interview docs\Movie_seating_arrangement\Walmart_final_round")
print(full_file_paths)