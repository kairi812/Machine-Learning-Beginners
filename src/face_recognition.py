'''
Create date : 2021/12/10.
Update      : 2021/12/11.
Writer      : Nishimura Kairi
'''

import cv2
import matplotlib.pyplot as plt

def main():
    CASCADE_PATH = 'C:/opencv/sources/data/haarcascades/'\
                    'haarcascade_frontalface_default.xml'
    INPUT_IMG_PATH = "src/data/img/lena.png"
    OUTPUT_IMG_PATH = "src/data/output/face_recognition.png"

    classifier = cv2.CascadeClassifier(CASCADE_PATH)

    img = cv2.imread(INPUT_IMG_PATH)

    color = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    targets = classifier.detectMultiScale(color)

    for x,y,w,h in targets:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imwrite(OUTPUT_IMG_PATH, img)

if __name__ == '__main__':
    main()