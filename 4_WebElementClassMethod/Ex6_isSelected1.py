import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://testautomationpractice.blogspot.com/")

result=driver.find_element(By.XPATH,"//input[@id='sunday']").is_selected()
print(result)

if result:
    print("Checkbox is selected")
else:
    print("Checkbox is not selected")

time.sleep(5)



