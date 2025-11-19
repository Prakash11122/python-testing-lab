import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

serv_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
# RegisterLink=Keys.COMMAND+Keys.RETURN
# driver.find_element(By.LINK_TEXT,"Register").send_keys(RegisterLink)


#New Tab - Selenium4 :  Opens a new tab and switches to new tab

# driver.get("https://www.opencart.com/")
# driver.switch_to.new_window('tab')
# driver.get("https://www.orangehrm.com/")


#New Window - Selenium4 :  Opens a new browser window and switches to new window
driver.get("https://www.opencart.com/")
driver.switch_to.new_window('window')
driver.get("https://www.orangehrm.com/")





time.sleep(5)













