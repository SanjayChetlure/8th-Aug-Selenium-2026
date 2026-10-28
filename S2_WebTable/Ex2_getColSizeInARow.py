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

allColAddress=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[4]/td")
print(len(allColAddress))

colSize=len(allColAddress)
print(colSize)