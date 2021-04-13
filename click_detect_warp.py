import cv2 as  cv
import numpy as np





def show_pixel(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(f"The coordinates are : \nx:{x}\ny:{y}")



path="image/king.jpg"
img=cv.imread(path,1)
cv.imshow("Frame",img)
cv.setMouseCallback("Frame",show_pixel) #calling the function
cv.waitKey(0)