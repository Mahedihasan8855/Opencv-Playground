import cv2 as cv
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


#function for rescaleframe
def rescaleframe(frame, scale=0.2):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimention=(width,height)

    return cv.resize(frame,dimention,interpolation=cv.INTER_AREA)


rescaled_image=rescaleframe(img)
image_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY) # Band W image
image_blur=cv.GaussianBlur(img,(15,15),0)# blur ( ) blur
image_canny=cv.Canny(img,100,200) #edge in the images




cv.imshow("rescaled_image_showing",image_canny)
cv.waitKey(0)
cv.destroyAllWindows()




#cv.imshow("resized_image",resized_image)
cv.waitKey(0)
cv.destroyAllWindows()

while True:
    isTrue, frame=vid.read()
    frame_resized=rescaleframe(frame)

    cv.imshow("playing_video resized",frame_resized)
    if cv.waitKey(1) & 0xFF==ord('f') :
        break

vid.release()
cv.destroyAllWindows()