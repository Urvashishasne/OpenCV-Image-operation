#------Grey Scale of Image 
import cv2 
import numpy 

#reading image with channel = 0
img1 = cv2.imread('cv2 work\\images\\nature.jpg',0)
img1 = cv2.resize(img1,(500,500))
cv2.imshow("grey_scale_img",img1)

cv2.waitKey(0)
cv2.destroyAllWindows()


