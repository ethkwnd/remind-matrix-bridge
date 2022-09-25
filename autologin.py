from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

username = "remindbridge@gmail.com"
password = "123remind##"

url = "https://www.remind.com/log_in"

driver = webdriver.Chrome("/Users/sekhargajula/Downloads/chromedriver")

driver.get(url)

driver.maximize_window() # For maximizing window
driver.implicitly_wait(20) # gives an implicit wait for 20 seconds


enterUser = driver.find_element(By.ID, "id-8")
enterUser.send_keys(username)
enterUser.submit()

enterPass = driver.find_element(By.ID, "id-9")
enterPass.send_keys(password)
enterPass.submit()

driver.implicitly_wait(20) # gives an implicit wait for 20 seconds

enterCode = driver.find_element(By.ID, "id-11")
authCode = input("Enter confirmation code: ")
enterCode.send_keys(authCode)
enterCode.submit()

print("logged in successfully")

