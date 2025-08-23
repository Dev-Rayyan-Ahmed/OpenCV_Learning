import cv2 as cv 
import numpy as np

img = cv.imread(r'Resources\Photos\park.jpg')
cv.imshow('Park',img)

def translate(img, x, y):
    translateMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])

    return cv.warpAffine(img, translateMat, dimensions)

translated = translate(img, 100, 100)
# cv.imshow('Translated', translated)


## Rotation
def rotate(img, angle, rotPoint= None):
    height, width = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, scale= 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
# cv.imshow("Rotated", rotated)


## Resizing
resized = cv.resize(img, (500,500), interpolation= cv.INTER_AREA)
# cv.imshow('Resized', resized)

## Flipped
flipped = cv.flip(img, 0)
# 0 vertically, 1 Horizontally, -1 Both
cv.imshow('Flipped', flipped)


cv.waitKey(0)