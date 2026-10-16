import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_myfirst")


#Switch to frame
driver.switch_to.frame("iframeResult")    #String id/name of the frame

#click on date & time button from IFrame
driver.find_element(By.XPATH,"//button[contains(text(),'Click me to display Date and Time')]").click()
time.sleep(5)


#Switch back to main page
# driver.switch_to.parent_frame()
driver.switch_to.default_content()

#click on Open menu button from main page
driver.find_element(By.XPATH,"//a[@id='menuButton']").click()

time.sleep(10)

