import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

try:
    link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "OrangeHRM, Inc"))
    )
    link.click()
    print("✅ Link clicked successfully!")
except Exception as e:
    print("❌ Link not found or not clickable:", e)

time.sleep(5)
# driver.close()
driver.quit()