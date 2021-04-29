from ImageInput import ImageInput, ImageInputSet
from WordInput import WordInput, WordInputSet
from DataLoading import DataLoading
from Preprocessing import Preprocessing
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from pathlib import Path
from collections import Counter

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


# Read images
## Prepare the images
base_width = 512
base_height = 128

images_from_files = DataLoading.loadImagesFromPath('./washington_dataset/words')
max_width = images_from_files.getMaxWidth()
resized_images = Preprocessing.resizeImages(images_from_files, max_width, base_height)
image_collection = Preprocessing.invertImages(resized_images)

print("Number of images:", len(image_collection.images))
print("First image resized size:", image_collection.images[25].original_width, 'x', image_collection.images[25].original_height)
plt.imshow(image_collection.images[25].img)
plt.show()

# Data Loading
## Load Sets

test_keys = DataLoading.getKeysFromFile('./washington_dataset/sets/test.txt')
train_keys = DataLoading.getKeysFromFile('./washington_dataset/sets/train.txt')
valid_keys = DataLoading.getKeysFromFile('./washington_dataset/sets/valid.txt')

test_set = DataLoading.getImageInputSetFromKeys(image_collection, test_keys)
train_set = DataLoading.getImageInputSetFromKeys(image_collection, train_keys)
valid_set = DataLoading.getImageInputSetFromKeys(image_collection, valid_keys)

print('Size of test set: ', len(test_set.images))
print('Size of train set: ', len(train_set.images))
print('Size of valid set: ', len(valid_set.images))

exit()
# Data Loading
## Load Labels

labels = DataLoading.getLabelsFromFile('./washington_dataset/word_labels.txt')
characters = labels.getSetOfChars()

print('Characters: ', labels.getSetOfChars())

# Preprocessing

# Mapping characters to integers
char_to_num = layers.experimental.preprocessing.StringLookup(
    vocabulary=list(characters), num_oov_indices=0, mask_token=None
)

# Mapping integers back to original characters
num_to_char = layers.experimental.preprocessing.StringLookup(
    vocabulary=char_to_num.get_vocabulary(), mask_token=None, invert=True
)

labels.getWordInputFromImage('275-01-01.png')
x_train, y_train = Preprocessing.split_data(train_set, labels, False)
# train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))

print(y_train[33])
plt.imshow(x_train[33])
plt.show()