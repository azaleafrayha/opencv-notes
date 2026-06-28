import cv2 as cv

img = cv.imread('img/minileon.webp')
cv.imshow('mwah', img)
cv.waitKey(0) # the input is in miliseconds, 0 means wait forever/infinite