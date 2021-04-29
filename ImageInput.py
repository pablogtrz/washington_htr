import os
import cv2
from PIL import Image

class ImageInput:
  def __init__(self, image, filename, width=0, height=0, label=''):
    self.img = image
    self.filename = filename
    self.original_width = width if width > 0 else self.img.size[0]
    self.original_height = height if height > 0 else self.img.size[1]
    # self.original_height = self.img.size
    self.label = label

class ImageInputSet:
  def __init__(self, images):
    self.images = images

  def append(self, image):
    self.images.append(image)

  def getMaxWidth(self):
    max_width = 0
    for image_input in self.images:
      if image_input.original_width > max_width:
        max_width = image_input.original_width
    return max_width
    
  def fromSet(self, set):
    return list(filter(lambda i: i.filename.startswith(set), self.images))
    