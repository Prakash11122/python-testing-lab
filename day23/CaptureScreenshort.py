import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

serv_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()


# driver.save_screenshot("/Users/prakashpradhan/PycharmProjects/PythonSelenium/day23/screentShort.png")
# driver.save_screenshot(os.getcwd()+"/homwpage.png")
driver.get_screenshot_as_file(os.getcwd()+"/homwpage1.png")



driver.quit()