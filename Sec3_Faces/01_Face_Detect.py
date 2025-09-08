import cv2 as cv

img = cv.imread("Resources\Photos\group 1.jpg")
cv.imshow("Img", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
haar_cascade = cv.CascadeClassifier("Sec3_Faces\haar_face.xml")

face_rects = haar_cascade.detectMultiScale(gray, scaleFactor= 1.01, minNeighbors= 2)

for (x,y,w,h) in face_rects:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness= 2)

cv.imshow("Detected Face", img)

cv.waitKey(0)