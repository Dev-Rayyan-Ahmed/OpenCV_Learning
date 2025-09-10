import os
import cv2 as cv
import numpy

people = ["Ben Afflek", "Elton John", "Jerry Seinfield", "Madonna", "Mindy Kaling"]
DIR = r"C:\Coding (VScode)\Codes\.CodingTools\OpenCV_Learning\Resources\Faces\train"

features = []
labels = []
haar_cascade = cv.CascadeClassifier(r"Sec3_Faces\haar_face.xml")

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_read = cv.imread(img_path)
            gray = cv.cvtColor(img_read, cv.COLOR_BGR2GRAY)

            face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

            for (x,y,w,h) in face_rect:
                face_roi = gray[y:y+h, x:x+w]

                features.append(face_roi)
                labels.append(label)

create_train()
# print(f"Length of features: {len(features)}")
# print(f"Length of Labels: {len(labels)}")

features = numpy.array(features, dtype= "object")
labels = numpy.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer.create()
face_recognizer.train(features, labels)
face_recognizer.save("Trained_Face_Recog.yml")

numpy.save("features.npy", features)
numpy.save("labels.npy", labels)


