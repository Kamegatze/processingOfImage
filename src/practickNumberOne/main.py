from skimage.io import imread, imsave
import numpy
from math import floor
import matplotlib.pyplot as plt

def lineСontrastingImage(image : numpy, g_max, g_min) : 
  max_value = image.max()
  min_value = image.min()
  
  image_return = numpy.array(image).tolist().copy()
  
  a = (g_max - g_min)/(max_value - min_value)
  
  b = g_min - a * min_value

  g = lambda a, b, f: a * f + b
  
  image_return = list(
    map(
      lambda row : list(
        map(
          lambda item: numpy.uint8(floor(g(a, b, item))), row
        )
      ), image_return
    )
  )
    
  return numpy.array(image_return)


def dissection(image : numpy) : 
  
  def subDissection(pixel : int, g_min : int) :
    value = pixel + g_min if pixel + g_min < 256 else 255 
    return numpy.uint8(value) 
    
  image_return = numpy.array(image).tolist().copy()
  
  max_value = image.max()
  
  g_min = 255 - max_value
  
  image_return = list(
    map(
      lambda row: list(
        map(
          lambda pixel: subDissection(pixel, g_min), row
        )
      ), image_return
    )
  )
  
  return numpy.array(image_return)

def equalization(images: numpy.ndarray, hist: numpy.ndarray) : 
  
  cdf = hist.cumsum()

  cdf = (cdf-cdf[0]) *255/ (cdf[-1]-1)
  cdf = cdf.astype(numpy.uint8)

  return cdf[images]

images = imread("./src/practickNumberOne/lena.jpg")

# images_other = lineСontrastingImage(images, images.max(), 60)

images_other = dissection(images)

plt.hist(images.ravel(), 255)

hist, bins = numpy.histogram(images.flatten(), 255, [0, 255])

# images_other = equalization(images, hist)

plt.hist(images_other.ravel(), 255)

plt.show()

imsave('./src/practickNumberOne/images-other.jpg', images_other)