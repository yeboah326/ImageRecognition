import cv2

camera_port = 0
camera = cv2.VideoCapture(camera_port)
return_value, image = camera.read()
cv2.imwrite("image.png", image)

camera.release() # Error is here
cv2.destroyAllWindows()