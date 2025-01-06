#this file will house functions to split processed data into Train, Test, and Cross Validation sets



#loop through all preprocessed images

#70% to train set

#15% to cross validation

#15% to test set


import os
import shutil
import random

# Paths


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROCESSED_DIR = "../../data/processed"
TRAIN_DIR = "../../data/train"
TEST_DIR = "../../data/test"
VAL_DIR = "../../data/val"

# Split ratios
TRAIN_RATIO = 0.7
TEST_RATIO = 0.15
VAL_RATIO = 0.15

def split_data():
    # Ensure output directories exist
    #for dir_path in [TRAIN_DIR, TEST_DIR, VAL_DIR]:
     #   for label in ["cat", "dog"]:
      #      os.makedirs(os.path.join(dir_path, label), exist_ok=True)

    # Loop through categories (e.g., cat and dog)
    for label in ["cat", "dog"]:
        category_dir = os.path.join(PROCESSED_DIR, label)
        files = os.listdir(category_dir)

        # Shuffle files to ensure randomness
        random.shuffle(files)

        # Calculate split indices
        total_files = len(files)
        train_end = int(total_files * TRAIN_RATIO)
        test_end = train_end + int(total_files * TEST_RATIO)

        # Split files
        
        train_files = files[:train_end]
        test_files = files[train_end:test_end]
        val_files = files[test_end:]

        # copy files
        for file in train_files:
            shutil.copy(os.path.join(category_dir, file), os.path.join(TRAIN_DIR, label, file))
        for file in test_files:
            shutil.copy(os.path.join(category_dir, file), os.path.join(TEST_DIR, label, file))
        for file in val_files:
            shutil.copy(os.path.join(category_dir, file), os.path.join(VAL_DIR, label, file))

    print("Data successfully split into train, test, and validation sets.")

# Run the split
split_data()
