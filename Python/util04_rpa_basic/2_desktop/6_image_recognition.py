import pyautogui
# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# 속도 개선 방법
# file_menu = pyautogui.locateOnScreen("file_menu.png", grayscale=True)
# pyautogui.click(file_menu)

# 범위 지정
# file_menu = pyautogui.locateOnScreen("file_menu.png", region=(x,y,width,height))
# pyautogui.click(file_menu)

# 정확도 조정
# file_menu = pyautogui.locateOnScreen("file_menu.png", confidence=0.2)
# pyautogui.click(file_menu)


# file_menu = pyautogui.locateOnScreen("file_menu.png")
# if file_menu:
#     pyautogui.click(file_menu)
# else:
#     print("발견 실패")

# while file_menu is None:
#     file_menu = pyautogui.locateOnScreen("file_menu.png")
#     print("발견 실패")
    
# pyautogui.click(file_menu)

import time
import sys

# timeout = 10
# start = time.time()
# file_menu = None
# while file_menu is None:
#     file_menu = pyautogui.locateOnScreen("file_menu.png")
#     end = time.time()
#     if end - start > timeout:
#         print("시간 종료")
#         sys.exit()
        
# pyautogui.click(file_menu)

def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file,timeout=30):
    target = find_target(img_file,timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program.")
        sys.exit()
        
my_click("file_menu.png",10)