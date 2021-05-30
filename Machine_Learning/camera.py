import cv2
import numpy as np
import pytesseract

cap = None
ret = None
frame = None
key = None

print('START')

cap = cv2.VideoCapture(0)
while True: 
    ret, frame = cap.read()
    cv2.imshow('Window', frame)
    print(pytesseract.image_to_string(frame))
    key = cv2.waitKey(2000)
    if key == (ord('q')):
        break
    cv2.destroyAllWindows()
    cap.release()

print('THE END')