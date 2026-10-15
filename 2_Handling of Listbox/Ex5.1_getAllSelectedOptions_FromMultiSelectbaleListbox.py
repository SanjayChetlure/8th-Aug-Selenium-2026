import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

colors=driver.find_element(By.XPATH,"//select[@id='colors']")
s=Select(colors)

s.select_by_index(1)
s.select_by_index(2)
s.select_by_index(3)
time.sleep(2)

allSelectedOptionsAddress=s.all_selected_options     #[webElement1, webElement2, webElement3]

for eachSelectedOptionAddress in allSelectedOptionsAddress:
    s1=eachSelectedOptionAddress.text
    print(s1)

time.sleep(10)
