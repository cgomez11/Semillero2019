#! /usr/bin/env python

import torch

# Introduction to Torch's tensor library

# Tensor: generalization of a matrix that can be indexed in more than 2 dimensions.

# Creating tensors
# torch.tensor(data) creates a torch.Tensor object with the given data.
V_data = [1., 2., 3.] # defined as a list
V = torch.tensor(V_data)
print(V)

# Creates a matrix of size 2x3
M_data = [[1., 2., 3.], [4., 5., 6]] # a list of lists
M = torch.tensor(M_data)
print(M)

# Create a 3D tensor of size 2x2x2.
T_data = [[[1., 2.], [3., 4.]],
          [[5., 6.], [7., 8.]]]
T = torch.tensor(T_data)
print(T)

# Indexing tensors
# Index into V and get a ?
print(V[0])
# Get a Python number from it
print(V[0].item())
# Index into M and get a ?
print(M[0])
# Index into T and get a ?
print(T[0])
# is T[0] equal to T[:,:,0] or T[0,:,:]?

# Note: the default datatype of tensors is Float. A tensor of integer types is Long

# Operations with tensors: https://pytorch.org/docs/stable/torch.html
x = torch.tensor([1., 2., 3.])
y = torch.tensor([4., 5., 6.])
z = x + y
print(z)
print(x * y)
print(x.mean())
print(y.sum())

# Concatenation
# By default, it concatenates along the first axis 
x_1 = torch.randn(2, 5)
y_1 = torch.randn(3, 5)
z_1 = torch.cat([x_1, y_1])
print(z_1)

# Try over columns
x_2 = torch.randn(2, 3)
y_2 = torch.randn(2, 5)

# Try torch.cat([x_1, x_2])

# Reshaping tensors
x = torch.randn(2, 3, 4)
print(x)
print(x.view(2, 12)) # what is the new shape?

print(x.view(2, -1)) # -1: the dimension can be inferred

