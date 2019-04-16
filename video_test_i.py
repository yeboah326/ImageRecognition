import cv2
import time

video = cv2.VideoCapture(0)

#check evaluates to True if the camera works and False when otherwise
check, frame = video.read()


#pauses the program for three seconds
time.sleep(3)

cv2.imshow('Capturing',frame)
cv2.waitKey()


video.release()

cv2.destroyAllWindows()