import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

colors=driver.find_element(By.XPATH,"//select[@id='colors']")
s=Select(colors)


allOptionsAddress=s.options     #[webElement1, webElement2, webElement3]

for eacOptionAddress in allOptionsAddress:
    s1=eacOptionAddress.text
    print(s1)

time.sleep(10)
