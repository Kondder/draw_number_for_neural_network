import cv2 

img = cv2.imread("test_number.png")

img = cv2.resize(img, (28, 28))

cv2.imwrite("set5/test_number_rz.png", img)