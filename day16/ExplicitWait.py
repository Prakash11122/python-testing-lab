from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=serv_obj)

mywait = WebDriverWait(driver, 10)  # Explicit Wait ✅

driver.get("https://www.google.com/")
driver.maximize_window()

searchbox = driver.find_element(By.NAME, 'q')
searchbox.send_keys("Selenium")
searchbox.submit()

mywait.until(EC.presence_of_element_located((By.XPATH, "//h3[normalize-space()='Selenium']")))

driver.quit()