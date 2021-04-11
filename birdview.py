import cv2 as cv
import numpy as np
path="image/king.jpg"
king=cv.imread(path,1)


pts1=np.float32([[178,52],[324,49],[233,204],[408,192]]) #image pixels of 4 point
pts2=np.float32([[0,0],[300,0],[0,400],[300,400]])# setting the image
matrix=cv.getPerspectiveTransform(pts1,pts2)
image_output=cv.warpPerspective(king,matrix,(300,400))

for x in range(0,4):
    cv.circle(king,(pts1[x][0],pts1[x][1]),5,(0,0,255),cv.FILLED)

cv.imshow("Point where warp",king)
cv.imshow("warp_Prespective",image_output)
cv.waitKey(0)
print(king.shape)