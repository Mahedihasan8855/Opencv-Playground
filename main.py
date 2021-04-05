import cv2 as cv
import numpy as np
path="image/rose.jpg"
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
def ressized_frame(frame,scale=.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim=(width,height)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)




#function for rescaleframe
def rescaleframe(frame, scale=0.2):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimention=(width,height)

    return cv.resize(frame,dimention,interpolation=cv.INTER_AREA)

resized_image=ressized_frame(img)
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


print(2+2)
print("2"+"2")
