import os
import cv2
import numpy as np

people=['Indian','Non Indian']
dir=r".\train"

haar_cascade=cv2.CascadeClassifier('.\haarcascades\haarcascade_frontalface_default.xml')

features=[]
labels=[]

def create_train():
    for person in people:
        path=os.path.join(dir,person)
        label=people.index(person)

        for img in os.listdir(path):
            img_path=os.path.join(path,img)

            img_array=cv2.imread(img_path)
            if img_array is None:
                continue
            gray = cv2.cvtColor(img_array,cv2.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print("Done")
features=np.array(features,dtype='object')
labels=np.array(labels)
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(features,labels)
face_recognizer.save('face_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)