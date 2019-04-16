import cv2
import time

video = cv2.VideoCapture(0)

a = 0

while True:
    a = a + 1
    #check evaluates to True if the camera works and False when otherwise
    check, frame = video.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow('Video Capturing', gray)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break



print("You have ", a, "frames in your video")

video.release()

cv2.destroyAllWindows()