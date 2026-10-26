import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

# allCheckboxes=driver.find_elements(By.XPATH,"(//div[@class='form-group'])[4]//input[@type='checkbox']")
allCheckboxes=driver.find_elements(By.XPATH,"//input[@class='form-check-input' and  @type='checkbox']")
print(len(allCheckboxes))

#select all checkboxes
for eachCheckbox in allCheckboxes:
    eachCheckbox.click()
    time.sleep(1)


time.sleep(5)

