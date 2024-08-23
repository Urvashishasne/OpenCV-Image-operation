import cv2 
import numpy 

img1 = cv2.imread('cv2 work\\images\\nature.jpg')
img1= cv2.resize(img1,(500,500)) 

txt=cv2.putText(img = img1,
text = "TEXT",
org = (60,100), #for downside of img make y axis value greater 
fontFace = cv2.FONT_HERSHEY_DUPLEX ,
fontScale = 3 ,
color = (0,0,255),
thickness = 3,
lineType = cv2.LINE_8,
bottomLeftOrigin = False) 
cv2.imshow("text_image",txt)
cv2.waitKey(0)
cv2.destroyAllWindows()
