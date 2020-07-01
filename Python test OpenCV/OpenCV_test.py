import cv2
import numpy as np

cap= cv2.imread(r'C:\Users\DK0626\Desktop\Sun Flower.jpg')
cap = cv2.resize(cap,(640,480))
kernel = np.ones((2,2),np.uint8)
img1 = cv2.VideoCapture(0)
img1.set(3,640)
img1.set(4,480)

while True:
    success, img = img1.read()
    img = cv2.Canny(img,50,80)
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

imgGray=  cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(cap,100,200)
imgDialation = cv2.dilate(imgCanny,kernel,iterations = 1)
imgEroded = cv2.erode(imgDialation,kernel,iterations = 1)

#cv2.imshow("Gray Image",imgGray)
#cv2.imshow("Blur Image", imgBlur)
#cv2.imshow("Canny", imgCanny)
#cv2.imshow("Dialation Image", imgDialation)
#cv2.imshow("Eroded Image", imgEroded)

cv2.waitKey(0)
