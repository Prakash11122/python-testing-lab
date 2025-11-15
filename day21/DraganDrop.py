import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

act=ActionChains(driver)

First_ele=driver.find_element(By.ID,"draggable")
Second_ele=driver.find_element(By.ID,"droppable")

act.drag_and_drop(First_ele,Second_ele).perform()

time.sleep(5)










