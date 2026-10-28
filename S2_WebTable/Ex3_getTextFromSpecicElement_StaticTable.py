import time
from threading import Thread

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

subjectNameOfBook_learnJS=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[3]/td[3]").text
print(subjectNameOfBook_learnJS )


authorNameOfBook_MasterInSelenium=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]/td[2]").text
print(authorNameOfBook_MasterInSelenium)