import cv2

img = cv2.imread('img_cat.jpg')

r_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
r_180 = cv2.rotate(img, cv2.ROTATE_180)
r_270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)




cv2.imshow('img',img)
cv2.imshow('img3',r_90)
cv2.imshow('img6',r_180)
cv2.imshow('img9',r_270)
cv2.waitKey(0)
cv2.destroyAllWindows()