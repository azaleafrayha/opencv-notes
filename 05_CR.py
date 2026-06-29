import cv2 as cv

img = cv.imread('img/minileon.webp')
print(img.shape) # prints the shape of the image in (height, width, channels)

imgResize = cv.resize(img, (300, 200)) # (width, height) -> (x, y)

imgCrop = img[250:300, 300:400] # (height, width) -> (y1:y2, x1:x2)

cv.imshow('first image', img)
cv.imshow('resized image', imgResize)
cv.imshow('cropped image', imgCrop)
cv.waitKey(0)