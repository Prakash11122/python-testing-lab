from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.facebook.com/")
driver.maximize_window()

#Tag & ID (OR) #id
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR,"#email").send_keys("abc")


# Tag & class (OR) .class
#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("abc@gmail.com")

# Tag & attribute (OR) [attribute=value]
#driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal-email]").send_keys("abc@gmail.com")
#driver.find_element(By.CSS_SELECTOR,"[data-testid=royal-email]").send_keys("abc@gmail.com")

# tag , class & attribute
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal-pass]").send_keys("xyz")


