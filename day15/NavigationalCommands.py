from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.core.driver import Driver

serv_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=serv_obj)


driver.get("https://www.amazon.in/")
driver.get("https://www.flipkart.com/")

driver.back()
driver.forward()

driver.refresh()

driver.quit()











