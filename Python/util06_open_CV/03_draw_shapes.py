import cv2
import numpy as np

img = np.zeros((480,640,3), dtype=np.uint8) # 480 * 640 3 CHANNEL 에 해당하는 스케치북
img[:] = (0,0,0) # 전체 공간을 흰 색으로 채우기
# print(img)


# img[100:200,200:300] = (125,125,125)


# cv2.LINE_4 : 상하좌우 4 방향으로 연결된 선
# cv2.LINE_8 : 대각선을 포함한 8 방향으로 연결된 선
# cv2.LINE_AA : 부드러운 선 (anti-aliasing)

Colr = (255,255,0)
thicks = 3
rads=50

# cv2.line(img,(50,100),(400,50),Colr,thicks,cv2.LINE_8)
# # 그릴 위치, 시작 점, 끝 점, 색깔, 두께, 선 종류
# cv2.line(img,(50,200),(400,150),Colr,thicks,cv2.LINE_4)
# cv2.line(img,(50,300),(400,250),Colr,thicks,cv2.LINE_AA)


# cv2.circle(img, (200,100), rads, Colr, thicks, cv2.LINE_AA) # 속이 빈 원
# # 그릴 위치, 원의 중심점, 반지름, 색깔, 두께, 선의 종류
# cv2.circle(img, (400,200), rads, Colr, cv2.FILLED, cv2.LINE_AA) # 꽉 찬 원


# cv2.rectangle(img, (100,100), (200,200), Colr, thicks)
# # 그릴 위치, 왼쪽 위 좌표, 오른쪽 아래 좌표, 색깔, 두께
# cv2.rectangle(img, (400,300), (500,400), Colr, cv2.FILLED)

pts1 = np.array([[100,100],[200,100],[100,200]])
pts2 = np.array([[200,100],[300,100],[300,200],[400,100]])
cv2.polylines(img, [pts1], True, Colr, thicks, cv2.LINE_AA)
cv2.polylines(img, [pts2], False, Colr, thicks, cv2.LINE_8)
# 그릴 위치, 그릴 좌표들, 닫힘 여부, 색깔, 두께, 선 종류

pts3= np.array([[300,300],[250,450],[375,350],[225,350],[350,450]])

cv2.fillPoly(img,[pts3],Colr,cv2.LINE_AA)
# 그릴 위치, 그릴 좌표들, 색깔, 선 종류



cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()