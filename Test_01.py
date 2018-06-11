import numpy as np
import cv2
img=cv2.imread("Test_01.png",1)
black=np.zeros([150,200,1],'uint8')
cv2.imshow("Black.png",black)
ones=np.ones([150,200,3],'uint8')
cv2.imshow("Ones.png",ones)

color= ones.copy()
color[:,:]=(255,255,0)
cv2.imshow("Test_01 Output.png",color)
print(color[0,0,:])
print(ones[0,0,:])
print(black[0,0,:])



cv2.waitKey(0)
cv2.destroyAllWindows()
