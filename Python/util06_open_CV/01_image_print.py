import cv2

# print(cv2.__version__)

img = cv2.imread('img_cat.jpg')

cv2.imshow('cat', img) # cat이라는 이름이 창에 img 표시

# key = cv2.waitKey(0) # 지정된 시간 동안 사용자 키 입력 대기
# print(key)
# cv2.destroyAllWindows() # 모든 창 닫기

# cv2.IMREAD_COLOR 컬러이미지, 투명 영역은 무시(기본값)
# cv2.IMREAD_GRAYSCALE 흑백 이미지
# cv2.IMREAD_UNCHANGED 투명영역까지 포함

# img_c=cv2.imread('img_cat.jpg',cv2.IMREAD_COLOR)
# img_g=cv2.imread('img_cat.jpg',cv2.IMREAD_GRAYSCALE)
# img_u=cv2.imread('img_cat.jpg',cv2.IMREAD_UNCHANGED)

# cv2.imshow('cat c', img_c)
# cv2.imshow('cat g', img_g)
# cv2.imshow('cat u', img_u)

print(img.shape)







cv2.waitKey(0)
cv2.destroyAllWindows()