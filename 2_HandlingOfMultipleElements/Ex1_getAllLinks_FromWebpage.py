import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

allLinks=driver.find_elements(By.XPATH,"//a")      #[webElement1, webelement2, webelement3....]
print("Total Links in a webpage: ",len(allLinks))

for eachLink in allLinks:
    s1=eachLink.text
    print(s1)



time.sleep(10)

