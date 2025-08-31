import cv2 as cv
img = cv.imread(r"Resources\Photos\park.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('hsv',hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('lab',lab)

import matplotlib.pyplot as plt
plt.imshow(img)
plt.show()

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(rgb)
plt.show()




cv.waitKey(0)
