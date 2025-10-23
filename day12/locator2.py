from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.inmotionhosting.com/")
driver.maximize_window()

# Correct class name for slider container on this site
sliders = driver.find_elements(By.CLASS_NAME, "imh-rostrum-card")
print("Number of sliders:", len(sliders)) #8

links=driver.find_elements(By.TAG_NAME,'a')
print(len(links)) #  256 total number of links on home pages