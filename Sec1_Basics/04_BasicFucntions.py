import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')
# cv.imshow('ColorFul Park', img)


## Turning Img to GrayScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

## Blurring Img (Gaussian Blur)

blur_cons = cv.GaussianBlur(img, (3,3), cv.BORDER_CONSTANT)
blur_def = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# cv.imshow('Blur_Cons', blur_cons)
# cv.imshow('Blur_Def', blur_def)


# Edge Cascade
canny = cv.Canny(blur_def, 125,175)
# cv.imshow('Canny', canny)


## Dilating an Image
dilated = cv.dilate(canny, (3,3), iterations=1)
# cv.imshow('dilated', dilated)

## Eroding 
eroded = cv.erode(dilated, (5,5), iterations=2)
# cv.imshow('eroded', eroded)

## Resize
resized = cv.resize(img, (500,500), interpolation= cv.INTER_AREA)
# cv.imshow('resized', resized) 

## Cropping
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)