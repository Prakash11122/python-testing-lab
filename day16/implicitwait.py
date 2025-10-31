from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)# seconds  # implicit wait
driver.get("https://www.google.com/")
driver.maximize_window()


searchBox = driver.find_element(By.NAME, 'q')
searchBox.send_keys("Selenium")
searchBox.submit()


driver.find_element(By.XPATH, "//h3[normalize-space()='Selenium']").click()
driver.quit()