import os
from ImageInput import ImageInput, ImageInputSet
from WordInput import WordInput, WordInputSet
import random
import numpy as np
from PIL import Image, ImageOps

class Preprocessing:
  @staticmethod
  def resizeImages(image_set: ImageInputSet, width, height):
    resized_images = []
    for index, image in enumerate(image_set.images):
      # Read
      img = image.img
      # Resize proportionally
      proportional_width = height * image.original_width // image.original_height
      img = img.resize((proportional_width, height), Image.ANTIALIAS)
      # Add padding
      padding_img = Image.new(img.mode, (width, height), (255, 255, 255))
      padding_img.paste(img, (0, 0))
      img = ImageInput(padding_img, image.filename, image.original_width, image.original_height)
      resized_images.append(img)
    return ImageInputSet(resized_images)

  @staticmethod
  def invertImages(image_set: ImageInputSet):
    inverted_images = []
    for index, image in enumerate(image_set.images):
      # Invert
      img = ImageOps.invert(image.img)
      img = ImageInput(img, image.filename, image.original_width, image.original_height)
      inverted_images.append(img)
    return ImageInputSet(inverted_images)

  @staticmethod
  def get_labeled_images(image_set: ImageInputSet, label_set: WordInputSet, vocabulary, shuffle=True):
    images = []
    labels = []
    
    images_from_set = random.shuffle(image_set.images) if shuffle else image_set.images

    for image_input in images_from_set:
      images.append(np.array(image_input.img))
      label = label_set.getWordInputFromImage(image_input.filename).word
      label = Preprocessing.char_to_num(label, vocabulary)
      labels.append(np.array(label))
    return images, labels

  @staticmethod
  def char_to_num(word, vocabulary):
     letters = word.split('-')
     numbers = list(map(lambda letter: vocabulary.index(letter), letters))
     return numbers

  @staticmethod
  def num_to_char(numbers, vocabulary):
    letters = list(map(lambda num: vocabulary[num], numbers))
    return letters