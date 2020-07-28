from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import getpass
#add beautiful soup library

key = Fernet.generate_key()
PATH = "./browserDrivers/chromedriver.exe"
#PATH = "/mnt/c/Program Files (x86)/chromedriver.exe"

user = input("Enter UserName: ")
password = getpass.getpass("Enter password: ")


driver = webdriver.Chrome(PATH)
driver.get("https://cuaonline.cuofamerica.com/MyAccountsV2")

#login
username = WebDriverWait(driver, 5).until(lambda d:d.find_element_by_id("UserName"))
username.send_keys(user)
passwd = driver.find_element_by_id("Password")
passwd.send_keys(password + Keys.RETURN)

#get list of accounts
accounts = WebDriverWait(driver, 5).until(lambda d: d.find_elements_by_class_name("account"))


#for account in accounts:
accounts[0].click()#select account
download_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'export_trigger')))
time.sleep(0.5)
download_btn.click()#click download
drop = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "x-form-text")))
drop.click()#open dropbox

dropbox_items = WebDriverWait(driver, 5).until(lambda d: d.find_elements(By.CLASS_NAME,"x-combo-list-item"))
dropbox_items[1].click()#select csv
   
#select start/end date
start = driver.find_element_by_id("Parameters_StartDate")
driver.execute_script("arguments[0].setAttribute('value', '06/21/2020')", start)
end = driver.find_element_by_id("Parameters_EndDate")
driver.execute_script("arguments[0].setAttribute('value', '07/21/2020')", end)

confirm_btn = driver.find_element_by_id("export_transactions_confirm_button")
confirm_btn.click()#confirm date and format
time.sleep(5)

confirm_btn.send_keys(Keys.ESCAPE)#close side panel to get ready for next account

accounts[1].click()#select account
download_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'export_trigger')))
time.sleep(0.5)
download_btn.click()#click download
drop = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "x-form-text")))
drop.click()#open dropbox

dropbox_items = WebDriverWait(driver, 5).until(lambda d: d.find_elements(By.CLASS_NAME,"x-combo-list-item"))
dropbox_items[1].click()#select csv
   
#select start/end date
start = driver.find_element_by_id("Parameters_StartDate")
driver.execute_script("arguments[0].setAttribute('value', '06/21/2020')", start)
end = driver.find_element_by_id("Parameters_EndDate")
driver.execute_script("arguments[0].setAttribute('value', '07/21/2020')", end)

confirm_btn = driver.find_element_by_id("export_transactions_confirm_button")
confirm_btn.click()#confirm date and format
time.sleep(5)

confirm_btn.send_keys(Keys.ESCAPE)#close side panel to get ready for next account

time.sleep(5)
driver.quit()    

#process csv's
