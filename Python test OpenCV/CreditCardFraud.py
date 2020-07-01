import cv2
from cv2 import *
from openCV import *


color_img = cv2.imread(r'C:\Users\DK0626\Desktop\Python\Data\Cat.jpg')
gray_img = cv2.imread(r'C:\Users\DK0626\Desktop\Python\Data\Cat.jpg',0)

cv2.imshow('Cat image', color_img)

k = cv2.waitKey()

if (k == ord('c')):
    cv2.imwrite('color.jpg',color_img)
    print("Image is saved color")
    cv2.destroyAllWiindows()

if (k == ord('g')):
    cv2.imwrite('gray.jpg',gray_img)
    print("image saved in grayscale")
    cv2.destroyAllWindows()


