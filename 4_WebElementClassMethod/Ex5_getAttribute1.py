import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://testautomationpractice.blogspot.com/")


attrValue1=driver.find_element(By.XPATH,"//input[@id='name']").get_attribute("placeholder")
print(attrValue1)


attrValue2=driver.find_element(By.XPATH,"//input[@id='phone']").get_attribute("placeholder")
print(attrValue2)

time.sleep(5)



