import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")


colors=driver.find_element(By.XPATH,"//select[@id='colors']")

s=Select(colors)

s.select_by_index(0)
s.select_by_visible_text("Blue")
s.select_by_value("green")

time.sleep(10)
