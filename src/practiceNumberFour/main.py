import numpy
from skimage.io import imread, imsave


def line_filter(image: numpy.ndarray, coef: float, 
                maska: numpy.ndarray = numpy.array([
                    [1, 1, 1], 
                    [1, 1, 1], 
                    [1, 1, 1]
                    ])) ->  numpy.ndarray:
    
    def filter(image: numpy.ndarray, row: int, col: int) -> numpy.uint8:
        
        row = numpy.abs(row).astype('int')
        col = numpy.abs(col).astype('int')
        
        return image[row][col]
        
    
    maska = maska.dot(coef)
    
    rows, cols = maska.shape
    
    diffirenceRow = numpy.round(rows / 2).astype('int')
    diffirenceCol = numpy.round(cols / 2).astype('int')
    
    centerFilterRow:int = numpy.round((rows + diffirenceRow) / 2).astype('int')
    centerFilterCol:int = numpy.round((cols + diffirenceCol) / 2).astype('int')
    
    imageCopy = image.copy()
    
    for i in range(len(imageCopy) - 1):
        for j in range(len(imageCopy[0]) - 1):
            summa = 0
            for p in range(rows):
                for q in range(cols):
                    summa += filter(
                        imageCopy, i - centerFilterRow + p, 
                        j - centerFilterCol + q) * maska[p, q]
            
            summa = numpy.abs(summa)
            
            if summa <= 255:
                imageCopy[i, j] = numpy.uint8(numpy.round(summa))
                
    return imageCopy


image = imread('src/practiceNumberFour/lena.jpg')
imageHightFilter = line_filter(image=image, coef=1, maska=numpy.array([
	[0, -1, 0],[-1, 5, -1],[0, -1, 0]
]))
imsave('src/practiceNumberFour/lena-hight-filter.jpg', imageHightFilter)