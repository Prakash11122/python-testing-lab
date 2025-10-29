from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://admin-demo.nopcommerce.com/login")


# emailBox=driver.find_element(By.XPATH,"//input[@id='Email']")
#
# emailBox.clear()
# emailBox.send_keys("prakash@gmail.com")
#
# print("Result of task is :", emailBox.text)#printing Nothing "because inner text is nothing so print nothing"
# print("Result of get_attribute is :", emailBox.get_attribute('value')) #print:  prakash@gmail.com


login=driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
print("Result of task is :", login.text)
print("Result of get_attribute is :", login.get_attribute('value'))
print("Result of get_attribute is :", login.get_attribute('Type'))












