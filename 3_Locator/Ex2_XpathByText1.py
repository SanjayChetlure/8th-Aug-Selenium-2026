import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://testautomationpractice.blogspot.com/")

#click on Apple link
driver.find_element(By.XPATH,"//a[text()='Apple']").click()

time.sleep(20)