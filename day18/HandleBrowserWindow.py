from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# Wait for and click OrangeHRM, Inc link
link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']")))
link.click()
windowsIDs = driver.window_handles

#Approach1
# parentWindowId = windowsIDs[0]
# childWindowId = windowsIDs[1]
#
# print("Parent:", parentWindowId)
# print("Child:", childWindowId)
#
# driver.switch_to.window(childWindowId)
# print("title of the child window :",driver.title)
#
#
# driver.switch_to.window(parentWindowId)
# print("title of the parent window :",driver.title)

#Approach2

# for winid in windowsIDs:
#     driver.switch_to.window(winid)
#     print(driver.title)


#Close specific browser windows   1 2 3
for winid in windowsIDs:
    driver.switch_to.window(winid)
    if driver.title=="OrangeHRM HR Software | Free HR Software | HRMS | HRIS" or driver.title=='XYZ':
        driver.close()


driver.close()