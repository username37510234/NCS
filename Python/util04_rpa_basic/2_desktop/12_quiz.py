import pyautogui


pyautogui.hotkey("win","r")
pyautogui.write("mspaint")
pyautogui.hotkey("enter")
pyautogui.sleep(0.2)
fw = pyautogui.getWindowsWithTitle("제목 없음")[0]
fw.activate()
fw.maximize()
pyautogui.sleep(0.5)
# pyautogui.mouseInfo()n
pyautogui.click(332,71)
pyautogui.click(60,191)

import pyperclip
pyperclip.copy("참 잘했어요")
pyautogui.hotkey("ctrl","v")

pyautogui.sleep(5)
fw.close()
pyautogui.hotkey("n")