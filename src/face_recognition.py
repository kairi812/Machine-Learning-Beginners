'''
Create date : 2021/12/10.
Update      : 2021/12/12.
Writer      : Nishimura Kairi
'''

import cv2
import matplotlib.pyplot as plt    

if __name__ == '__main__':
    # constants define
    DEVICE_ID = 0
    # path reading
    CASCADE_PATH = 'C:/opencv/sources/data/haarcascades/'\
                    'haarcascade_frontalface_alt2.xml'
    # classifier define
    classifier = cv2.CascadeClassifier(CASCADE_PATH)
    # video capture getting
    cap = cv2.VideoCapture(DEVICE_ID)
    end_flag, frame = cap.read()
    h, w = frame.shape[:2]
    # real-time proccesing
    while end_flag == True:
        targets = classifier.detectMultiScale(frame, minSize=(100,100))
        # target drowing
        for x, y, w, h in targets:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # display
        cv2.imshow("org", frame)

        # if put on Esc key -> end proccesing
        key = cv2.waitKey(33)
        if key == 27:
            break

        # update
        end_flag , frame = cap.read()
    
    # end proccesing
    cv2.destroyAllWindows()
    cap.release()