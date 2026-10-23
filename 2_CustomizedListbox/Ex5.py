import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

name=driver.find_element(By.XPATH,"//input[@id='name']")
name.send_keys("xyz")
time.sleep(2)


#Select All & Delete
name.send_keys(Keys.CONTROL + "a")
name.send_keys(Keys.DELETE)
time.sleep(2)

#Enter new value
name.send_keys("abc")
time.sleep(10)
