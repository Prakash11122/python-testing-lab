from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.ID,"password").send_keys("admin123")
driver.find_element(By.ID,"").click()
act_title=driver.title
exp_title="OrangeHRM"

if act_title == act_title:
    print("✅ Login Test Passed")
else:
    print("❌ Login Test Failed")
driver.quit()