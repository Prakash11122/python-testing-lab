from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://docs.oracle.com/javase/8/docs/api/?java/util/Collections.html")
driver.maximize_window()

# 1) packageListFrame -> java.util
driver.switch_to.frame("packageListFrame")
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "java.util"))).click()
driver.switch_to.default_content()

# 2) packageFrame -> AbstractQueue
driver.switch_to.frame("packageFrame")
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "AbstractQueue"))).click()
driver.switch_to.default_content()

# 3) classFrame -> Help
driver.switch_to.frame("classFrame")
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Help']"))).click()

driver.quit()