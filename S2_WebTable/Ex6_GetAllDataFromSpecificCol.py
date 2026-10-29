import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

multipleRows=driver.find_elements(By.XPATH,"//table[@name='BookTable']//td[2]")

for eachRow in multipleRows:
   print(eachRow.text)



