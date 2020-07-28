from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import getpass
import functions
import time




#add beautiful soup library
#research requests to see if it's useful

#TODO: Use cryptography to save username/password

#key = Fernet.generate_key()

url = "https://cuaonline.cuofamerica.com/MyAccountsV2"

PATH = "./browserDrivers/chromedriver.exe"
#PATH = "/mnt/c/Program Files (x86)/chromedriver.exe"

#get bank login info
user = input("Enter UserName: ")
password = getpass.getpass("Enter password: ")


driver = webdriver.Chrome(PATH)
driver.get(url)

#login
username = WebDriverWait(driver, 5).until(lambda d:d.find_element_by_id("UserName"))
username.send_keys(user)
passwd = driver.find_element_by_id("Password")
passwd.send_keys(password + Keys.RETURN)


i = 1#cause apparently I need a counter for the dropbox list

#get list of accounts
accounts = WebDriverWait(driver, 5).until(lambda d: d.find_elements_by_class_name("account"))

date_params = functions.get_date_parameters()

for account in accounts:#download csv for each account
    account.click()
    
    download_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'export_trigger')))
    time.sleep(0.5)
    download_btn.click()#click download
    
    drop = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "x-form-text")))
    drop.click()#open dropbox
    
    dropbox_items = WebDriverWait(driver, 5).until(lambda d: d.find_elements(By.CLASS_NAME,"x-combo-list-item"))
    dropbox_items[i].click()#select csv

    #TODO: something with the dates is broken
    start = driver.find_element_by_id("Parameters_StartDate")
    driver.execute_script(date_params['start_date'], start)
    end = driver.find_element_by_id("Parameters_EndDate")
    driver.execute_script(date_params['end_date'], end)

    confirm_btn = driver.find_element_by_id("export_transactions_confirm_button")
    confirm_btn.click()#confirm date and format
    time.sleep(3)

    confirm_btn.send_keys(Keys.ESCAPE)#close side panel to get ready for next account
    
    time.sleep(3)
    
    i = i + 5 #increment counter for dropbox


driver.quit()    

#process csv's
