import cv2

img = cv2.imread('img_cat.jpg')

# dst = cv2.resize(img, (400,500))
dst = cv2.resize(img,None, fx=0.6, fy=0.6)


cv2.imshow('img',img)
cv2.imshow('resize',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()



cap = cv2.VideoCapture('vid_cat.mp4')


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # frame_resized = cv2.resize(frame, (400,500))
    frame_resized = cv2.resize(frame, None, fx=0.5,fy=0.5, interpolation=cv2.INTER_CUBIC)
    
    cv2.imshow('video',frame_resized)
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
