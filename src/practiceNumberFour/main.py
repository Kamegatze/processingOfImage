import cv2
import numpy

image = cv2.imread('./src/practiceNumberFour/lena.jpg')

# Высокочастотные фильтры в сумме которые даут единицу
filterHightOne = numpy.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])


filterHightTwo = numpy.array([
    [-1, -1, -1],
    [-1, 9, -1],
    [-1, -1, -1]
])

filterHightThree = numpy.array([
    [1, -2, 1],
    [-2, 5, -2],
    [1, -2, 1]
])

saveImageOne = cv2.filter2D(image, -1, filterHightOne)
saveImageTwo = cv2.filter2D(image, -1, filterHightTwo)
saveImageThree = cv2.filter2D(image, -1, filterHightThree)

cv2.imwrite('./src/practiceNumberFour/lena-hight-filter-one.jpg', saveImageOne)
cv2.imwrite('./src/practiceNumberFour/lena-hight-filter-two.jpg', saveImageTwo)
cv2.imwrite('./src/practiceNumberFour/lena-hight-filter-three.jpg', saveImageThree)