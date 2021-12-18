import cv2
import numpy as np 
def sketch(image):
    img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    img_gray_blur = cv2.GaussianBlur(img_gray,(4,5),0)
    canny_edges = cv2.Canny(img_gray_blur,10,60)
    ret,mask = cv2.threshold(canny_edges,60,240,cv2.THRESH_BINARY_INV)
    return mask 

cam = cv2.VideoCapture(0)# for live if want to use a precorded video , enter path of video in place of "0"

while(True):
    ret,frame = cam.read()
    cv2.imshow("Live Sketch 😁 " , sketch(frame))
    if(cv2.waitKey(1) == 13):
        break

cam.release()
cv2.destroyAllWindows()    
