from os import PRIO_PGRP

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.core.driver import Driver

serv_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

#is_displayed()   is_enabled()
searchbox=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("Display Status:",searchbox.is_displayed())#True
print("enable Status:",searchbox.is_enabled())#True


#is_selected() - for radio buttons and check boxes
sl_male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
sl_female=driver.find_element(By.XPATH,"//input[@id='gender-female']")

print("default radio buttons status.....")
print(sl_male.is_selected())#False
print((sl_female.is_selected()))#False


sl_male.click()
print("After selecting male radio button.....")
print(sl_male.is_selected())#True
print(sl_female.is_selected())#False

sl_female.click()
print("After selecting female radio button.....")
print(sl_male.is_selected())
print(sl_female.is_selected())

