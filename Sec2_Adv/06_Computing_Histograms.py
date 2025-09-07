import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread(r"Resources\Photos\cats 2.jpg")
cv.imshow("Img", img)

## Gray Hist

grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',grayscale)

#masking
import numpy as np
blank = np.zeros(img.shape[:2], dtype= "uint8")
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# masked_img = cv.bitwise_and(grayscale,grayscale, mask= mask)
# cv.imshow("MaskedImg", masked_img)

# gray_hist = cv.calcHist([grayscale], [0], masked_img, [256], [0,256])

# plt.figure()
# plt.title("GrayScale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("No. of Pixels")
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()


## Color Hist
colors = ("b","g","r")
masked_img = cv.bitwise_and(img,img, mask= mask)

plt.figure()
plt.title("GrayScale Histogram")
plt.xlabel("Bins")
plt.ylabel("No. of Pixels")
for i,color in enumerate(colors):
    hist = cv.calcHist([img],[i], mask, [256], [0,256])
    plt.plot(hist, color= color)
    plt.xlim([0,256])

plt.show()






cv.waitKey(0)