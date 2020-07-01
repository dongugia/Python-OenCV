import cv2

faceCascade = cv2.CascadeClassifier(r'C:\Users\DK0626\Desktop\Python\Data\haarcascades\haarcascade_frontalface_default.xml')
#img = cv2.imread(r'C:\Users\DK0626\Desktop\Shanks.png')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,150)

while True:
    success, img = cap.read()
    imgGray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray,1.1,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("A",img)
    #cv2.imshow("B",imgGray)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

