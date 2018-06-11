import numpy as np
import cv2

img= cv2.imread("Test_01.png",1)
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("Original",img)

ret,thresh=cv2.threshold(gray,138,255,cv2.THRESH_BINARY)

_,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
thresh_rgb=cv2.cvtColor(thresh,cv2.COLOR_GRAY2RGB)

img2=thresh_rgb.copy()
index=-1
thickness=3
color=(0,0,255)

cv2.drawContours(img2, contours,index,color,thickness)
cv2.imshow("Contours",img2)

black_mask = np.all(img2 == 0, axis=-1)
alpha = np.uint8(np.logical_not(black_mask)) * 255
bgra = np.dstack((img2, alpha))
cv2.imwrite("rgba.png", bgra)

cv2.waitKey()
cv2.destroyAllWindows()



