import cv2 as cv

img = cv.imread(r'Resources\Photos\park.jpg')
b, g, r = cv.split(img)

# cv.imshow('Blue', b)
print(b.shape)
print(img.shape)

merged = cv.merge([b,g,r])
# cv.imshow('merged', merged)

import numpy as np
blank = np.zeros(img.shape[:2], dtype= 'uint8')
blued = cv.merge([b,blank,blank])
cv.imshow('blued', blued)


cv.waitKey(0)