import cv2
import math
import numpy
from skimage.io import imread, imsave
import matplotlib.pyplot as plt
from skimage.transform import EuclideanTransform, AffineTransform, EssentialMatrixTransform, warp

def normalize8(image: numpy.ndarray):
  mn = image.min()
  mx = image.max()

  mx -= mn

  image = ((image - mn)/mx) * 255
  return image.astype(numpy.uint8)


image = imread('./src/practiceNumberTwo/lena.jpg')

# евклидовые преоброзования

euclideanProcessing = EuclideanTransform(rotation=numpy.deg2rad(15), translation=(1, 1))

image_eulidean = warp(image=image, inverse_map=euclideanProcessing)

imsave('./src/practiceNumberTwo/lena-processing-euclidean.jpg', normalize8(image_eulidean))

affineProcessing = AffineTransform(shear=numpy.deg2rad(15), rotation=numpy.deg2rad(0), translation=(1, 1))

image_affine = warp(image=image, inverse_map=affineProcessing)

imsave('./src/practiceNumberTwo/lena-processing-affine.jpg', normalize8(image_affine))

rows, cols = image.shape

image_essantial = cv2.warpPerspective(image, numpy.float32([
    [1, 0, 0],
    [0, 1, 0],
    [0.0005, 0.00005, 1]
]), (rows, cols))

imsave('./src/practiceNumberTwo/lena-processing-essantial.jpg', image_essantial)