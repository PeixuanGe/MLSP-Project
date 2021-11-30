# MLSP-Project
Machine Learning for Signal Processing Project
Professor: Najim Dehak


# Project Topic:
Speaker Recognition Task Using Convolutional Neural Network (CNN) and
Recurrent Neural Network (RNN) Models Based on MFCC Features

# Team members:
Peixuan Ge, Jiwei Zou, Deming (Remus) Li
pge3@jh.edu , jzou13@jh.edu , dli90@jh.edu

# Dataset:
VoxCeleb1
“VoxCeleb is an audio-visual dataset consisting of short clips of human speech,
extracted from interview videos uploaded to YouTube” [1]
(Including 1251 speaker identities with 145,265 utterances)
https://www.robots.ox.ac.uk/~vgg/data/voxceleb/vox1.html [1]

# Models:
Resnet34_mfcc.pth - trained ResNet 34 network using MFCC features, can use Resnet34_mfcc.ipynb to import and test

Resnet34_spectro.pth - trained ResNet 34 network using Spectrogram features, can use ResNet34_Spectrogram.ipynb to import and test

LSTM_file1_mfcc.pth - trained LSTM network using MFCC features, can use MLSP_LSTM_mfcc.ipynb to import and test

LSTM_file10.pth - trained LSTM network using Spectrogram features, can use MLSP_LSTM.ipynb to import and test

# Preprocessing and Feature extraction functions:
Inside the utils folder

mfcc_fix_length.m - generate fix length mfcc features from the raw wav files

mfcc_100_to_1000_len.m - generate 100, 200 to 1000 length mfcc features from raw wav files

pool.m - helper function for 100, 200 to 1000 length mfcc features

pre_process.m - preprocess helper function for mfcc features

process_test_files.m -  generate test files mfcc features with length based on wav files and create a index file

generate_100_1000_len_split.py - genetrate index files for 100, 200 to 1000 length mfcc features based on the iden_split.txt file form the raw dataset 
