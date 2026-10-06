import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://testautomationpractice.blogspot.com/")

#click on Simple Alert button
driver.find_element(By.XPATH,"//button[text()='Simple Alert']").click()

time.sleep(20)