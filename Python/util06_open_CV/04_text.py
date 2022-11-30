import cv2
import numpy as np

# cv2.FONT_HERSHEY_SIMPLEX 보통 크기의 산 세리프 글꼴
# cv2.FONT_HERSHEY_PLAIN 작은 크기의 산 세리프 글꼴
# cv2.FONT_HERSHEY_SCRIPT_SIMPLEX 필기체 스타일 글꼴
# cv2.FONT_HERSHEY_TRIPLEX 보통크기의 산 세리프 글꼴
# cv2.FONT_ITALIC 기울임

img = np.zeros((480,640,3), dtype=np.uint8) # 480 * 640 3 CHANNEL 에 해당하는 스케치북
img[:] = (0,0,0)


Colr = (255,255,255)
thicks = 2
Scale= 1

# cv2.putText(img, "FONT_HERSHEY_SIMPLEX",(20,50),cv2.FONT_HERSHEY_SIMPLEX,Scale,Colr,thicks)
# # 그릴 위치, 텍스트 내용, 시작 위치, 폰트 종류, 크기, 색깔, 두께
# cv2.putText(img, "FONT_HERSHEY_PLAIN",(20,150),cv2.FONT_HERSHEY_PLAIN,Scale,Colr,thicks)
# cv2.putText(img, "FONT_HERSHEY_SCRIPT_SIMPLEX",(20,250),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,Scale,Colr,thicks)
# cv2.putText(img, "FONT_HERSHEY_TRIPLEX",(20,350),cv2.FONT_HERSHEY_TRIPLEX,Scale,Colr,thicks)
# cv2.putText(img, "FONT_ITALIC",(20,450),cv2.FONT_ITALIC,Scale,Colr,thicks)

from PIL import ImageFont, ImageDraw, Image # PIL = Python Image Library

def myPutText(src,text,pos,font_size,font_color):
    img_pil = Image.fromarray(src)
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype('fonts/gulim.ttc',font_size)
    draw.text(pos,text, font=font,fill=font_color)
    return np.array(img_pil)

# cv2.putText(img, "폰트",(20,50),cv2.FONT_HERSHEY_SIMPLEX,Scale,Colr,thicks)
img = myPutText(img, "한글폰트",(20,50),30,Colr)



cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()