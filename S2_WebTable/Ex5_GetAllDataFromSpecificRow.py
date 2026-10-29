import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

multipleCols=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[2]/td")

for eachCol in multipleCols:
   print(eachCol.text)



