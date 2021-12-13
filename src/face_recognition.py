'''
Create date : 2021/12/10.
Update      : 2021/12/12.
Writer      : Nishimura Kairi
'''

import cv2
import matplotlib.pyplot as plt 

# constants define
DEVICE_ID = 0
# path reading
FACE_CASCADE_PATH = 'C:/opencv/sources/data/haarcascades/'\
                'haarcascade_frontalface_default.xml'
EYE_CASCADE_PATH = 'C:/opencv/sources/data/haarcascades/'\
                    'haarcascade_eye.xml'
MOUSE_CASCADE_PATH = 'C:/opencv/sources/data/haarcascades/'\
                        'haarcascade_mcs_mouth.xml'

# classifier define
face_classifier = cv2.CascadeClassifier(FACE_CASCADE_PATH)
mouse_classifier = cv2.CascadeClassifier(MOUSE_CASCADE_PATH)
eye_classifier = cv2.CascadeClassifier(EYE_CASCADE_PATH)
# video capture getting
cap = cv2.VideoCapture(DEVICE_ID)
# real-time proccesing
while True:
    end_flag , frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(frame, minSize=(100,100))
    # target drowing
    for x, y, w, h in faces:
        gray_frame = frame[y:y+h, x:x+w]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        mouses = mouse_classifier.detectMultiScale(gray_frame)
        if len(mouses) > 0:
            cv2.putText(frame, 'No mask! Please wear a mask!', (10, 100), 1, cv2.FONT_HERSHEY_DUPLEX, (0,0,255), thickness=2)
    # display
    cv2.imshow("org", frame)

    # if put on Q key -> end proccesing
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# end proccesing
cap.release()
cv2.destroyAllWindows()