import numpy as np
import cv2
color=cv2.imread("blacktest.png",1)
gray= cv2.cvtColor(color,cv2.COLOR_RGB2GRAY)
cv2.imwrite("gray.jpg",gray)
"""b = color[:,:,0]
g = color[:,:,1]
r = color[:,:,2]

rgba = cv2.merge((b,g,r,b))
cv2.imwrite("rgba.png",rgba)
"""
black_mask = np.all(color == 0, axis=-1)
alpha = np.uint8(np.logical_not(black_mask)) * 255
bgra = np.dstack((color, alpha))
cv2.imwrite("rgba.png", bgra)
