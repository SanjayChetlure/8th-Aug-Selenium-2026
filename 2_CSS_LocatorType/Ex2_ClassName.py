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


#Enter Name
# driver.find_element(By.CSS_SELECTOR,"input.form-control").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR,"*.form-control").send_keys("abc")
driver.find_element(By.CSS_SELECTOR,".form-control").send_keys("abc")






time.sleep(10)
