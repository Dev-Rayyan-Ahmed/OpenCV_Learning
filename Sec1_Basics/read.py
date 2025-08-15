import cv2 as cv

# Reading Images
# img = cv.imread("Resources/Photos/cat.jpg")
# cv.imshow('cat', img)

# Reading Videos
capture = cv.VideoCapture('Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow("Dog",frame)


    if cv.waitKey(20) & 0xFF==ord("d"):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)