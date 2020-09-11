import requests
from bs4 import BeautifulSoup
import time
import functions
import csv
from winreg import QueryValueEx, OpenKey, HKEY_CURRENT_USER
from os import listdir, remove, path
from os.path import isfile, join
from transaction import Transaction
from functions import *
import json

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
#row_to_remove = [0]

for file in csvs:
    fl = open(path_to_csvs + file)
    readers.extend(csv.reader(fl))
    readers.remove(readers[row_to_remove])
    #row_to_remove.append(len(readers))
    row_to_remove = len(readers)
    fl.close()

#row_to_remove.remove(row_to_remove[-1])

""" for r in row_to_remove:
    print(readers[r])
    readers.remove(readers[r])
 """


mPaycheck = []
mPayAmt = 0
bPaycheck = []
bPayAmt = 0
ext = ".fin"

#trying to get the list of transactions into a dictionary. Or we build an account object to track the balance over time and hold a list of transactions
""" order = {f:readers[t] for f in get_account_order(ext) for t in range(row_to_remove[1]-1)}
print(order) """

t = clean_rows(readers)#cleanup descriptions, extended desc is  not changed
amounts = {k : 0 for k in categories.keys()}#dictionary to hold category amounts

#read categories in a file
if path.exists('cats.json') and path.getsize('cats.json') > 0:
    fl= open('cats.json', 'r')
    categories = json.load(fl)
    fl.close()
    remove('cats.json')


#filters transactions based on category
uncategorized = filter_all_transactions(t)

i = 1
while len(uncategorized) > 0:

    print(i-1)
    uncategorized[i].display()
    key = input('Enter category: ')
    val = input('Enter transaction description: ')
    
    if key != '' and val != '':
        #update transaction and add to transaction list
        update_category(key, val)
    
    for trans in uncategorized:
        filter_transaction(trans)
        if trans.desc != 'uncategorized':
            t.append(trans)
            uncategorized.remove(trans)

    i = i + 1 % len(uncategorized)
    print(len(uncategorized))
    
#amounts = trans.update_cat()
#amounts[a[0]] += a[1]
#write categories to a file
""" fl = open('cats.json', 'w')
json.dump(categories, fl)
fl.close() """

show_category('uncategorized', t)


"""
print("Britt Pay: " + str(bPayAmt))
print("Matt Pay: " + str(mPayAmt))
print("Britt Paychecks:")
print(bPaycheck)
print ("=======================")
print("Matt Paychecks:")
print(mPaycheck)  """

#========================================================================