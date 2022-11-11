from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.maximize_window()

url = "http://air.gmarket.co.kr/gm/init/lp/lpMain.do"
browser.get(url)

time.sleep(0.5)
browser.find_element(By.CLASS_NAME,"form__input-day.form__input--placeholder-shown").click()

time.sleep(0.5)
browser.find_element(By.LINK_TEXT,"27").click()
time.sleep(0.5)
browser.find_element(By.LINK_TEXT,"28").click()
time.sleep(0.5)
browser.find_element(By.XPATH,"/html/body/div[4]/div/div[1]/div[2]/div/div[2]/div/div[2]/ul/li[1]/ul/li[1]/a").click()
time.sleep(1)
browser.find_element(By.XPATH,"/html/body/div[4]/div/div[1]/div[2]/div/div[2]/div/div[2]/ul/li[2]/a").click()
time.sleep(0.5)
browser.find_element(By.XPATH,"/html/body/div[4]/div/div[1]/div[2]/div/div[2]/div/div[2]/ul/li[2]/ul/li[1]/a").click()
time.sleep(0.5)
browser.find_element(By.XPATH,"/html/body/div[4]/div/div[1]/div[2]/div/div[1]/form/fieldset/div[2]/div[5]/button").click()

try:
    elem = browser.find_element(By.XPATH,"/html/body/div[3]/div[6]/div[4]/ul/li[1]/div[1]/table/tbody/tr/td[4]/div/div/ul/li[1]/div")

    print(elem.text)
finally:
    browser.quit()
