import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

# Enter Name
driver.find_element(By.CSS_SELECTOR,"input[class='form-control']:nth-of-type(1)").send_keys("abc")

# Enter Email
driver.find_element(By.CSS_SELECTOR,"input[class='form-control']:nth-of-type(2)").send_keys("xyz")

# Enter Phone Num
driver.find_element(By.CSS_SELECTOR,"input[class='form-control']:nth-of-type(3)").send_keys("9999999999")




time.sleep(10)
