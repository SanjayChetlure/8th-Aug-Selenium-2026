import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://www.saucedemo.com/")

result=driver.find_element(By.XPATH,"//input[@id='login-button']").is_enabled()
print(result)

if result:
    print("Element is enabled")
else:
    print("Element is disabled")


time.sleep(5)



