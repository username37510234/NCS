import cv2

# cap = cv2.VideoCapture('vid_cat.mp4')

# while cap.isOpened():
#     ret, frame = cap.read() # ret 성공여부, frame 받아온 이미지(프레임)
#     if not ret:
#         print('더 이상 가져올 프레임이 없어요')
#         break
    
#     cv2.imshow('video',frame)
    
#     if cv2.waitKey(1) == ord('q'):
#         print('사용자 입력에 의해 종료합니다')
#         break
    
# cap.release()
# cv2.destroyAllWindows()

cap = cv2.VideoCapture(0) # 0번째 카메라 장치 (Device ID)

if not cap.isOpened():
    exit()
    
while True:
    ret, frame = cap.read()
    if not ret:
        print('더 이상 가져올 프레임이 없어요')
        break
    
    cv2.imshow('camera',frame)
    
    if cv2.waitKey(1) == ord('q'):
        print('사용자 입력에 의해 종료합니다')
        break
    
cap.release()
cv2.destroyAllWindows()