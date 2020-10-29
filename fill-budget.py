from functions import *
import pandas as pd
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


""" url = "https://cuaonline.cuofamerica.com/MyAccountsV2"
PATH = "./browserDrivers/chromedriver.exe"
ext = '.fin'

log_info = get_log_info()#get bank login info

driver = webdriver.Chrome(PATH)
driver.get(url)

login(log_info[0], log_info[1] , driver)#login
print("Logging in...")
i = 0#cause apparently I need a counter for the dropbox list

#get list of accounts
print("Collecting accounts...")
accounts = WebDriverWait(driver, 5).until(lambda d: d.find_elements_by_class_name("account"))
#TODO: add in checking for bad credentials, shown from timeout error when getting accounts

date_params = get_date_parameters()#generate dates
print("Setting dates...")

print("Downloading transactions...")
try:
    accounts[0].click()

    wait_and_click('export_trigger', driver, 5)    

    drop = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "iris-dropdown__selected-value")))
    drop.click()#open dropbox

    dropbox_items = WebDriverWait(driver, 5).until(lambda d: d.find_elements(By.CLASS_NAME,"iris-list-item__content"))
    dropbox_items[i].click()#select csv

    input_dates(date_params, driver)#put date values into date selectors

    download = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "export_transactions_confirm_button")))

    download.click()
    #confirm_btn = wait_and_click("export_transactions_confirm_button", driver, 5)
        
    time.sleep(2)#give the file time to download

except Exception as e:
    print("something failed")

#website was updated

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
 """

#read-in files
path_to_csvs = get_downloads()

#Dictionary to check descriptions and categorize
configs = {
    'income' : ['my awsome job'],
    'rent' : ['lik my crib'],
    'phone' : ['gunna call u l8r'],
    'credit cards' : ['drowning in debt'],
    'transportation' : ['am gon places'],
    'utilities' : ['hang at hom'],
    'loans' : ['still drownin'],
    'gym' : ['lazy'],
    'groceries' : ['hungry'],
    'dining out' : ['cant cook'],
    'healthcare' : ['im dying']
}

#build list of transaction files
#collects them in ascending order with ExportedTransactions at the end
csvs = [f for f in listdir(path_to_csvs) if isfile(join(path_to_csvs, f)) and 'ExportedTransactions' in f]

row_to_remove = 0#get rid of each file heading
readers = []

#add in a list or something to keep track of the different accounts
#accounts stored in json
amounts = []


for file in csvs:#open files and put into csv reader
    with open(path_to_csvs + file) as fl:
        readers.extend(reader(fl))
        readers.remove(readers[row_to_remove])
        if (len(readers) - row_to_remove) > 1:#if we added new transactions, then get the balance
            amounts.append(readers[row_to_remove][csv_fields['balance']])#collect most recent balance from each account
        else:#otherwise the file was blank, set it to 0
            amounts.append(0)
        row_to_remove = len(readers)
    
    #remove(path_to_csvs + file)#delete file, so we don't have repeat transactions


#check for a categories file
if exists('configs.json') and getsize('configs.json') > 0:#if we have one, read the categories from it
    with open('configs.json', 'r') as fl:    
        configs = load(fl)
        fl.close()
        remove('configs.json')
else:#initialize empty dictionary
    #TODO: fill up accounts here, so we can get the correct balances later, 
    # and avoid index out of bounds
    configs = {
        "accounts" : [
            "CHECKING", 
            "BALANCE BOOST",
            "SAVINGS",
            "Quicksilver credit card",
            "360 Savings",
            "Chase credit card",
            "Amazon credit card"],
        
        "categories" : {},
        "subcategories" : {}
    }

if not configs['categories'] or not configs['subcategories']:
    haveFile = False
else:
    haveFile = True

#read the first file last, so put the last balance at the front to get in same order as bank
amounts.insert(0, amounts.pop())

balances = {key:0 for key in configs['accounts']}
i = 0
for acct in balances.keys():
    if i > len(balances.keys()):#we'll have indexing issues
        break
    balances[acct] = float(amounts[i])
    i += 1


for key in balances:#check if we have a positive credit card balance, and make it negative
    #this may cause problems if the actual balance is positive, like when a statement has been accidentally overpaid
    if "credit card" in key and balances[key] > 0:
        balances[key] = -balances[key]


print(balances)

k = input("here we are")

#clean the csv rows
t = clean_rows(readers, configs['subcategories'])

#filters transactions based on category
t, uncategorized = filter_all_transactions(t, configs['subcategories'], haveFile)


#while we have uncategorized transactions
while len(uncategorized) > 0:
    uncategorized[0].display()

    print(str(len(uncategorized)) + " uncategorized transactions remaining")

    #have user input category
    print("CURRENT CATEGORIES:")
    print("================================")
    for k in configs['categories'].keys():#show user the current categories
        print(k)
    
    print("Enter 'ext' to see extended description")
    new_cat = input('Enter category: ')

    print("CURRENT SUBCATEGORIES:")
    print("================================")
    
    for k in configs['subcategories'].keys():#show user the current categories
        print(k)
    
    
    new_sub_cat = input('Enter subcategory: ')
    
    new_desc = input('Enter transaction description: ')

    while new_cat == 'ext' or new_sub_cat == 'ext' or new_desc == 'ext':
        print(uncategorized[0].get_ext())
        new_cat = input('Enter category: ')
        new_sub_cat = input('Enter subcategory: ')
        new_desc = input('Enter transaction description: ')

    if new_cat != '' and new_sub_cat != '' and new_desc != '':#if we got user input
        #update transaction and add to transaction list
        update_category(new_cat, new_sub_cat, new_desc,configs['subcategories'], configs['categories'])
        uncategorized[0].set_desc(new_desc)#update transactions description
    
    #then refilter the uncategorized transactions to remove all from the new category
    i = 0
    while i < len(uncategorized):
        filter_transaction(uncategorized[i], configs['subcategories'])
        #for any that have been updated
        if uncategorized[i].cat != 'uncategorized':
            t.append(uncategorized[i])#move them to the categorized
            uncategorized.remove(uncategorized[i])#remove from uncategorized
        else:
            i += 1

#update the cats json with new categoriese
save_configs('configs.json', configs)

amounts = {k: 0 for k in configs['subcategories'].keys()}#setup a dictionary to hold the amounts in each category

#possible analysis of transactions here

#add up the transaction amounts for each transaction category
for trans in t:
    for cat in amounts:
        if trans.cat.lower() == cat.lower():
                amounts[cat] += trans.amt

print(amounts)

p = pd.DataFrame.from_dict(data=amounts, orient='index')
print(p)
p.to_excel('test.xlsx')

#output categories and totals into excel
"""to set up the next budget use percentages:
    38% - housing
    12% - food
    5% - debts or savings
    10% - insurance
    5% Entertainment
    5% Clothing
    5% Savings
    5% Miscellaneous
    
    stretch goals: make these percentages modifiable by user
        store in json?

    then compare that to the amounts from the previous month.
    if last month was over in that category, the excess comes out of this month.
    if last month was under in a category, we have more to spend this month.
    Goal is to allocate 100% of income into a category, so we have 0 left over.

Need to figure out how to store our data.
This needs to be a separate file so it can be different for each user
data needing stored:
    1. categories
    2. subcategories
    3. account order
    4. percentages?
"""

""" for cat in categories.keys():
    show_by_category(cat, t) """

