import cv2
import numpy as np

img = cv2.imread('newspaper.jpg')

width, height = 640,240

src = np.array([[510,352],[1012,344],[1116,580],[461,581]], dtype=np.float32)
dst = np.array([[0,0],[width,0],[width,height],[0,height]], dtype=np.float32)

matrix = cv2.getPerspectiveTransform(src,dst)
result = cv2.warpPerspective(img, matrix,(width,height))
# 사다리꼴 이미지


img2 = cv2.imread('poker.jpg')

width, height = 530,710

src = np.array([[702,143],[1133,414],[726,1007],[276,700]], dtype=np.float32)
dst = np.array([[0,0],[width,0],[width,height],[0,height]], dtype=np.float32)

matrix2 = cv2.getPerspectiveTransform(src,dst)
result2 = cv2.warpPerspective(img2, matrix2,(width,height))
# 회전된 이미지 세우기


cv2.imshow('img',img)
cv2.imshow('img2',img2)
cv2.imshow('result',result)
cv2.imshow('result2',result2)
cv2.waitKey(0)
cv2.destroyAllWindows()