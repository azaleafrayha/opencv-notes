import cv2 as cv
import numpy as np

img = cv.imread('img/minileon.webp')

imgHor = np.hstack((img, img))
imgVer = np.vstack((img, img))

cv.imshow("Horizontal Stack", imgHor) 
cv.imshow("Vertical Stack", imgVer)
cv.waitKey(0)