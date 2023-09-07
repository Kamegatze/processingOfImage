from skimage.io import imread, imsave
import numpy
from math import floor

def lineСontrastingImage(image : numpy, g_max, g_min) : 
  max_value = image.max()
  min_value = image.min()
  
  image_return = numpy.array(image).tolist().copy()
  
  a = (g_max - g_min)/(max_value - min_value)
  
  b = g_min - a*min_value

  g = lambda a, b, f: a * f + b
  
  for i in range(len(image)):
    image_return[i] = list(
      map(
        lambda item: numpy.uint8(floor(g(a, b, item))), image[i]
      )
    )
    
  return numpy.array(image_return)


def dissection(image : numpy) : 
  image_return = numpy.array(image).tolist().copy()
  
  max_value = image.max()
  
  min_value = image.min()
  
  g_min = 255 - max_value
  
  for i in range(len(image)):
    image_return[i] = list(
      map(
        lambda item : numpy.uint8(item) if item != min_value else numpy.uint8(g_min), image[i]
      )
    )
  
  return numpy.array(image_return)



images = imread("./src/practickNumberOne/lena.jpg")

# images = lineСontrastingImage(images, images.max() - 50, 30)

# imsave('./src/practickNumberOne/images-other.jpg', images)

images = dissection(images)

imsave('./src/practickNumberOne/images-other.jpg', images)