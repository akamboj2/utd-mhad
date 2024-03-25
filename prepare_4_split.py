#create annotations that look like kinetics dataset
# e.g. a train and val file formatted as:
# path_to_data_file activity_label_#

import os
import numpy as np

modality = "Both" #"Inertial"  or "RGB"
label_category = "Both" # "PID" or "Action"
base_dir = f"./{modality}_splits/both_42.5_42.5_5_10_#1"
if not os.path.exists(base_dir):
    os.makedirs(base_dir)


videos = os.listdir(f"./{modality}") if modality not in ["Both"] else os.listdir(f"./Inertial")

# Shuffle the videos using numpy's shuffle function
np.random.shuffle(videos)

# Split the shuffled videos into training and validation sets
# train_1 = videos[:int(len(videos) * 0.45)]
# train_2 = videos[int(len(videos) * 0.45):int(len(videos) * 0.9)]
# val = videos[int(len(videos) * 0.9):]
train_1 = videos[:int(len(videos) * 0.425)]
train_2 = videos[int(len(videos) * 0.425):int(len(videos) * 0.85)]
val = videos[int(len(videos) * 0.85):int(len(videos) * 0.95)]
test = videos[int(len(videos) * 0.95):]

# Open the train.txt and val.txt files for writing
train_1_dir = os.path.join(base_dir, "train.txt")
train_2_dir = os.path.join(base_dir, "train_2.txt")
val_dir = os.path.join(base_dir, "val.txt")
test_dir = os.path.join(base_dir, "test.txt")
train_1_file = open(train_1_dir, "w")
train_2_file = open(train_2_dir, "w")
val_file = open(val_dir, "w")
test_file = open(test_dir, "w")

for file, split in [(train_1_file, train_1), (train_2_file, train_2), (val_file, val), (test_file, test)]:
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
train_1_file.close()
train_2_file.close()
val_file.close()
test_file.close()
