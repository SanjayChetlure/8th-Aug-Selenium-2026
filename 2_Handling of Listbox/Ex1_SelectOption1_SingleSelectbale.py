import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

#step1: Identify the listbox
country=driver.find_element(By.XPATH,"//select[@id='country']")

#2:create object of Select class which accepts the listbox element as argument
s=Select(country)

#3: call Select methods (selectByIndex, selectByValue, selectByVisibleText)
# s.select_by_index(5)                  #int index
# s.select_by_visible_text("India")     #String text
s.select_by_value("china")              #string value


time.sleep(10)
