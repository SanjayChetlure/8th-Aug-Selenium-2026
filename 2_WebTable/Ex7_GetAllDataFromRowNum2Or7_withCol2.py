import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

multipleData=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[position()=2 or position()=7]/td[4]")

for eachData in multipleData:
   print(eachData.text)



