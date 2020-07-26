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


key = Fernet.generate_key()
PATH = "C:\Program Files (x86)\chromedriver.exe"
#PATH = "/mnt/c/Program Files (x86)/chromedriver.exe"

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
download_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'export_trigger')))
time.sleep(0.5)
download_btn.click()

#dropboxGrandparent = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'ext_export_format_dropdown')))
#dropbox = dropboxGrandparent.find_element_by_xpath("//div/input[2]")#"//div/input/@value='0'"
dropbox = driver.find_elements_by_class("x-layer")
print(dropbox)
#csv = dropbox.find_element_by_xpath("//div/div[2]")
#driver.execute_script('arguments[0].setAttribute("class", "x-combo-list x-combo-selected")', csv)
#dropbox.send_keys("")   
#driver.execute_script('arguments[0].setAttribute("value", "CSV (Comma-Separated Values)")', dropbox)
#dropbox.send_keys(Keys.RETURN)
start = driver.find_element_by_id("Parameters_StartDate")
driver.execute_script("arguments[0].setAttribute('value', '06/21/2020')", start)
end = driver.find_element_by_id("Parameters_EndDate")
driver.execute_script("arguments[0].setAttribute('value', '07/21/2020')", end)

confirm_btn = driver.find_element_by_id("export_transactions_confirm_button")
confirm_btn.click()
time.sleep(5)

""" for account in accounts:
    account.click()
    download_btn = WebDriverWait(driver, 5).until(lambda d: d.find_element_by_id("export_trigger"))
    download_btn.click()
    dropbox = WebDriverWait(driver, 5).until(lambda d: d.find_element_by_id("ext-gen12"))
    driver.send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.RETURN)
    time.sleep(5) """
    

driver.quit()    
