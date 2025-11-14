import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Login
wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Navigate to Users page
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Admin']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='User Management']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Users']"))).click()

# Wait for the table to load
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='oxd-table-body']")))

# Correct locator for rows
rows = driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")

print("Total Number of Rows in this page :", len(rows))

# Print status values (column 5)
for r in rows:
    status = r.find_element(By.XPATH, "./div[@role='cell'][5]").text
    print("Status:", status)


# ---- USERNAMES ----
usernames = driver.find_elements(
    By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']//div[@role='cell'][2]"
)
print("Total Usernames:", len(usernames))
for u in usernames:
    print(u.text)

# ---- EMPLOYEE NAMES ----
employee_names = driver.find_elements(
    By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']//div[@role='cell'][4]"
)
print("Total Employee Names:", len(employee_names))
for e in employee_names:
    print(e.text)

time.sleep(3)
driver.quit()