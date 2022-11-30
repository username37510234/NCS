import cv2

img = cv2.imread('img_cat.jpg')


dst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel_3 = cv2.GaussianBlur(img, (3,3),0)
kernel_5 = cv2.GaussianBlur(img, (5,5),0)
kernel_7 = cv2.GaussianBlur(img, (7,7),0)

sigma_3 = cv2.GaussianBlur(img, (0,0),1)
sigma_5 = cv2.GaussianBlur(img, (0,0),2)
sigma_7 = cv2.GaussianBlur(img, (0,0),3)



cv2.imshow('img',img)
cv2.imshow('imgg',dst)
cv2.imshow('imgk3',kernel_3)
cv2.imshow('imgk5',kernel_5)
cv2.imshow('imgk7',kernel_7)
cv2.imshow('imgs3',sigma_3)
cv2.imshow('imgs5',sigma_5)
cv2.imshow('imgs7',sigma_7)
cv2.waitKey(0)
cv2.destroyAllWindows()