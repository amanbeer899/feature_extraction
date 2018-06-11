import numpy as np
import cv2

canvas = np.ones((500,500,3),'uint8')*255
radius=3
bl=0;gr=0;re=0
color = (bl,gr,re)
pressed= False
def click(event,x,y,flags,param):
    global canvas
    global pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(canvas,(x,y),radius, color, -1)
        pressed = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if pressed == True:
            cv2.circle(canvas,(x,y),radius,color,-1)
    elif event== cv2.EVENT_LBUTTONUP:
        pressed = False

cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas",click)

while True:
    cv2.imshow("canvas",canvas)
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break
    if ch & 0xFF == ord('b'):
        bl=255
        color = (bl,gr,re)
    if ch & 0xFF == ord('g'):
        gr=255
        color = (bl,gr,re)
    if ch & 0xFF == ord('r'):
        re=255
        color = (bl,gr,re)
    if ch & 0xFF == ord('e'):
        bl=0;gr=0;re=0
        color = (bl,gr,re)
    if ch & 0xFF == ord('m'):
        radius+=1
    if ch & 0xFF == ord('n'):
        radius-=1

cv2.destroyAllWindows()
