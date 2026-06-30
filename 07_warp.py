import cv2 as cv
import numpy as np

img = cv.imread('img/cat.webp')

width, height = 400, 300
pts1 = np.float32([[208, 76], [500, 74], [208, 372], [500, 370]]) # you can get the points by ms paint or other img editing software
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv.getPerspectiveTransform(pts1, pts2)
imgOutput = cv.warpPerspective(img, matrix, (width, height))

cv.imshow("Original Image", img)
cv.imshow("Warped", imgOutput)
cv.waitKey(0)