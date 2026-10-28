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

networkSpeedOfChrome=driver.find_element(By.XPATH,"//table[@id='taskTable']//td[text()='Chrome']//parent::tr/td[contains(text(),'Mbps')]").text
print(networkSpeedOfChrome)

cpuValueOfFirefox=driver.find_element(By.XPATH,"//table[@id='taskTable']//td[text()='Firefox']//parent::tr/td[contains(text(),'%')]").text
print(cpuValueOfFirefox)

time.sleep(20)