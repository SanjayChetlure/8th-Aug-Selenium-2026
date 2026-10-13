import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://testautomationpractice.blogspot.com/")

start=driver.find_element(By.XPATH,"//button[text()='START']")
start.screenshot("D:\\Python\Batches\\8th Aug 2026 Python Automation\\Screenshot\start_button2.png")