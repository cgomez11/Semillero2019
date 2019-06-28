#! /usr/bin/env python

# Tutorial for creating your own dataloader function

# Link to download sample data: https://download.pytorch.org/tutorial/hymenoptera_data.zip
import os
import pandas  as pd
from skimage import io, transform

import torch
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
        # image = transform.resize(image, (375,500))
        if self.transform:
            image = self.transform(image)
        return image, label
    
 class Rescale(object):
    """Rescale the image in a sample to a given size.

    Args:
        output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
    """
    def __init__(self, output_size):
        assert isinstance(output_size, (int, tuple))
        self.output_size = output_size

    def __call__(self, X):
        image = X

        h, w = image.shape[:2]
        if isinstance(self.output_size, int):
            if h > w:
                new_h, new_w = self.output_size * h / w, self.output_size
            else:
                new_h, new_w = self.output_size, self.output_size * w / h
        else:
            new_h, new_w = self.output_size

        new_h, new_w = int(new_h), int(new_w)

        img = transform.resize(image, (new_h, new_w), mode='constant')
        return img
