#import requests
#from bs4 import BeautifulSoup
import time
import functions
import csv
from os import listdir
from os import remove
from os.path import isfile, join

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

path_to_csvs = 'D:/UserLibraries/matta/Downloads/'

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
print(len(readers))

#csv = open(path_do_csvs + '/ExportedTransactions.csv')
