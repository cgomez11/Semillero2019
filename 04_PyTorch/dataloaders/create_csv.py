import os
import csv

'''
This is a toy example of a code to create a csv. It is very simple, you only
need to make a list of the paths to your data and another one to the lables,
turn that into a dict and write it in the csv file.
'''

# Where your data is stored. In this case we assume that the images
# and labels are in different folders
root = '/Path/to/your/data'
images = 'Images'
labels = 'Labels'

# List all files in the folders. Note: this will only store the names of
# the files, not the complete path. If you need the path you can use glob.glob
dataset = os.listdir(os.path.join(root, images))
groundtruth = os.listdir(os.path.join(root, labels))

# Names of the columns that the csv will have
fieldnames = ['Image', 'Label']

# Write everithing in the csv
with open('file_name.csv', 'w') as outcsv:
    writer = csv.DictWriter(outcsv, fieldnames=fieldnames)
    writer.writeheader()

    writer.writerows({fieldnames[0]: im, fieldnames[1]: lb}
                     for im, lb in zip(dataset, groundtruth))
    outcsv.close()
