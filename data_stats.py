# This file plots a histogram of how many times each label appears in the train.txt file

import matplotlib.pyplot as plt
import numpy as np

file= "Both_splits/both_45_45_10_#1/val.txt"
# Load the train.txt file
with open(file, 'r') as f:
    train_labels = f.readlines()

train_labels = [int(label.strip().split(" ")[1]) for label in train_labels]

# Count the number of occurrences of each label
unique_labels, label_counts = np.unique(train_labels, return_counts=True)

# Plot the histogram
plt.bar(unique_labels, label_counts)
plt.title('Label Histogram')
plt.xlabel('Label')
plt.ylabel('Count')
plt.savefig("both_histogram.png")

