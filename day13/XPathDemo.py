from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.flipkart.com/")
driver.maximize_window()

# Close popup if appears
try:
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@role='button']"))
    ).click()
except:
    print("Popup not found or already closed")

# Wait for search box
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='q']"))
)
search_box.send_keys("T-shirts")

# Wait for search button to be clickable
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)
search_button.click()

print("✅ Search successful!")
driver.quit()