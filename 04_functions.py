import cv2 as cv
import numpy as np

img = cv.imread('img/minileon.webp')
kernel = np.ones((5, 5), np.uint8) # create a kernel for morphological operations, (5, 5) is the size of the kernel (5 horizontal, 5 vertical), np.uint8 is the data type of the kernel

imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # convert the image to grayscale
imgBlur = cv.GaussianBlur(imgGray, (7, 7), 0) # apply Gaussian blur to the grayscale image, (7, 7) is the kernel size, 0 is the standard deviation in X and Y direction
imgCanny = cv.Canny(img, 150, 200) # apply Canny edge detection to the original image, 150 is the lower threshold, 200 is the upper threshold
imgDilation = cv.dilate(imgCanny, kernel, iterations=5) # kernel is the structuring element, iterations is the thickness of the edges (dilation = thick.)
imgEroded = cv.erode(imgDilation, kernel, iterations=10) # (erosion = thin.)

cv.imshow("The Image", imgEroded) # ("the image", any function that we pick)
cv.waitKey(0)