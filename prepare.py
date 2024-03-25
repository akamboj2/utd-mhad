#create annotations that look like kinetics dataset
# e.g. a train and val file formatted as:
# path_to_data_file activity_label_#

import os
import numpy as np

modality = "Both" #"Inertial"  or "RGB"
label_category = "Both" # "PID" or "Action"
base_dir = f"./{modality}_splits/both_80_20_#1"

if not os.path.exists(base_dir):
    os.makedirs(base_dir)

videos = os.listdir(f"./{modality}") if modality not in ["Both"] else os.listdir(f"./Inertial")

# Shuffle the videos using numpy's shuffle function
np.random.shuffle(videos)

# Split the shuffled videos into training and validation sets
train = videos[:int(len(videos) * 0.8)]
val = videos[int(len(videos) * 0.8):]

# Open the train.txt and val.txt files for writing
train_dir = os.path.join(base_dir, "train.txt")
val_dir = os.path.join(base_dir, "val.txt")
train_file = open(train_dir, "w")
val_file = open(val_dir, "w")

for file, split in [(train_file, train), (val_file, val)]:
    for v in split: #v is the video filename
        label_action = v.split("_")[0][1:]  # Extract the action label from the video filename
        label_PID = v.split("_")[1][1:] #RGB/a1_s1_t1_color.avi action 1, subject 1, test 1
        if label_category=="action":
            label = label_action
        elif label_category=="PID":
            label = label_PID
        elif label_category=="Both":
            label = label_action + " " + label_PID
        
        if modality=="Both":
            # Extract the file name without the extension
            v = '_'.join(v.split(".")[0].split("_")[:-1])
            file.write(v + " " + label + "\n")
        else:
            file.write(os.path.join(os.getcwd(), modality, v) + " " + label + "\n")

# Close the train.txt and val.txt files
train_file.close()
val_file.close()
