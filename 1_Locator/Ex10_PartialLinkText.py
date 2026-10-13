import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
time.sleep(2)
driver.get("file:///D:/Python/Workspace/8th-Aug-Selenium-2026/Html%20Files/linkText_PartialLinkText.html")

#click on facebook link
driver.find_element(By.PARTIAL_LINK_TEXT, "book").click()

time.sleep(5)