import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()

# Switch to iframe correctly
iframe = driver.find_element(By.ID, "iframeResult")
driver.switch_to.frame(iframe)

field1 = driver.find_element(By.ID, "field1")
field1.clear()
field1.send_keys("Hello RichMan")

CopyText=driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
act=ActionChains(driver)

act.double_click(CopyText).perform()# double click action



time.sleep(5)


