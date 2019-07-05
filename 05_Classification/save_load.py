# Saving and loading PyTorch models

# 3 core functions:
# torch.save: saves a serialized object to disk. Models, tensors and dictionaries can be saved with this option
# torch.load: deserializes pickled object files to memory. It also facilitates the device to load data into.
# torch.nn.Module.load_state_dict: loads a model’s parameter dictionary using a deserialized state_dict.

# What is a state_dict? 
# Is a Python object dictionary that maps each layer to its parameter tensor. 
# Note that only layers with learnable parameters (convolutional layers, 
# linear layers, etc.) and registered buffers (batchnorm’s running_mean) 
# have entries in the model’s state_dict. Optimizer objects also have a
# state_dict, which contains information about the state and hyperparameters 
# used.

# Example: check the state_dict of the following model
import torch
import torch.nn as nn
import torch.nn.functional as F

# Define model
class TheModelClass(nn.Module):
    def __init__(self):
        super(TheModelClass, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# Initialize model
model = TheModelClass()

# Initialize optimizer
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

# Print model's state_dict
print("Model's state_dict:")
for param_tensor in model.state_dict():
    print(param_tensor, "\t", model.state_dict()[param_tensor].size())

# Print optimizer's state_dict
print("Optimizer's state_dict:")
for var_name in optimizer.state_dict():
    print(var_name, "\t", optimizer.state_dict()[var_name])

# Saving and loading models for inference
# save: it is necessary to save the trained model’s learned parameters.
# use a .pth extension
# torch.save(model.state_dict(), PATH)
# load: 
# model = TheModelClass(*args, **kwargs)
# model.load_state_dict(torch.load(PATH)) 
# model.eval()

# saving and loading a general checkpoint for inference or resume training
# save: .tar extension
torch.save({
            'epoch': epoch,
            'model_state_dict': model.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
            'loss': loss,
            ...
            }, PATH)

# load:
model = TheModelClass(*args, **kwargs)
optimizer = TheOptimizerClass(*args, **kwargs)

checkpoint = torch.load(PATH)
model.load_state_dict(checkpoint['model_state_dict'])
optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
epoch = checkpoint['epoch']
loss = checkpoint['loss']

model.eval()
# - or -
model.train()