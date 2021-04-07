import cv2 as cv
import numpy as np

kernel=np.ones((5,5),np.uint8)
path="image/rose.jpg"
road=cv.imread("image/road.jpg",1)
rose=cv.imread(path,1)

img1=cv.resize(rose,(300,300),None,1,1)
img2=cv.resize(road,(300,300),None,1,1)

#showing image horizontally & vertically

hor=np.hstack((img1,img2))
ver=np.vstack((img1,img2))

cv.imshow("Horizontal",hor)
cv.waitKey(0)
cv.imshow("Vertical",ver)
cv.waitKey(0)


#videos in horizontal
cap=cv.VideoCapture(0)

framewidth=640
frameheight=360
cap=cv.VideoCapture(0)
cap.set(4,framewidth)
cap.set(5,frameheight)
while True:
    success,img=cap.read()
    v1 = cv.resize(img, (300, 300), None, 1, 1)
    v2 = cv.resize(img, (300, 300), None, 1, 1)
    hl=np.hstack((v1,v2))
    vl=np.vstack((v1,v2))
    cv.imshow("Horizontal Live",hl)
    cv.imshow("vertical Live", vl)
    if cv.waitKey(1) & 0xff==ord("f"):
        break
