from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/lenovo-thinkpad-carbon-laptop")
driver.maximize_window()

#for id locators
# ✅ Wait until the search box appears
wait = WebDriverWait(driver, 10)
# search_box = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
# search_box.send_keys("Lenovo Thinkpad Carbon Laptop")

#for name locators
# search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
# search_box.send_keys("Lenovo Thinkpad Carbon Laptop")


#LinkTest and partial linkText
# driver.find_element(By.LINK_TEXT,"Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Regis").click()