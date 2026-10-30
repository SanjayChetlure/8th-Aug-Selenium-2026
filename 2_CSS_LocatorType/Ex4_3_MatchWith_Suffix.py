import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

# click on start button
driver.find_element(By.CSS_SELECTOR,"input[placeholder$='EMail']").send_keys("xyz")




time.sleep(10)
