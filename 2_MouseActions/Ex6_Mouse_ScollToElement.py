import time
from threading import Thread

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(3)

act=ActionChains(driver)

footerLinkEle=driver.find_element(By.XPATH,"//h2[text()='Footer Links']")
act.scroll_to_element(footerLinkEle).perform()
time.sleep(8)


mobileLabelsEle=driver.find_element(By.XPATH,"//h4[text()='Mobile Labels']")
act.scroll_to_element(mobileLabelsEle).perform()



time.sleep(20)