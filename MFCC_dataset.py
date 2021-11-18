import torch
import numpy as np
from torch.utils.data import Dataset
from numpy import genfromtxt

metadata = './vox1_meta.csv'
data_path = './coeffs/'
split_path = 'iden_split.txt'
file_format = 'csv'

class VoxCeleb1_MFCC(Dataset):
    def __init__(self, is_train=True):
        f = open(split_path, "r")
        lines = f.readlines()
        ids = []
        paths = []
        counter = 0
        for line in lines:
            strings = line.split(' ')
            set_label = int(strings[0])
            if is_train:
                if set_label == 1 or set_label == 2:
                    strings2 = strings[1].split('/')
                    ids.append(int(strings2[0].replace('id',''))-10001)
                    paths.append(strings[1].replace('wav\n', file_format))
                    counter += 1
            else:
                if set_label == 3:
                    strings2 = strings[1].split('/')
                    ids.append(int(strings2[0].replace('id',''))-10001)
                    paths.append(strings[1].replace('wav\n', file_format))
                    counter += 1
        f.close()

        self.ids = ids
        self.paths = paths

        self.data_path = data_path
        self.is_train = is_train

    def __len__(self):
        return len(self.ids)

    def __getitem__(self, idx):
        return torch.from_numpy(np.expand_dims(genfromtxt(data_path + self.paths[idx], delimiter=','), axis=0)),\
               self.ids[idx] #in one line to save memory
