import requests
from bs4 import BeautifulSoup
<<<<<<< HEAD
import datetime
import functions
import calendar
import getpass
from selenium import webdriver
import os
import csv
import transaction

=======
import time
import functions
>>>>>>> parent of ebfbbac... able to read csvs. need to categorize transactions.
#######Testing requests and beautiful soup
""" 
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Controw-Allow-Methods':'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

url = "https://cuaonline.cuofamerica.com/MyAccountsV2"

req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
print(soup.prettify) """

<<<<<<< HEAD
########Testing reading in files
""" path_to_csvs = 'D:/UserLibraries/matta/Downloads/'

csvs = [f for f in listdir(path_to_csvs) if isfile(join(path_to_csvs, f)) and 'ExportedTransactions' in f]
readers = []
row_to_remove = 0

for file in csvs:
    fl = open(path_to_csvs + file)
    readers.extend(csv.reader(fl))
    readers.remove(readers[row_to_remove])
    row_to_remove = len(readers)
    fl.close()

for file in csvs:
    remove(path_to_csvs + file)
print(readers)
print(len(readers)) """

#url = "https://cuaonline.cuofamerica.com/MyAccountsV2"

#PATH = "./browserDrivers/chromedriver.exe"
#for linux -> #PATH = "/mnt/c/Program Files (x86)/chromedriver.exe"

#get bank login info
#user = input("Enter UserName: ")
#password = getpass.getpass("Enter password: ")


#driver = webdriver.Chrome(PATH)
#driver.get(url)


fl = open('C:/Users/matta/Downloads/ExportedTransactions.csv')

csv1 = csv.reader(fl)
t = []
for row in csv1:
    r = row
    t.__add__(transaction.Transaction(r[0], r[1], r[2],r[3],r[4],r[6],r[7],r[8],r[11]))
    


for i in trans:
    i.show()

=======

#######Getting current day
params = functions.get_date_parameters()
print(params)
>>>>>>> parent of ebfbbac... able to read csvs. need to categorize transactions.
