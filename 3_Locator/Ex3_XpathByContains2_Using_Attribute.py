import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://testautomationpractice.blogspot.com/")

#Enter Name
driver.find_element(By.XPATH,"//input[contains(@placeholder,'Name')]").send_keys("abc")


#Enter Email
driver.find_element(By.XPATH,"//input[contains(@placeholder,'Name')]").send_keys("abc")

#Enter Address
driver.find_element(By.XPATH,"//textarea[contains(@id,'area')]").send_keys("xyz")



time.sleep(10)