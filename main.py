import cv2 as cv
import numpy as np
path="image/rose.jpg"
road=cv.imread("image/road.jpg",1)
img= cv.imread(path,1)
vid=cv.VideoCapture("video/dog.mp4")
'''
print(img.shape)
cv.imshow("rose_image.jpg",img)
cv.waitKey(0)
cv.destroyAllWindows()
'''
#resized_image=cv.resize(img,(int(img.shape[1]),int(img.shape[0]/2)))

resized_image=cv.resize(img,(0,0),fx=.4,fy=.4)

#fuction for resizing image
def resized_frame(frame,scale=.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim=(width,height)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)


def square(frame):
    w,h=400,400
    return cv.resize(frame,(w,h))


#function for rescaleframe
def rescaleframe(frame, scale=0.2):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimention=(width,height)

    return cv.resize(frame,dimention,interpolation=cv.INTER_AREA)

resized_image=resized_frame(img)
rescaled_image=rescaleframe(img)
image_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY) # Band W image
image_blur=cv.GaussianBlur(img,(7,7),0)# blur ( ) blur
image_canny=cv.Canny(img,150,200) #edge in the images

#morphological transformation
kernel=np.ones((5,5),np.uint8)

image_dialation=cv.dilate(image_canny,kernel,iterations=1)
image_erosion=cv.erode(image_dialation,kernel,iterations=1)
image_gradient = cv.morphologyEx(image_canny, cv.MORPH_GRADIENT, kernel)
image_blackhat = cv.morphologyEx(image_canny, cv.MORPH_BLACKHAT, kernel)

cv.imshow("image_showing",image_erosion)

cv.waitKey(0)


#playing video and 0xFF==ord("f") for close window clicking f
while True:
    isTrue, frame=vid.read()
    frame_resized=rescaleframe(frame)

    cv.imshow("playing_video resized",frame_resized)
    if cv.waitKey(1) & 0xFF==ord('f') :
        break


#webcamera live video..

framewidth=640
frameheight=360
cap=cv.VideoCapture(0)
cap.set(4,framewidth)
cap.set(5,frameheight)
while True:
    success,img=cap.read()
    cv.imshow("Live",img)
    if cv.waitKey(1) & 0xff==ord("f"):
        break



# Crop and Resizing the images

print(road.shape)
sq=square(road)
cv.imshow("road",road)
cv.imshow("sqaure_image",sq)
cv.waitKey(0)
print(sq.shape)

#Cropping
crop_image=road[300:553,358:600] #[height:width]=[px:px : px:px]
cv.imshow("Cropped Image",crop_image)
cv.waitKey(0)

#Drawing shapes and text in images

blank_white= 255*np.ones([512,512,3],np.uint8)
blank_black=np.zeros([512,512,3],np.uint8)

blank_black[0:512,256:512]=252,0,0 #change the color px to px
blank_white[256:512,0:512]=252,1,1 # chang the clr to px to px
blank_white[:]=255,1,1             #turn white image to blue

#line, rectangle, circle, putText, ellipse
black_img=np.zeros([500,500,3],np.uint8)

'''
To draw a Line
For drawing a line cv2.line() function is used. This function takes five arguments

Image object on which to draw
Starting point coordinates (x, y)
End point coordinates (x, y)
Stroke color in BGR (not RGB, to be noted)
Stroke thickness (in pixels)
'''
cv.line(black_img,(0,0),(500,500),(0,255,0),2)

'''
To draw a Rectangle
For drawing a rectangle cv2.rectangle() function is used. This function accepts five input parameters.

Image object on which to draw
Coordinates of the vertex at the top left (x, y)
Coordinates of the lower right vertex (x, y)
Stroke color in BGR (not RGB, to be noted)
Stroke thickness (in pixels)
'''

cv.rectangle(black_img,(50,300),(260,450),(255, 0, 0),2)


'''
To draw a circle
For drawing a circle, cv2.circle() function is used. This function accepts five input parameters.

Image object on which to draw
Center coordinates (x, y)
Radius of the circle
Stroke color in BGR (not RGB, to be noted)
Stroke thickness (in pixels)
'''

cv.circle(black_img,(350,150),100,(0, 0, 255),2)

'''
To draw the text
To write text with OpenCV there is cv2.putText() function that accepts a number of arguments.

The image on which to draw
The text to be written
Coordinates of the text start point
Font to be used
Font size
Text color
Text thickness
The type of the line used
'''
cv.putText(black_img,"Mahedi Hassan",(10,250),cv.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),1,cv.LINE_AA)

cv.imshow("Black",black_img)
cv.waitKey(0)




