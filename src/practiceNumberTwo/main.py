import cv2
import math
import numpy
from skimage.io import imread, imsave
from skimage.transform import EuclideanTransform, AffineTransform, warp

def normalize8(image: numpy.ndarray):
  mn = image.min()
  mx = image.max()

  mx -= mn

  image = ((image - mn)/mx) * 255
  return image.astype(numpy.uint8)


image = imread('./src/practiceNumberTwo/lena.jpg')

# евклидовые преоброзования

euclideanProcessing = EuclideanTransform(rotation=math.radians(15), translation=(1, 1))

image_eulidean = warp(image=image, inverse_map=euclideanProcessing)

imsave('./src/practiceNumberTwo/lena-processing-euclidean.jpg', normalize8(image_eulidean))

# аффиновые преоброзования

affineProcessing = AffineTransform(shear=math.radians(15), rotation=math.radians(0), translation=(1, 1))

image_affine = warp(image=image, inverse_map=affineProcessing)

imsave('./src/practiceNumberTwo/lena-processing-affine.jpg', normalize8(image_affine))

# Проективные преоброзования

rows, cols = image.shape

image_essantial = cv2.warpPerspective(image, numpy.float32([
    [1, 0.1, 0],
    [0.1, 1, 0],
    [0.001, 0.00001, 1]
]), (rows, cols))

imsave('./src/practiceNumberTwo/lena-processing-essantial.jpg', image_essantial)