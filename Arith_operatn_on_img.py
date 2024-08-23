import cv2 
import numpy 

#reading image  
img1 = cv2.imread('cv2 work\\images\\nature.jpg')
img2 = cv2.imread('cv2 work\\images\\mix_colors.jpg')
#change size of image so that it will fully shown 
img1=cv2.resize(img1,(500,500))
img2=cv2.resize(img2,(500,500))
#lets add images 
add = cv2.addWeighted(img1,0.5,img2,0.4,0)
#subtracting two images 
sub = cv2.subtract(img1,img2)
cv2.imshow("Added Image",add)
cv2.imshow("subtract image",sub)
cv2.waitKey(0)
cv2.destroyAllWindows()


