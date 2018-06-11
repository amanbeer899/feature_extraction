import numpy as np
import cv2

image = cv2.imread("Test_01.png",1)
gray= cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
cv2.resize(image,(0,0), fx=0.5,fy=0.5)
cv2.imshow("OG",image)
height,width = gray.shape[0:2]
binary = np.zeros([height,width,1],'uint8')
thresh = 139

for row in range(0,height):
    for col in range (0,width):
        if gray[row][col]>thresh:
            binary[row][col]=0
        else:
            binary[row][col]=255
cv2.resize(binary,(0,0), fx=0.5,fy=0.5)
cv2.imshow("Slow Binary",binary)


ret, thresh = cv2.threshold(binary,thresh,255,cv2.THRESH_BINARY)
cv2.imshow("CV Threshold",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
