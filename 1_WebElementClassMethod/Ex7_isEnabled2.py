import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://www.instagram.com/?hl=en")

result=driver.find_element(By.XPATH,"//span[text()='Log in']").is_enabled()
print(result)

if result:
    print("Element is enabled")
else:
    print("Element is disabled")


time.sleep(5)



