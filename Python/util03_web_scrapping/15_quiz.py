from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

browser = webdriver.Chrome()

url = "https://realty.daum.net/home/apt/map"
browser.get(url)

browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/div[1]/div/div[1]/input").send_keys("송파 헬리오시티")

time.sleep(1)
browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/div[2]/div").click()
browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/div[1]/div/div[2]/button").click()

time.sleep(1)
res = requests.get(browser.current_url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

informs = soup.find_all("div",attrs={"class":"css-1dbjc4n"})

for inform in informs:
    budong = inform.find("div",attrs={"class":"css-1563yu1"})
    
    print(budong)    

time.sleep(5)