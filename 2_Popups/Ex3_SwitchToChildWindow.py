import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://skpatro.github.io/demo/links/")
time.sleep(2)

#click on NewTab from main page
driver.find_element(By.XPATH,"//input[@name='NewTab']").click()
time.sleep(4)


#get child window ID
allIds=driver.window_handles      #[mainPageId[0], childWindowId[1]]
childWindowId=allIds[1]


#Switch to Child Window
driver.switch_to.window(childWindowId)      #String ChildWindowId


#click on Training Link from Child Window
driver.find_element(By.XPATH,"(//span[text()='Training'])[1]").click()





time.sleep(10)


