import cv2 
import numpy  
#read an image 
img1 = cv2.imread('cv2 work\\images\\nature.jpg')
img2 = cv2.imread('cv2 work\\images\\mix_colors.jpg')
#change the size the image 
img1 = cv2.resize(img1,(300,300))
img2 = cv2.resize(img2,(300,300))
#horizontal addition
h= numpy.hstack((img1,img2))
#vertical addition
v= numpy.vstack((img1,img2))
# make the grid 
grid = numpy.concatenate((h,h))
cv2.imshow("Horizontal addition of images ",h)
cv2.imshow("Vertical addition of images ",v)
cv2.imshow("Grid of images ",grid)

cv2.waitKey()
cv2.destroyAllWindows()







