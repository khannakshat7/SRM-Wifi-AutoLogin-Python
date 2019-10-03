#Srm wifi Auto login 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

username = '' # Enter Your SRM Wifi Username 
password = '' # Enter Your SRM Wifi password

url = 'https://iac.srmist.edu.in/connect/PortalMain'  # SRM Wifi Login URL

driver = webdriver.Chrome("chromedriver_win32\\chromedriver.exe")  # Link to Chrome Driver

driver.get(url)
time.sleep(0.2)
try:
    driver.find_element_by_id('LoginUserPassword_auth_username').send_keys(username)
    driver.find_element_by_id('LoginUserPassword_auth_password').send_keys(password)
    driver.find_element_by_id('UserCheck_Login_Button').click()
except:
    driver.refresh()
    driver.find_element_by_id('LoginUserPassword_auth_username').send_keys(username)
    driver.find_element_by_id('LoginUserPassword_auth_password').send_keys(password)
    driver.find_element_by_id('UserCheck_Login_Button').click()
