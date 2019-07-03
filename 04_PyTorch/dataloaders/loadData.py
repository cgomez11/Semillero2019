#! /usr/bin/env python

# Tutorial for loading your own data
import numpy as np
import matplotlib.pylab as plt

import torch
import torch.nn as nn
from torch.utils.data import Dataset
from torchvision import datasets, transforms, models, utils

from dataloader_csv import myDataset, Rescale

# define batch size
batch_size = 8

# load the dictionaries with your data configuration
# partition has two keys: train and validation
# partition['train'] = ['image_train_1','image_train_2']
# labels has as many keys as instances in partition
# labels['image_train_1'] = 1
partition = np.load('partition_ids.npy').item()
labels = np.load('labels_ids.npy').item()

# define path to your data
data_path =  './hymenoptera_data/'

# call your dataset function
#train_dataset = myDataset(partition['train'], labels, data_path + 'train/', transform = transforms.Compose([Rescale((375, 500)), transforms.ToTensor()]))
train_dataset = myDataset('train_images.csv', data_path + 'train/', transform = transforms.Compose([Rescale((375, 500)), transforms.ToTensor()]))
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size = batch_size, shuffle = True, num_workers = 4)

#val_dataset = myDataset(partition['val'], labels, data_path + 'val/', transform = transforms.Compose([Rescale((375, 500)), transforms.ToTensor()]))
val_dataset = myDataset('val_images.csv', data_path + 'val/', transform = transforms.Compose([Rescale((375, 500)), transforms.ToTensor()]))
val_loader = torch.utils.data.DataLoader(val_dataset, batch_size = batch_size, shuffle = True, num_workers = 4)

# check the size of your datatset
dataset_sizes = {}
dataset_sizes['train'] = len(train_dataset)
dataset_sizes['validation'] = len(val_dataset)
print('training dataset size:', dataset_sizes['train'])
print('Validation dataset size:', dataset_sizes['validation'])

# iterate over the dataloader
for batch_idx, (inputs, targets) in enumerate(train_loader):
    print('Batch: {}, shape input: {}, label: {}'.format(batch_idx, inputs.shape, targets.data))


# Visualize training images
"""
class_names = ['bees', 'ants']

def imshow(inp, title=None):
    #Imshow for Tensor
    inp = inp.numpy().transpose((1, 2, 0))
    plt.imshow(inp)
    if title is not None:
        plt.title(title)
    plt.pause(0.001)  # pause a bit so that plots are updated


# Get a batch of training data
inputs, classes = next(iter(train_loader))

# Make a grid from batch
out = torchvision.utils.make_grid(inputs)

imshow(out, title=[class_names[x] for x in classes])
"""
