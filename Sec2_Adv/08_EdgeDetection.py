import cv2 as cv
import numpy as np

img = cv.imread("Resources\Photos\park.jpg")
cv.imshow('img', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))

# cv.imshow("Laplacian", lap)

## Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1,0)
sobely = cv.Sobel(gray, cv.CV_64F, 0,1)
sobel_combined = cv.bitwise_or(sobelx, sobely)

cv.imshow("Sobel X", sobelx)
cv.imshow("Sobel Y", sobely)
cv.imshow("Sobel", sobel_combined)


cv.waitKey(0)
