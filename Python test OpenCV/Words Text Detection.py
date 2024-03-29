import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time

pytesseract.pytesseract.tesseract_cmd = 'C:\\ProgramData\\Tesseract-OCR\\tesseract.exe'

img =  cv2.imread('Image\Text Detection.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

boxes = pytesseract.image_to_data(img)
for a,b in enumerate(boxes.splitlines()):
    print(b)
    if a != 0:
        b = b.split()
        if len(b) == 12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.putText(img, b[11], (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)
            cv2.rectangle(img, (x, y), (x + w, y + h), (50, 50, 255), 2)

#print(pytesseract.image_to_string(img))
cv2.imshow('IMG',img)
cv2.waitKey(0)