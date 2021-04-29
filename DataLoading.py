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
  def getImageInputSetFromKeys(image_collection, keys):
    images = []
    for key in keys:
        images.extend(image_collection.fromSet(key))
    return ImageInputSet(images)
  
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
      images.append(ImageInput(image, file_path))
    
    return images

