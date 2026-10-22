import time
from threading import Thread

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in/")
time.sleep(3)

allMenuOption=driver.find_element(By.XPATH,"//a[@id='nav-hamburger-menu']")

act=ActionChains(driver)

#Apr1
# act.move_to_element(allMenuOption).perform()
# act.click().perform()

#Apr2
# act.move_to_element(allMenuOption).click().perform()

#Apr3
act.click(allMenuOption).perform()





time.sleep(20)