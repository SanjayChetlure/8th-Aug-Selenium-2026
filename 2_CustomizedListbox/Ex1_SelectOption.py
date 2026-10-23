import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

#step1: Identify the listbox
country=driver.find_element(By.XPATH,"//select[@id='country']")

#step2: Open listbox option using click method
country.click()

#Arrow Down
country.send_keys(Keys.ARROW_DOWN)
time.sleep(1)
country.send_keys(Keys.ARROW_DOWN)
time.sleep(3)

#Arrow Up
country.send_keys(Keys.ARROW_UP)
time.sleep(1)

#Select option using Enter key
country.send_keys(Keys.ENTER)


time.sleep(10)
