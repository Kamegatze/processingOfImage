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
            
            imageCopy[i, j] = numpy.uint8(numpy.round(summa))
    
    return imageCopy


def recursive_filter(image: numpy.ndarray, coef: float, k: float = 1, maska: numpy.ndarray = numpy.array([
                    [1, 1, 1], 
                    [1, 1, 1], 
                    [1, 1, 1]
                    ]))-> numpy.ndarray:
    
    return line_filter(image, coef, maska).dot(k).astype(numpy.uint8) + line_filter(image, coef, maska).dot(1 - k).astype(numpy.uint8)


def median_filter(image: numpy.ndarray, rows:int = 3, cols:int = 3)-> numpy.ndarray:

    imageCopy = image.copy()
    
    diffirenceRow = numpy.round(rows / 2).astype('int')
    diffirenceCol = numpy.round(cols / 2).astype('int')
    
    centerRow: int = numpy.round((rows + diffirenceRow) / 2).astype('int')
    centerCol: int = numpy.round((cols + diffirenceCol) / 2).astype('int')
    
    for i in range(0, len(imageCopy), rows):
        for j in range(0, len(imageCopy[0]), cols):
            
            filter = []
            
            maxIndexRow = 0
            maxIndexCol = 0
            
            maxValue = 0
            
            for p in range(rows):
                for q in range(cols):          
                    value = imageCopy[numpy.abs(i - centerRow + p).astype('int'), 
                                            numpy.abs(j - centerCol + q).astype('int')]
                    
                    filter.append(value)
                    
                    if maxValue <= value:
                        maxValue = value
                        maxIndexCol = numpy.abs(j - centerCol + q).astype('int')
                        maxIndexRow = numpy.abs(i - centerRow + p).astype('int')
            
            imageCopy[maxIndexRow, maxIndexCol] = numpy.median(filter).astype(numpy.uint8)   
            
    return imageCopy         
    
    
image = imread('./src/practiceNumberThree/lena.jpg')

# реализация линейного фильтра

imageLineFilter = line_filter(image, 1/16, numpy.array([
    [2, 1, 2],[1, 4, 1],[2, 1, 2]
]))

imsave('./src/practiceNumberThree/lena-liner-filter.jpg', imageLineFilter)

# реализация рекурсивного фильтра

imageRecursiveFilter = recursive_filter(image, 1 / 16, 0.9, numpy.array([
    [2, 1, 2],[1, 4, 1],[2, 1, 2]
]))

imsave('./src/practiceNumberThree/lena-recursive-filter.jpg', imageRecursiveFilter)

# реализация медианной фильтрации

imageMedian = median_filter(image, 7, 7)

imsave('./src/practiceNumberThree/lena-median-filter.jpg', imageMedian)