import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://testautomationpractice.blogspot.com/")


textValue=driver.find_element(By.XPATH,"//button[@id='alertBtn']").text
print(textValue)

tableName=driver.find_element(By.XPATH,"//h2[text()='Static Web Table']").text
print(tableName)

time.sleep(5)



