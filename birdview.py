import cv2 as cv
import numpy as np
path="image/king.jpg"
king=cv.imread(path,1)


pts1=np.float32([[178,52],[324,49],[233,204],[408,192]]) #image pixels of 4 point
pts2=np.float32([[0,0],[300,0],[0,400],[300,400]])# setting the image
matrix=cv.getPerspectiveTransform(pts1,pts2)
image_output=cv.warpPerspective(king,matrix,(300,400))




cv.imshow("warp_Prespective",image_output)
cv.waitKey(0)
print(king.shape)