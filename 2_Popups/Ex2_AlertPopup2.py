import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.guru99.com/test/delete_customer.php")
time.sleep(2)

#ENter Customer Id
driver.find_element(By.XPATH,"//input[@name='cusid']").send_keys("1234")

#click on submit button
driver.find_element(By.XPATH,"//input[@name='submit']").click()
time.sleep(2)

#Switch to Alert popup
alt=driver.switch_to.alert

#getText from Alert popup
Textvalue=alt.text
print(Textvalue)


#click on cancel button from alert popup
# alt.dismiss()

#click on OK button from 1st alert popup
alt.accept()
time.sleep(2)

#click on OK button from 2nd alert popup
alt.accept()





time.sleep(10)


