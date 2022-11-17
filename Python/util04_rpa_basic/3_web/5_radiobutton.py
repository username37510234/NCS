from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio")

time.sleep(0.2)
browser.switch_to.frame('iframeResult')

elem = browser.find_element(By.XPATH,'//*[@id="age1"]')

if elem.is_selected() == False:
    print("선택 안되어 있으므로 선택하기")
    elem.click()
else:
    print("선택 되어 있으므로 아무것도 안함")
    
time.sleep(2)