import cv2
import numpy as np

img = cv2.imread(r'C:\Users\DK0626\Desktop\Sun Flower.jpg')
print(img.shape)

imgResize = cv2.resize(img,(640,480))
imgcrop = imgResize[0:300,100:300]

print(imgResize.shape)

#cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Crop", imgcrop)

cv2.waitKey(0)

