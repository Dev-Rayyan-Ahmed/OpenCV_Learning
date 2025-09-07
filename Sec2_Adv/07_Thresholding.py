import cv2 as cv

img = cv.imread(r"Resources\Photos\cats.jpg")
cv.imshow("IMG", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 120, 255, cv.THRESH_BINARY)
# cv.imshow("Simple Thresholded", thresh)

threshold, thresh_Inv = cv.threshold(gray, 120, 255, cv.THRESH_BINARY_INV)
# cv.imshow("Simple Thresholded", thresh_Inv)

## Adaptive Thresholding
adaptive_threshold = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("adaptive_threshold", adaptive_threshold)



cv.waitKey(0)