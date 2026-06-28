import cv2 as cv

capture = cv.VideoCapture('vid/cat.mp4')

while True: # need to use while loop to read the video frame by frame
    isTrue, frame = capture.read() # isTrue is a boolean value, frame is the actual frame of the video, and capture.read() reads the video frame by frame
    cv.imshow('Video', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):  # means if the user presses the 'q' key, then break the loop and stop the video
        break

capture.release() # if we don't release the video capture, then the video will not be released and will keep running in the background that causes a memory leak and will slow down the computer
cv.destroyAllWindows()  # might freeze the computer if we don't destroy all the windows that are created by OpenCV