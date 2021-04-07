import cv2 as cv
import numpy as np
path="image/king.jpg"
king=cv.imread(path,1)
king=cv.resize(king,(600,400),None,1,1)







cv.imshow("original",king)
cv.waitKey(0)
print(king.shape)