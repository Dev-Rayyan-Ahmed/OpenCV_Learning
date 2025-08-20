import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype="uint8")
# print(blank)
# cv.imshow("blank",blank)

# Paint Img a particular color:

# blank[:] = 0,255,0 # changing all values
# blank[200:300,300:400] = 0,0,255 # Specific Area

# cv.imshow("Green",blank)


# Draw Rectangle

# cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=cv.FILLED,)
# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=cv.FILLED,)

# cv.imshow("Rectangle", blank)

# Draw Circle:
# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2), radius=50, color=(0,0,255), thickness=-1)
# cv.imshow("Circle", blank)

# Draw line:
# cv.line(blank,(0,0), (blank.shape[1]//2,blank.shape[0]//2), color=(0,0,255), thickness=10)
# cv.imshow("Line", blank)


# Put Text on Img
cv.putText(blank, "Hello, My Name is Rayyan", (15,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow("line", blank)

cv.waitKey(0)