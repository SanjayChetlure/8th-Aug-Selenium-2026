import time
from selenium import webdriver


driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get("https://www.facebook.com/")

actTitle=driver.title
expTitle="Facebook"

if actTitle==expTitle:
    print("navigate to correct webpage")
else:
    print("navigate to wrong webpage")

time.sleep(10)