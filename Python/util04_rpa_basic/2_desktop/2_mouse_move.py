import pyautogui

pyautogui.moveTo(100,100, duration=1)
pyautogui.moveTo(200,200, duration=0.5)
pyautogui.moveTo(300,300, duration=0.25)

pyautogui.move(300,-100, duration=0.05)
print(pyautogui.position())