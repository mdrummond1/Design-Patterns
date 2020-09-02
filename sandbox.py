import requests
from bs4 import BeautifulSoup
import time
import functions
import csv
from winreg import QueryValueEx, OpenKey, HKEY_CURRENT_USER
from os import listdir, remove
from os.path import isfile, join
from transaction import Transaction
from functions import *


#===============Testing requests and beautiful soup==================
"""
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Controw-Allow-Methods':'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

#url = "https://cuaonline.cuofamerica.com/MyAccountsV2"
url = "https://cuaonline.cuofamerica.com/Authentication?ReturnUrl=MyAccountsV2#account-446e56f2-defd-43e1-8971-3a229f9258c6"

req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
print(soup.prettify)

fl = open("test.html", 'w')
fl.write(str(soup))
"""
#=====================================================================

#==============Testing csv reading====================================
path_to_csvs = functions.get_downloads()


csvs = [f for f in listdir(path_to_csvs) if isfile(join(path_to_csvs, f)) and 'ExportedTransactions' in f]
readers = []
row_to_remove = 0


for file in csvs:
    fl = open(path_to_csvs + file)
    readers.extend(csv.reader(fl))
    readers.remove(readers[row_to_remove])
    row_to_remove = len(readers)
    fl.close()


#print(readers)
mPaycheck = []
mPayAmt = 0
bPaycheck = []

bPayAmt = 0

order = functions.get_account_order()
print(str(order))

t = clean_rows(readers)
#test how to process the csv data

#This is how we can clean the descriptions. Hopefully we can eventually change it so we don't need 3 loops
""" for row in readers:
    for cat in functions.categories.values():
        for sub in cat:
            if sub.lower() in row[functions.csv_fields['desc']].lower():
                row[functions.csv_fields['desc']] = sub
                t.append(Transaction(row))
                break
 """    

for trans in t:
    trans.display()

""" 

print("Britt Pay: " + str(bPayAmt))
print("Matt Pay: " + str(mPayAmt))
print("Britt Paychecks:")
print(bPaycheck)
print ("=======================")
print("Matt Paychecks:")
print(mPaycheck)  """

#========================================================================