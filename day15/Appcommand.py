from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")

print(driver.title)
print(driver.current_url)
driver.close()













