from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

browser.get("https://shopping.naver.com/home")

time.sleep(0.2)

browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div[1]/div/input').send_keys('무선마우스')

browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div[1]/div/button[2]').click()

time.sleep(1)

# browser.execute_script('window.scrollTo(0, 1080)')
# time.sleep(1)

# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

prev_height = browser.execute_script('return document.body.scrollHeight')
interval = 2
while True:
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    
    time.sleep(interval)
    
    curr_height = browser.execute_script('return document.body.scrollHeight')
    if curr_height == prev_height:
        break
    
    prev_height = curr_height

time.sleep(1)
time.sleep(3)