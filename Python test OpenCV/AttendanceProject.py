import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime as dt

path = 'ImageAttendance'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cls in myList:
    curImg = cv2.imread(f'{path}/{cls}')
    images.append(curImg)
    classNames.append(os.path.splitext(cls)[0])
print(classNames)


def finEncodings(images):
    '''
    Thiet dat mac dinh Khuon mat cho moi buc anh data
    :return: encodeList
    '''
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def markAttendance(name):
    '''
    Xuat thong tin nhan dien khuon mat va thoi gian nhan dien
    :param name:
    :return:
    '''
    with open('Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = dt.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')

encodeListKnown = finEncodings(images)


cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img,(0,0),fx=0.25,fy=0.25)
    imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

    for encodeFace, faceLoc in zip(encodeCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        #print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            if faceDis[matchIndex]< 0.50:
                name = classNames[matchIndex].upper()
            else: name = 'Unknown'

            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4,x2*4, y2*4, x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+20,y2-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),2,cv2.LINE_AA)

            markAttendance(name)

    cv2.imshow("Webcam",img)

    if cv2.waitKey(1) and 0xFF == ord('s'):
        cv2.imwrite('ImageAttendance\*.*' ,img )
        cv2.waitKey(500)

    # if cv2.waitKey(1) and 0xFF == ord('q'):
    #     break

