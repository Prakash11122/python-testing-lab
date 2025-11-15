import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)

year = "2024"
month = "November"
date = "20"

# Open the date picker
driver.find_element(By.ID, "datepicker").click()

while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mon == month and yr == year:
        break
    else:
        # driver.find_element(By.XPATH, "//a[@title='Next']").click()
        driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[1]/span").click()
        time.sleep(3)

# Select date
driver.find_element(By.XPATH, f"//a[text()='{date}']").click()