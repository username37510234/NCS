from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download.default_directory':r'C:\NCS'})

browser = webdriver.Chrome(options=chrome_options)

browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download")

time.sleep(0.2)
browser.switch_to.frame('iframeResult')

elem = browser.find_element(By.XPATH,'/html/body/p[2]/a')
elem.click()

time.sleep(2)