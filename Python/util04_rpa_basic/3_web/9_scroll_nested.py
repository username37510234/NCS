from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome()

browser.get("https://www.w3schools.com/html/default.asp")
time.sleep(0.5)
browser.maximize_window()

elem = browser.find_element(By.XPATH,'//*[@id="leftmenuinnerinner"]/a[62]')

# 방법1
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()

# 방법2
xy = elem.location_once_scrolled_into_view
print("type : ",type(xy))
print("value : ",xy)

elem.click()

time.sleep(2)