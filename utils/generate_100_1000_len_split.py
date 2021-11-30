import os
import torch
import numpy as np
import scipy.io as sio


f = open("test/iden_split.txt", "r")
lines = f.readlines()
f.close()

split_dict = {}
train = 0
train_counter = 0
test_counter = 0
for line in lines:
    strings = line.split(' ')
    set_label = int(strings[0])
    path = 'coeffs/'+ strings[1].replace('wav\n','')
    if set_label == 3: #test
        split_dict[path] = 2
        test_counter += 1
    else:
        split_dict[path] = 1
        train_counter += 1
print(train_counter)
print(test_counter)

train_counter = 0
test_counter = 0
for i in range(1,11):
    f = open("txt/"+ str(i*100) +".txt", "r")
    lines = f.readlines()
    f.close()
    trainfile = open("split_index/"+ str(i*100) +"_train.txt", "w")
    testfile = open("split_index/"+ str(i*100) +"_test.txt", "w")
    for line in lines:
        key = line.replace('csv\n','')
        set_label = split_dict[key]
        strs = line.split('/')[1].replace('id','')
        if set_label == 2: #test
            testfile.write(strs + " " + line)
            test_counter+=1
        else:
            trainfile.write(strs + " " + line)
            train_counter+=1
    trainfile.close()
    testfile.close()

print(train_counter)
print(test_counter)