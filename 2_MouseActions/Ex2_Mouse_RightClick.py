import time
from threading import Thread

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in/")
time.sleep(5)

Bestsellers=driver.find_element(By.XPATH,"(//a[text()='Bestsellers'])[1]")

act=ActionChains(driver)

#Apr1
# act.move_to_element(Bestsellers).perform()
# act.context_click().perform()

#Apr2
# act.move_to_element(Bestsellers).context_click().perform()

#Apr3
act.context_click(Bestsellers).perform()





time.sleep(20)