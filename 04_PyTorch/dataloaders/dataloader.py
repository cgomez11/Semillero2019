#! /usr/bin/env python

# Tutorial for creating your own dataloader function

# Link to download sample data: https://download.pytorch.org/tutorial/hymenoptera_data.zip
import os
import pandas  as pd
from skimage import io, transform

import torch
import torch.nn as nn
from torch.utils.data import Dataset

# Dataset class
class myDataset(Dataset):
  'Characterizes a dataset for PyTorch'
  def __init__(self, list_IDs, labels, data_path, transform=None):
        super(myDataset, self).__init__()
        'Initialization'
        self.labels = labels
        self.list_IDs = list_IDs
        self.transform = transform
        self.data_path = data_path

  def __len__(self):
        'Denotes the total number of samples'
        return len(self.list_IDs)

  def __getitem__(self, index):
        'Generates one sample of data'
        ID = self.list_IDs[index]
        # Load data and get label
        label = self.labels[ID]
        image = io.imread(self.data_path + ID)
        image = transform.resize(image, (375,500))
        if self.transform:
            image = self.transform(image)
        return image, label
    
