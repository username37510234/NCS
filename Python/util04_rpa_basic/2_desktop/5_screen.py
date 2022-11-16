import pyautogui

# img = pyautogui.screenshot()
# img.save("screenshot.png")

pixel = pyautogui.pixel(812,33)
print(pixel)

print(pyautogui.pixelMatchesColor(812,33, (50,50,51)))
print(pyautogui.pixelMatchesColor(812,33, pixel))
print(pyautogui.pixelMatchesColor(812,33, (60, 60, 60)))
