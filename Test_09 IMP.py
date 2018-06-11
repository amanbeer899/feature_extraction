import numpy as np
import cv2

img= cv2.imread("Test_01.jpg",1)
img_half=cv2.resize(img,(0,0),fx=0.5,fy=0.5)
gray_double=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
gray=cv2.resize(gray_double,(0,0),fx=0.5,fy=0.5)
cv2.imshow("Original",img_half)

ret,thresh_basic=cv2.threshold(gray,138,255,cv2.THRESH_BINARY)

thresh_adapt=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
thresh_adapt_rgb= cv2.cvtColor(thresh_adapt,cv2.COLOR_GRAY2RGB)


final=cv2.bitwise_and(thresh_adapt_rgb,img_half)
cv2.imwrite("FinalV1.jpg",final)

black_mask = np.all(final == 0, axis=-1)
alpha = np.uint8(np.logical_not(black_mask)) * 255
bgra = np.dstack((final, alpha))
cv2.imshow("rgba.png", bgra)



cv2.waitKey()
cv2.destroyAllWindows()
