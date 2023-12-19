import numpy
import cv2

# [
#   [-1, -2, -1]
#   [0, 0, 0]
#   [1, 2, 1]
# ]
#[
# [-1, 0, 1],
# [-2, 0, 2],
# [-1, 0, 1]
#]
# Операторы соболя

filterSobolyOne = numpy.array([
  [-1, 2, -1],
  [0, 0, 0],
  [1, 2, 1]
])

filterSobolyTwo = numpy.array([
  [-1, 0, 1],
  [-2, 0, 2],
  [-1, 0, 1]
])

image = cv2.imread('./src/practiceNumberFive/lena.jpg')

imageOne = cv2.filter2D(image, -1, filterSobolyOne)
imageTwo = cv2.filter2D(image, -1, filterSobolyTwo)

cv2.imwrite('./src/practiceNumberFive/lena-one.jpg', imageOne)
cv2.imwrite('./src/practiceNumberFive/lena-two.jpg', imageTwo)