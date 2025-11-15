from selenium import webdriver
from selenium.webdriver import ActionChains
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

# Hover and navigate to Users page
admin = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@class='oxd-main-menu-item active']//span[1]")))
userMgmt = wait.until(EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='User Management']")))
users = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Users']")))

actions = ActionChains(driver)
actions.move_to_element(admin).move_to_element(userMgmt).move_to_element(users).click().perform()