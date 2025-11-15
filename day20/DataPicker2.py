import time
from select import select

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.core.driver import Driver

serv_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

#Date of birth
driver.find_element(By.XPATH,"//input[@id='dob']").click()#opens date picker

datepicker_month=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
datepicker_month.select_by_visible_text("Oct")

datepicker_Year=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
datepicker_Year.select_by_visible_text("1999")











