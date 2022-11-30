import cv2

# img = cv2.imread('img_cat.jpg', cv2.IMREAD_GRAYSCALE)


# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.imwrite('img_cat_gray.png',img)



cap = cv2.VideoCapture('vid_cat.mp4')

# 코덱 정의
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter('output.avi',fourcc,fps,(width,height))
# 저장 파일명, 코덱, FPS, 크기 (width,height)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    out.write(frame) # 소리없이 영상만 저장
    cv2.imshow('video',frame)
    if cv2.waitKey(1) == ord('q'):
        break
    
out.release()
cap.release()
cv2.destroyAllWindows()

# codec = 'DIVX'
# print(codec)
# print(*codec)
# print([codec])
# print([*codec])