import cv2 
#reading image - using relative path of image
image = cv2.imread('nature.jpg') 
image = cv2.resize(image,(500,500))
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
angle = 45
scale = 0.5
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
rotated_image = cv2.warpAffine(image, rotation_matrix, (500, 500))
cv2.imshow('Real image',image)
cv2.imshow('Rotated image',rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()