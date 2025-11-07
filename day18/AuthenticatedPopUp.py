import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("/usr/local/bin/chromedriver")
driver=webdriver.Chrome(service=serv_obj)

#driver.get("http://the-internet.herokuapp.com/basic_auth")
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")

driver.maximize_window()
time.sleep(5)