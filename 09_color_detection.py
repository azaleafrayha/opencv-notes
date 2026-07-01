import cv2 as cv
import numpy as np

def empty(a):
    pass

cv.namedWindow("TrackBars") # this is the name of the window that will be created
cv.resizeWindow("TrackBars", 640, 240) # this is the size of the window that will be created

cv.createTrackbar("Hue Min", "TrackBars", 20, 179, empty) # -> (name of the trackbar, name of the window, min value, max value, function to be called when the trackbar is changed)
cv.createTrackbar("Hue Max", "TrackBars", 29, 179, empty)
cv.createTrackbar("Sat Min", "TrackBars", 26, 255, empty)
cv.createTrackbar("Sat Max", "TrackBars", 78, 255, empty)
cv.createTrackbar("Val Min", "TrackBars", 193, 255, empty)
cv.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

while True:
    img = cv.imread('img/minileon.webp')
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV) # HSV stands for Hue, Saturation, Value.

    h_min = cv.getTrackbarPos("Hue Min", "TrackBars") # returns the current position of the trackbar
    h_max = cv.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv.getTrackbarPos("Val Max", "TrackBars")

    print(h_min, h_max, s_min, s_max, v_min, v_max) # prints the current position of the trackbars

    lower = np.array([h_min, s_min, v_min]) # create a numpy array for the lower bound of the HSV values
    upper = np.array([h_max, s_max, v_max]) 
    mask = cv.inRange(imgHSV, lower, upper) # filter the image to only show the colors within the specified range

    imgResult = cv.bitwise_and(img, img, mask=mask) # apply the mask to the original image to get the result

    cv.imshow("Image", img)
    cv.imshow("HSV Image", imgHSV)
    cv.imshow("Mask", mask)
    cv.imshow("Result", imgResult)
    cv.waitKey(1)