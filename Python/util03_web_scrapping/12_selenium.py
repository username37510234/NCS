from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome() #"./chromedriver.exe"
browser.get("http://naver.com")

elem = browser.find_element(By.CLASS_NAME, "link_login")
elem.click()

browser.find_element(By.ID,"id").send_keys("naver_id")
browser.find_element(By.ID,"pw").send_keys("password")

browser.find_element(By.CLASS_NAME,"btn_login").click()

time.sleep(3)
browser.quit()