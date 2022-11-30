import cv2

img = cv2.imread('img_cat.jpg')

flip_h = cv2.flip(img,1) # 좌우 대칭
flip_v = cv2.flip(img,0) # 상하 대칭
flip_b = cv2.flip(img,-1) # 전 대칭




cv2.imshow('img',img)
cv2.imshow('imgh',flip_h)
cv2.imshow('imgv',flip_v)
cv2.imshow('imgb',flip_b)
cv2.waitKey(0)
cv2.destroyAllWindows()