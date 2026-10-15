import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

colors=driver.find_element(By.XPATH,"//select[@id='colors']")
s=Select(colors)

#Apr1
allOptionsAddress=s.options             #[webElement1, webElement2, webElement3]

size=len(allOptionsAddress)
print(size)

print(len(allOptionsAddress))

print("-----")

size2=len(s.options)
print(size2)

print(len(s.options))

time.sleep(10)
