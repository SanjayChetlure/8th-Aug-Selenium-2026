import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

print("--staring browser--")
driver=webdriver.Edge()
print("--started browser--")
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")



# Enter Email
driver.find_element(By.CSS_SELECTOR,"input[placeholder*='er EM']").send_keys("xyz")




time.sleep(10)
