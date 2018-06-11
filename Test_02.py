import numpy as np
import cv2

imagery= cv2.imread("Test.jpg",1)
cv2.imshow("Internot",imagery)
cv2.moveWindow("Internot",0,0)
print(imagery.shape)
height,width,channel = imagery.shape

b,g,r= cv2.split(imagery)

rgb_split = np.empty([height,width*3,3],'uint8')
rgb_split[:,0:width]=cv2.merge([b,b,b])
rgb_split[:,width:width*2]=cv2.merge([g,g,g])
rgb_split[:,width*2:width*3]=cv2.merge([r,r,r])
hsv=cv2.cvtColor(imagery,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv)
hsv_split=np.concatenate((h,s,v),axis=1)
cv2.imshow("HSVSplit.png",hsv_split)

cv2.imshow("InterNu.png",rgb_split)

cv2.waitKey(0)
cv2.destroyAllWindows()
