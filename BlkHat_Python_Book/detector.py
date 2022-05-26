"""
a simple facial image detector using OPENCV
"""
import os
import cv2

ROOT = '/home/foxhound/Desktop/pictures'
FACES = '/home/foxhound/Desktop/faces'
TRAIN = '/home/foxhound/Desktop/training'

def detect(src_dir=ROOT, tgt_dir=FACES, train_dir=TRAIN):
    for fname in os.listdir(src_dir):
        if not fname.upper().endswith('.JPG'):
            continue
        full_name = os.path.join(src_dir, fname)
        new_name = os.path.join(tgt_dir, fname)
        img = cv2.imread(full_name)
        if img is None:
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        training = os.path.join(train_dir, 'haarcascade_frontalface_alt.xml')
        cascade = cv2.CascadeClassifier(training)
        rects = cascade.detectMultiScale(gray, 1.3, 5)
        try:
            if rects.any():
                print('Got a Face')
                rects[:, 2:] += rects[:, :2]
        except AttributeError:
            print(f'No faces found in {fname}.')
            continue

        for x1,y1,x2,y2 in rects:
            cv2.rectangle(img, (x1, y1), (x2, y2), (127, 255, 0), 2)
        cv2.imwrite(newname, img)

if __name__ == '__main__':
    detect()