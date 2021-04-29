import cv2
import os
from ImageInput import ImageInput, ImageInputSet
from WordInput import WordInput, WordInputSet
from PIL import Image

class DataLoading:
  @staticmethod
  def getLabelsFromFile(filename):
    labels = []
    with open(filename) as f:
        for line in f:
            word = WordInput(line)
            labels.append(word)
    return WordInputSet(labels)
  
  @staticmethod
  def getKeysFromFile(filename):
    keys = []
    with open(filename) as f:
        for line in f:
            keys.append(line.replace("\n", ""))
    return keys
  
  @staticmethod
  def loadImagesFromPath(path):
    images = ImageInputSet([])
    for file in os.listdir(path):
      file_path = os.path.join(path,file)
      image = Image.fromarray(cv2.imread(file_path))
      filename = os.path.basename(file_path).split('.')[0]
      images.append(ImageInput(image, filename))
    
    return images

  @staticmethod
  def split_in_sets(images_collection, train_keys, test_keys, valid_keys):
    images = images_collection.images
    train_images = []
    test_images = []
    valid_images = []
    for image in images:
      image_page = image.filename[:-3]
      if image_page in train_keys:
        train_images.append(image)
      elif image_page in test_keys:
        test_images.append(image)
      elif image_page in valid_keys:
        valid_images.append(image)
    return ImageInputSet(train_images), ImageInputSet(test_images), ImageInputSet(valid_images)
