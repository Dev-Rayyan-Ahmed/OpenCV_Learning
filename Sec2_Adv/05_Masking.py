import cv2 as cv
import numpy as np

img = cv.imread("Resources\Photos\cats 2.jpg")
blank = np.zeros(img.shape[:2], dtype= "uint8")
cv.imshow("Orignal", img)
cv.imshow("Blank", blank)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow("mask", mask)

masked_img = cv.bitwise_and(img, img, mask=mask)
cv.imshow("masked_img",masked_img) 

cv.waitKey(0)