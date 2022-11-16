import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0]

w.activate()

# pyautogui.write("12345")
# pyautogui.write("OraenoCoding", interval=0.2)
# pyautogui.write("오래노코딩") 안됨 한글차별 ㅅㅂ

# pyautogui.write(["t","e","s","t","left","left","right","l","a","enter"],interval=0.2)
# test 적고 왼쪽두번 오른쪽 한번 커서 이동 la쓰고 엔터

# pyautogui.keyDown("shift")
# pyautogui.press("4")
# pyautogui.keyUp("shift")

# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("ctrl")

import pyperclip
pyperclip.copy("코딩")
pyautogui.hotkey("ctrl","v")

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")
    
my_write("너도코딩")

pyautogui.hotkey("ctrl","a")