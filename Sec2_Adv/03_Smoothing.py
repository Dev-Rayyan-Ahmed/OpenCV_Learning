import cv2 as cv

img = cv.imread(r'Resources\Photos\cats.jpg')

avg = cv.blur(img, (3,3))
cv.imshow('avg', avg )

guass = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('guass', guass)

median = cv.medianBlur(img, 3)
cv.imshow('median', median)

bilaterl = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilaterl)


cv.waitKey(0)