import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

serv_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()


#Capture Cookies from the browser
cookies=driver.get_cookies()
print("number of cookies: ",len(cookies))

#Print details of all cookies

for allCookiesDetails in cookies:
    #print(allCookiesDetails)
    print(allCookiesDetails.get('name'),":",allCookiesDetails.get('value'))

#Add new cookie to the browser

driver.add_cookie({"name":"Hanuman", "value":"0055"})
HanumanCookies=driver.get_cookies()
print("Size of cookies after adding new one:",len(HanumanCookies))

#Delete specific cookie from the browser
driver.delete_cookie("Hanuman")
HanumanCookies=driver.get_cookies()
print("Size of cookies after adding new one:",len(HanumanCookies))


#Delete all teh cookies
driver.delete_all_cookies()
HanumanCookies=driver.get_cookies()
print("Size of cookies after adding new one:",len(HanumanCookies))



