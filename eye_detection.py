import cv2

#Creating a cascade classifier object
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

#Reading the image as it is
img = cv2.imread("face1.png")

#Reading the image as grayscale image
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Search the coordinates of the image for faces
eyes = eye_cascade.detectMultiScale(gray_img, scaleFactor=1.05,minNeighbors=10)

for x,y,w,h in eyes:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0) , 1)

resized = cv2.resize(img, (1200,800))

cv2.imshow("Gray", resized)

cv2.waitKey(0)

cv2.destroyAllWindows()

