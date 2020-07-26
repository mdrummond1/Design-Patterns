from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import getpass


key = Fernet.generate_key()
PATH = "C:\Program Files (x86)\chromedriver.exe"

user = input("Enter UserName: ")
password = getpass.getpass("Enter password: ")

driver = webdriver.Chrome(PATH)
driver.get("https://cuaonline.cuofamerica.com/MyAccountsV2")


username = WebDriverWait(driver, 5).until(lambda d:d.find_element_by_id("UserName"))
username.send_keys(user)
passwd = driver.find_element_by_id("Password")
passwd.send_keys(password + Keys.RETURN)
#accounts = WebDriverWait(driver, 5).until(lambda d: d.find_elements_by_class_name("account"))
accounts = WebDriverWait(driver, 5).until(lambda d: d.find_elements_by_class_name("account"))
#account.click()
#download_btn = WebDriverWait(driver, 5).until(lambda d: d.find_element_by_id("export_trigger"))
#print(download_btn.get_attribute())

accounts[1].click()
download_btn = WebDriverWait(driver, 5).until(lambda d: d.find_element_by_id("export_trigger"))
download_btn.click()
dropbox = WebDriverWait(driver, 5).until(lambda d: d.find_element_by_name("format"))
dropbox.value = 54
dropbox.send_keys(Keys.RETURN)
time.sleep(5)

""" for account in accounts:
    account.click()
    download_btn = WebDriverWait(driver, 5).until(lambda d: d.find_element_by_id("export_trigger"))
    download_btn.click()
    dropbox = WebDriverWait(driver, 5).until(lambda d: d.find_element_by_id("ext-gen12"))
    driver.send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.RETURN)
    time.sleep(5) """
    

driver.quit()    
