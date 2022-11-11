from PIL import ImageGrab
import time

time.sleep(5)

for i in range(1,11):
    img = ImageGrab.grab()
    img.save("image{}.png".format(i))
    time.sleep(2)