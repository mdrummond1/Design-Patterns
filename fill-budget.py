from functions import *
from selenium import common
from csv import reader
from os import listdir, remove
from os.path import isfile, join
from transaction import Transaction
#from cryptography.fernet import Fernet
#from cryptography.hazmat.backends import default_backend
#from cryptography.hazmat.primitives import hashes
#from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

#TODO: research beautiful soup and requests to see if it's useful
#TODO: possibly replace selenium if I can make the request directly, or use an api like plaid
#TODO: Use cryptography to save username/password


url = "https://cuaonline.cuofamerica.com/MyAccountsV2"
PATH = "./browserDrivers/chromedriver.exe"
ext = '.fin'

log_info = get_log_info()#get bank login info

driver = webdriver.Chrome(PATH)
driver.get(url)

login(log_info[0], log_info[1] , driver)#login
print("Logging in...")
i = 1#cause apparently I need a counter for the dropbox list

#get list of accounts
print("Collecting accounts...")
accounts = WebDriverWait(driver, 5).until(lambda d: d.find_elements_by_class_name("account"))
#TODO: add in checking for bad credentials, shown from timeout error when getting accounts
date_params = get_date_parameters()#generate dates
print("Setting dates...")

print("Downloading transactions...")
for account in accounts:#download csv for each account
    try:
        account.click()
    
        #print(account.get_attribute('data-account-identifier'))#maybe I can use this to get the date directly?
    
        wait_and_click('export_trigger', driver, 5)    

        drop = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "x-form-text")))
        drop.click()#open dropbox
    
        dropbox_items = WebDriverWait(driver, 5).until(lambda d: d.find_elements(By.CLASS_NAME,"x-combo-list-item"))
        dropbox_items[i].click()#select csv
        i = i + 5 #increment counter for dropbox

        input_dates(date_params, driver)#put date values into date selectors
        
        #click confirm
        confirm_btn = wait_and_click("export_transactions_confirm_button", driver, 5)
    
        time.sleep(2)#give the file time to download

        confirm_btn.send_keys(Keys.ESCAPE)#close side panel to get ready for next account
    
        time.sleep(1)#give the sidebar time to close
    
    except Exception  as  e:
        print("you can't do that")
        print(e)
        

driver.quit()  


#TODO: process csv's
#read-in files
path_to_csvs = get_downloads()

#Dictionary to check descriptions and categorize
categories = {
    'income' : ['VIA CHRISTI', 'STATE OF KANSAS', 'APY Earned'],
    'rent' : ['CHECK'],
    'phone' : ['ATT'],
    'credit cards' : ['CAPITAL ONE', 'PAYMENT FOR AMZ', 'CHASE CREDIT CRD'],
    'transportation' : ['PROG N WESTERN', 'QuikTrip'],
    'renters insurance' : ['STATE FARM'],
    'utilities' : ['COX', 'Evergy', 'KANSAS GAS', 'ATT', 'WASTELINK', 'CITY OF WICHITA'],
    'loans' : ['GREAT LAKES'],
    'gym' : ['YMCA'],
    'groceries' : ['Walmart', 'Aldi', 'Dillons', 'Dollar Tree'],
    'dining out' : ['Spangles', 'Braum\'s', 'Fazoli\'s', 'Saigon', 'Starbucks', 'Wichita Coffee'],
    'pets' : ['Sitstay'],
    'healthcare' : ['grene vision']
}


#build list of transaction files
csvs = [f for f in listdir(path_to_csvs) if isfile(join(path_to_csvs, f)) and 'ExportedTransactions' in f]

row_to_remove = 0#get rid of each file heading
readers = []

#add in a list or something to keep track of the different accounts

#open files and put into csv reader
for file in csvs:
    fl = open(path_to_csvs + file)
    readers.extend(reader(fl))
    readers.remove(readers[row_to_remove])
    row_to_remove = len(readers)
    fl.close()
    remove(path_to_csvs + file)#delete file, so we don't have repeat transactions

 
#clean the csv rows
t = clean_rows(readers, categories)


#put in categorizing below here!
#check for a categories file
if exists('cats.json') and getsize('cats.json') > 0:#if we have one, read the categories from it
    with open('cats.json', 'r') as fl:    
        categories = load(fl)
        fl.close()
        remove('cats.json')


#filters transactions based on category
uncategorized = filter_all_transactions(t, categories)

#while we have uncategorized transactions
while len(uncategorized) > 0:
    uncategorized[0].display()

    
    print(str(len(uncategorized)) + " uncategorized transactions remaining")

    print("CURRENT CATEGORIES:")
    print("================================")
    for k in categories.keys():#show user the currennt categories
        print(k)

    #have user input category
    print("Enter 'ext' to see extended description")
    key = input('Enter category: ')
    val = input('Enter transaction description: ')

    while key == 'ext' or val == 'ext':
        print(uncategorized[0].get_ext())
        key = input('Enter category: ')
        val = input('Enter transaction description: ')

    if key != '' and val != '':#if we got user input
        #update transaction and add to transaction list
        update_category(key, val, categories)
        uncategorized[0].set_desc(val)#update transactions description
    
    #then refilter the uncategorized transactions to remove all from the new category
    i = 0
    while i < len(uncategorized):
        filter_transaction(uncategorized[i], categories)
        #for any that have been updated
        if uncategorized[i].cat != 'uncategorized':
            t.append(uncategorized[i])#move them to the categorized
            uncategorized.remove(uncategorized[i])#remove from uncategorized
        else:
            i += 1

    #Shouldn't need this....
    """ if len(uncategorized) == 0:#when they're all categorized exit
        break """

#update the cats json with new categoriese
save_categories('cats.json', categories)

amounts = {k: 0 for k in categories.keys()}#setup a dictionary to hold the amounts in each category

#possible analysis of transactions here

#add up the transaction amounts for each transaction category
for trans in t:
    for cat in amounts:
        if trans.cat.lower() == cat:
                amounts[cat] += trans.amt

print(amounts)
for cat in categories.keys():
    show_by_category(cat, t)

