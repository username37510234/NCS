from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

First_Name = "오래노"
Last_Name = "코딩"
Country = "Canada"
Subject = "퀴즈완료하였습니다."

browser.get("https://www.w3schools.com/")

time.sleep(0.2)
browser.maximize_window()
browser.find_element(By.XPATH,'//*[@id="main"]/div[2]/div/div[1]/a[1]').click()
time.sleep(0.2)
browser.find_element(By.XPATH,'//*[@id="topnav"]/div/div[1]/a[11]').click()
time.sleep(0.2)
browser.find_element(By.XPATH,'//*[@id="leftmenuinnerinner"]/a[118]').click()

time.sleep(0.2)
browser.find_element(By.XPATH,'//*[@id="fname"]').send_keys(First_Name)
browser.find_element(By.XPATH,'//*[@id="lname"]').send_keys(Last_Name)
browser.find_element(By.XPATH,'//*[@id="country"]/option[text()="{}"]'.format(Country)).click()
browser.find_element(By.XPATH,'//*[@id="main"]/div[3]/textarea').send_keys(Subject)

time.sleep(5)
browser.find_element(By.XPATH,'//*[@id="main"]/div[3]/a').click()

time.sleep(5)
browser.quit()