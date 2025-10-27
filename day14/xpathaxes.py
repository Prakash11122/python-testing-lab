from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By




serv_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

#self
# text_sms= driver.find_element(By.XPATH,"//a[normalize-space()='Gravita India Ltd.']/self::a").text
# print(text_sms) #Gravita India Ltd.

#parent
# text_sms = driver.find_element(By.XPATH,"//a[normalize-space()='Gravita India Ltd.']/parent::td").text
# print(text_sms)  #Gravita India Ltd.

#child
# text_sms = driver.find_elements(By.XPATH,"//a[normalize-space()='Gravita India Ltd.']/ancestor::tr/child::td")
# print(len(text_sms))
# driver.close()


#ancestor
# ancestor = driver.find_element(By.XPATH,"//a[normalize-space()='Gravita India Ltd.']/ancestor::tr").text
# print(ancestor)
# driver.close()

#Decendant
# decendants=ancestor = driver.find_elements(By.XPATH,"//a[normalize-space()='Gravita India Ltd.']/ancestor::tr/descendant::*")
# print("Number of Decendant", len(decendants))

#following
# followings=ancestor = driver.find_elements(By.XPATH,"//a[normalize-space()='Gravita India Ltd.']/ancestor::tr/following::*")
# print("Number od following",len(followings))


#following-sibling
# followings_sibling = driver.find_elements(By.XPATH,"//a[normalize-space()='Gravita India Ltd.']/ancestor::tr/following-sibling::*")
# print("Number od followings_sibling",len(followings_sibling))

#preceding
# preceding=ancestor = driver.find_elements(By.XPATH,"//a[normalize-space()='Gravita India Ltd.']/ancestor::tr/preceding::*")
# print("Number of preceding",len(preceding))


#preceding
preceding_sibling=driver.find_elements(By.XPATH,"//a[normalize-space()='Gravita India Ltd.']/ancestor::tr/preceding-sibling::*")
print("Number of preceding_sibling",len(preceding_sibling))
