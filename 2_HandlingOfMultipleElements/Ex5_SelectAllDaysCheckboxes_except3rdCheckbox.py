import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

allCheckboxes=driver.find_elements(By.XPATH,"//input[@class='form-check-input' and  @type='checkbox']")
print(len(allCheckboxes))

count=1   #4
for eachCheckbox in allCheckboxes:
    if count !=3:
        eachCheckbox.click()
        time.sleep(1)
    count+=1


time.sleep(5)

