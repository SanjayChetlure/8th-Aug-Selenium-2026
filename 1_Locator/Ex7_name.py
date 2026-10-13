import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(2)
driver.get("file:///D:/Python/Workspace/8th-Aug-Selenium-2026/Html%20Files/name.html")

#Enter FN
driver.find_element(By.NAME,"abc123").send_keys("abc")


#Enter LN
driver.find_element(By.NAME,"abc456").send_keys("xyz")


time.sleep(5)