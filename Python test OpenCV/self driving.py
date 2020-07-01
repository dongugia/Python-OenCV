import cv2
import numpy as np




if __name__ == '__main__':
    cap = cv2.VideoCapture(r'C:\Users\DK0626\Desktop\Python\Data\vid1.mp4')
    while True:
        _,img = cap.read()
        img = cv2.resize(img,(640,480))
        getLaneCurve(img)
        cv2.waitKey(1)

def thresholding(img):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lowerWhite = np.array([85, 0, 0])
    upperWhite = np.array([179, 160, 255])
    maskedWhite= cv2.inRange(hsv,lowerWhite,upperWhite)
    return maskedWhite

def getLaneCurve(img):
    imgThres = thresholding(img)