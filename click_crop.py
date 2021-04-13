import cv2 as cv
import numpy as np
path="image/king.jpg"
king=cv.imread(path,1)

circles=np.zeros((4,2),np.uint)
counter=0


def show_pixel(event, x, y, flags, param):
    global counter
    if event == cv.EVENT_LBUTTONDOWN:
        print(x,y)
        circles[counter]=x,y
        counter= counter +1
        print(circles)

while True:
    if counter==4:
        width = 300
        height = 400
        pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])  # image pixels of 4 point
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])  # setting the image
        matrix = cv.getPerspectiveTransform(pts1, pts2)
        image_output = cv.warpPerspective(king, matrix, (width, height))
        cv.imshow("output image",image_output)

    for x in range(0,4):
        cv.circle(king,(circles[x][0],circles[x][1]),5,(0,0,255),cv.FILLED)
    cv.imshow("Frame", king)
    cv.setMouseCallback("Frame", show_pixel)
    cv.waitKey(1)