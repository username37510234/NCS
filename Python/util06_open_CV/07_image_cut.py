import cv2

img = cv2.imread('img_cat.jpg')

crop = img[100:200, 300:400]
# img[100:200, 400:600] = crop






cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()