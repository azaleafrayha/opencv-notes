import cv2 as cv
import numpy as np

img = np.zeros((512, 512, 3), np.uint8) # this creates a black image of size 512x512 with 3 color channels (without 3, it would be a grayscale image)
# print(img)
# img[:] = 255, 0, 0 # this sets the entire image to blue color (BGR format)

cv.line(img, (0,0), (img.shape[1], img.shape[0]), (0, 255, 0), 3) # (img, start point, end point, color, thickness) -> (img, (x1, y1), (x2, y2), (B, G, R), thickness)
# img.shape[1] is the width of the image, img.shape[0] is the height of the image

cv.rectangle(img, (0, 0), (250, 350), (0, 0, 255), cv.FILLED) # (img, top left corner, bottom right corner, color, thickness) -> (img, (x1, y1), (x2, y2), (B, G, R), thickness)

cv.circle(img, (400, 50), 30, (255, 255, 0), 5) # (img, center, radius, color, thickness) -> (img, (x, y), radius, (B, G, R), thickness)

cv.putText(img, "OPENCV", (300, 200), cv.FONT_HERSHEY_COMPLEX, 0.8, (0, 150, 0), 2) # (img, "text", (x, y), font type, font scale, (B, G, R), thickness)

cv.imshow("Image", img)

cv.waitKey(0)