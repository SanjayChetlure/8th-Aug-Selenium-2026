import time
from threading import Thread

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in/")
time.sleep(2)

#1: Identify Mouse over element
SignIn=driver.find_element(By.XPATH,"//span[text()='Hello, sign in']")

#2: Create Object of ActionChain class
act=ActionChains(driver)

#3: call method - moveToElement to display option from mouse over
act.move_to_element(SignIn).perform()

time.sleep(5)
#click on wishlist element
driver.find_element(By.XPATH,"//span[text()='Your Wish List']").click()

time.sleep(20)