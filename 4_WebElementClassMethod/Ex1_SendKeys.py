import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://testautomationpractice.blogspot.com/")


#Enter Name
# Apr1:
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("abc")


#apr2:
# name=driver.find_element(By.XPATH,"//input[@id='name']")
# name.send_keys("abc")



time.sleep(5)



