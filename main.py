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


# Data Loading
## Prepare the images
base_height = 128

images_from_files = DataLoading.loadImagesFromPath('./washington_dataset/words')
max_width = images_from_files.getMaxWidth()

resized_images = Preprocessing.resizeImages(images_from_files, max_width, base_height)
image_collection = Preprocessing.invertImages(resized_images)

print("Number of images:", len(image_collection.images))

## Load Sets

train_keys = DataLoading.getKeysFromFile('./washington_dataset/sets/train.txt')
test_keys = DataLoading.getKeysFromFile('./washington_dataset/sets/test.txt')
valid_keys = DataLoading.getKeysFromFile('./washington_dataset/sets/valid.txt')

train_set, test_set, valid_set = DataLoading.split_in_sets(image_collection, train_keys, test_keys, valid_keys)

print('Size of test set: ', test_set.size())
print('Size of train set: ', train_set.size())
print('Size of valid set: ', valid_set.size())

# Data Loading
## Load Labels

labels = DataLoading.getLabelsFromFile('./washington_dataset/word_labels.txt')
characters = labels.getSetOfChars()

print('Number of used chars: ', len(characters))

# Preprocessing

labels.set_words_length_to_max()
x_train, y_train = Preprocessing.get_labeled_images(train_set, labels, characters, False)
print('Example label:', y_train[33])

plt.imshow(x_train[33])
plt.show()
