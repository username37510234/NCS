from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio")

time.sleep(0.5)
iframe = browser.find_element(By.ID,"iframeResult")
browser.switch_to.frame(iframe) 
# 탐색 오류 아이프레임 포커스 구분

elem = browser.find_element(By.XPATH,'/html/body/form/input[4]')

elem.click()

time.sleep(2)