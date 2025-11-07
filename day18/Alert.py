from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

# open alert window
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(5)


alertWindow=driver.switch_to.alert

print(alertWindow.text)
alertWindow.send_keys("prakash")

#alertWindow.accept() #close alert window by using OK Button
alertWindow.dismiss()#close alert window by using cancel button
time.sleep(5)