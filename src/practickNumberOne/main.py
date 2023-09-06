from PIL import Image
from matplotlib import image
import numpy

def lineСontrastingImage(image : numpy, g_max, g_min) : 
  max_value = image.max()
  min_value = image.min()
  
  image_return = numpy.array(image).tolist().copy()
  
  a = (g_max - g_min)/(max_value - min_value)
  
  b = g_min - a*min_value

  g = lambda a, b, f: a*f + b
  
  for i in range(len(image)):
    for j in range(len(image[i])):
      image_return[i][j] = list(
        map(
          lambda item: g(a, b, item) / 255, image[i][j]
        )
      )
    
  return numpy.array(image_return)


def dissection(image : numpy) : 
  image_return = numpy.array(image).tolist().copy()
  
  max_value = image.max()
  
  min_value = image.min()
  
  g_min = 255 - max_value
  
  for i in range(len(image)):
    for j in range(len(image[i])):
      image_return[i][j] = list(
        map(
          lambda item : item / 255 if item != min_value else g_min /255, image[i][j]
        )
      )
  
  return image_return

images = image.imread('./src/practickNumberOne/images.jpg')

images = lineСontrastingImage(images, images.max(), 30)

# image.imsave('./src/practickNumberOne/images-other.jpg', images)

# images = dissection(images)

image.imsave('./src/practickNumberOne/images-other.jpg', images)