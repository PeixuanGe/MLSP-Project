import torch
import numpy as np
from torch.utils.data import Dataset
import scipy.io as sio
#import pandas as pd

metadata = './vox1_meta.csv'
data_path = './coeffs'
split_path = 'iden_split.txt'
file_format = 'mat'

class VoxCeleb1_MFCC(Dataset):
    def __init__(self, is_train=True):
        #csv_file = pd.read_csv(metadata)
        f = open(split_path, "r")
        lines = f.readlines()
        ids = []
        paths = []
        for line in lines:
            strings = line.split(' ')
            set_label = int(strings[0])
            if is_train:
                if set_label == 1 or set_label == 2:
                    paths.append(strings[1].replace('wav\n', file_format))
                    strings2 = strings[1].split('/')
                    ids.append(strings2[0])
            else:
                if set_label == 3:
                    paths.append(strings[1].replace('wav\n', file_format))
                    strings2 = strings[1].split('/')
                    ids.append(strings2[0])
        f.close()

        self.ids = ids
        self.paths = paths

        self.data_path = data_path
        self.is_train = is_train

    def __len__(self):
        return len(self.ids)

    def __getitem__(self, idx):
        label = self.ids[idx]
        raw_mfcc = sio.loadmat(self.paths[idx])
        torch_mfcc = torch.from_numpy(np.array(raw_mfcc['coeff']))
        return torch_mfcc, label
