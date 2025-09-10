import cv2 as cv
import numpy as np

people = ["Ben Afflek", "Elton John", "Jerry Seinfield", "Madonna", "Mindy Kaling"]

haar_cascade = cv.CascadeClassifier(r"Sec3_Faces\haar_face.xml")
features = np.load(r"Sec3_Faces\features.npy", allow_pickle= True)
labels = np.load(r"Sec3_Faces\labels.npy")

face_recognizer = cv.face.LBPHFaceRecognizer.create()
face_recognizer.read(r"Sec3_Faces\Trained_Face_Recog.yml")

path = r"C:\Coding (VScode)\Codes\.CodingTools\OpenCV_Learning\Resources\Faces\val\ben_afflek\1.jpg"
img = cv.imread(path)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in face_rect:
    face_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(face_roi)
    print(f"Predicted Label is: {label} with Confidence of: {confidence} and So, Predicted Person is: {people[label]}")

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

cv.imshow("Detected Image", img)
cv.waitKey(0)




