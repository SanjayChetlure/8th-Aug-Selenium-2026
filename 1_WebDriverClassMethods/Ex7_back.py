import time
from selenium import webdriver


driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get("https://www.facebook.com/")
time.sleep(2)
driver.get("https://www.google.com/")
time.sleep(2)
driver.back()

a


time.sleep(10)