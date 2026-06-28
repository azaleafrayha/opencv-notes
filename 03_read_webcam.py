import cv2 as cv

capture = cv.VideoCapture(0, cv.CAP_DSHOW) # 0 means the default webcam, if you have multiple webcams, you can change the number to 1, 2, etc.
# CAP_DSHOW is a flag that tells OpenCV to use the DirectShow backend for video capture, which is a Windows-specific API for capturing video from webcams and other video devices. It can help improve compatibility and performance when using certain webcams on Windows systems.

capture.set(3, 640) # 3 is the width of the webcam, 640 is the width in pixels
capture.set(4, 480) # 4 is the height of the webcam, 480 is the height in pixels

# the while loop is the same like the 02_read_vid.py, but the difference is that we are reading from the webcam instead of a video file
while True: 
    isTrue, frame = capture.read()
    cv.imshow('Webcam', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):  
        break

capture.release()
cv.destroyAllWindows()