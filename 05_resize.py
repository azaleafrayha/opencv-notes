import cv2 as cv

img = cv.imread('img/minileon.webp')
print(img.shape) # prints the shape of the image in (height, width, channels)

imgResize = cv.resize(img, (300, 200)) # resize the image to 300x200 pixels

cv.imshow('first image', img)
cv.imshow('resized image', imgResize)
cv.waitKey(0)