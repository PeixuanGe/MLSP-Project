import os
import numpy as np
directory = './coeffs'

counts = []

total = 0
for filename in os.listdir(directory):
    counter = 0
    for subfoldername in os.listdir(directory + '/' + filename):
        if subfoldername != '.DS_Store' and subfoldername != '._.DS_Store':
            for file in os.listdir(directory + '/' + filename + '/' + subfoldername):
                if file.endswith('.mat'):
                    counter += 1
    if counter == 0:
        print('0 found at' + str(len(counts)+1))
    else:
        print(counter)
    total += counter
    counts.append(counter)

print('total id = ' + str(len(counts)))
print('min num:' + str(min(x for x in counts if x != 0)))
print('max num:' + str(max(counts)))
print('total num: ' + str(total))

f = open("iden_split.txt", "r")
lines = f.readlines()
count = 0
classcounts = [0, 0, 0]
for line in lines:
    strs = line.split(' ')
    classNum = int(strs[0])
    classcounts[classNum-1] += 1
    path = strs[1]
    #print(path)
    count += 1
f.close()
print(classcounts)
print(count)