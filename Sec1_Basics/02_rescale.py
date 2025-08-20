import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation= cv.INTER_AREA)

def ChangeRes(width,height):
    """Only Works on Live Videos"""
    # capture.set(3, width) # 3 reference to width property in capture_Class
    # capture.set(4, height) # similary 4 -> Height

img = cv.imread('Resources/Photos/cat_large.jpg')
img_resized = rescaleFrame(img, 0.2)
cv.imshow('CAT',img_resized)



### Reading Resized Videos

# capture = cv.VideoCapture('Resources/Videos/dog.mp4')
# while True:
#     isTrue, frame = capture.read()

#     frame_resized = rescaleFrame(frame,0.2)

#     cv.imshow("Video",frame)
#     cv.imshow("Video_Resized",frame_resized)



#     if cv.waitKey(20) & 0xFF==ord("d"):
#         break

# capture.release()
# cv.destroyAllWindows()

cv.waitKey(0)