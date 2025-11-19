import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()

Countries_List=driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
print(len(Countries_List))

for country in Countries_List:
    if country.text=="India":
        country.click()
        break
time.sleep(5)















