import cv2

#Creating a cascade classifier object
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Reading the image as it is
img = cv2.imread("Bill.png")

#Reading the image as grayscale image
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Search the coordinates of the image for faces
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05,minNeighbors=5)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0) , 1)

resized = cv2.resize(img, (800,800))

cv2.imshow("Gray", resized)

cv2.waitKey(0)

cv2.destroyAllWindows()

