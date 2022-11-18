from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()

browser.get("https://flight.naver.com/")

time.sleep(0.2)
browser.maximize_window()

time.sleep(0.2)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/b').click()
time.sleep(0.2)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/button[2]').click()
browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/div/button[1]').click()

browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()

time.sleep(0.5)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[2]/button').click()
browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[2]').click()
time.sleep(0.5)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[4]/button').click()

browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[4]/div/div/button').click()

# try:
#     elem = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/div/div[1]/div[6]/div/div[3]/div[1]/div/div[1]')))
#     print(elem.text)
# except:
#     print("실패했어요")
time.sleep(7)
    
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[6]/div/div[3]/div[1]/div')
print(elem.text)
time.sleep(2)