import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

# startStopEle=driver.find_element(By.XPATH,"//button[@name='start' or @name='stop']")
# startStopEle=driver.find_element(By.XPATH,"//button[text()='START' or text()='STOP']")

# startStopEle=driver.find_element(By.XPATH,"//button[starts-with(@name,'st')]")
startStopEle=driver.find_element(By.XPATH,"//button[starts-with(text(),'ST')]")



#click on Start
startStopEle.click()
time.sleep(3)

#click on STOP
startStopEle.click()
time.sleep(3)

#click on Start
startStopEle.click()
time.sleep(3)

time.sleep(15)

