import pyautogui

# fw = pyautogui.getActiveWindow()
# print(fw.title)
# print(fw.size)
# print(fw.left,fw.top,fw.right,fw.bottom)
# pyautogui.click(fw.left + 25, fw.top + 20)

# for w in pyautogui.getAllWindows():
#     if w.title == "":
#         pass
#     else:
#         print(w)
        
for w in pyautogui.getWindowsWithTitle("제목 없음"):
    print(w)
    
if w.isActive == False:
    w.activate()

if w.isMaximized == False:
    w.maximize()
    
pyautogui.sleep(0.5)

w.restore()

w.close()