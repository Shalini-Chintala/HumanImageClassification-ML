import cv2
import numpy

haar_cascade=cv2.CascadeClassifier('.\haarcascades\haarcascade_frontalface_default.xml')
people=['Indian','Non Indian']

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.save('face_trained.yml')

img_path=input("Enter the url: ")
img=cv2.imread(img_path)
gray=cv2.imread(img_path)
gray = cv2.cvtColor(img_array,cv2.COLOR_BGR2GRAY)

m=1.0
i=None

faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]
    label, confidence = face_recognizer.predict(faces_roi)
    if i is None:
        i=label
    if confidence>m:
        continue