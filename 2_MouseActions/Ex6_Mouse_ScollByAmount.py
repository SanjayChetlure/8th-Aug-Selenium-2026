import time
from threading import Thread

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")


act=ActionChains(driver)

#Scroll down -> 1st Para: 0, 2nd Para: +ve   pixel values
act.scroll_by_amount(0,800).perform()
time.sleep(5)


#Scroll up -> 1st Para: 0, 2nd Para: -ve   pixel values
act.scroll_by_amount(0,-600).perform()
time.sleep(3)


#Scroll right -> 1st Para: +ve, 2nd Para: 0   pixel values
# act.scroll_by_amount(300,0).perform()


#Scroll left -> 1st Para: -ve, 2nd Para: 0   pixel values
# act.scroll_by_amount(-150,0).perform()


time.sleep(20)

