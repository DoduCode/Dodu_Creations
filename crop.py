import cv2
image = cv2.imread("Your image path")

y=0
x=0
h=300
w=510
crop_image = image[x:w, y:h]
cv2.imshow("Cropped", crop_image)
cv2.waitKey(0)
