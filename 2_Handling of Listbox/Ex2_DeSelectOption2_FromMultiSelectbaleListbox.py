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

#Apr1
s1=s.first_selected_option
firstSelectOptionValue=s1.text
print(firstSelectOptionValue)

# Apr2
firstSelectOptionValue2=s.first_selected_option.text
print(firstSelectOptionValue2)

# Apr3:
print(s.first_selected_option.text)
time.sleep(10)
