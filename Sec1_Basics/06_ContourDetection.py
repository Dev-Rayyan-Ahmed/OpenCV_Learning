import cv2 as cv

img = cv.imread(r'C:\Coding (VScode)\Codes\.CodingTools\OpenCV_Learning\Resources\Photos\cats.jpg')
cv.imshow('cat',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
# canny = cv.Canny(blur, 125,175)
# cv.imshow('canny', canny)

ret, thresh = cv.threshold(gray, 125, 225, cv.THRESH_BINARY)
cv.imshow('thresh',thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

import numpy as np
blank = np.zeros(img.shape, dtype='uint8')
cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow('countors', blank)


cv.waitKey(0)