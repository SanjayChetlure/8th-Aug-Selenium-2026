import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://testautomationpractice.blogspot.com/")

# driver.find_element("Locator Type")
# driver.find_element(By.locatorName,"locator value")
# driver.find_element(By.XPATH,"Xpath xpression")

#Enter Name
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("xyz")

#Enter Email
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("abc@gmail.com")






time.sleep(20)