from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

opt=webdriver.ChromeOptions()
opt.add_argument("--disable-notificatins")

serv_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=serv_obj, options=opt)
driver.get("https://whatmylocation.com/")
driver.maximize_window()

time.sleep(5)