import time
from threading import Thread

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

allRowsAddress=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
print(len(allRowsAddress))

rowSize=len(allRowsAddress)
print(rowSize)