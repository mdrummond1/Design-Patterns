import requests
from bs4 import BeautifulSoup
import time
import functions
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

mPaycheck = []
mPayAmt = 0
bPaycheck = []
bPayAmt = 0

for row in readers:
    if "DIR DEP" and "VIA CHRISTI" in row[functions.csv_fields["desc"]]:
        bPaycheck.extend([[row[functions.csv_fields["desc"]], row[functions.csv_fields["amt"]], row[functions.csv_fields["balance"]]]])
        bPayAmt += float(row[functions.csv_fields["amt"]])      
    elif "DIR DEP" and "STATE OF KANSAS" in row[functions.csv_fields["desc"]]:
        mPaycheck.extend([row[functions.csv_fields["desc"]], row[functions.csv_fields["amt"]], row[functions.csv_fields["balance"]]])
        mPayAmt += float(row[functions.csv_fields["amt"]])

#print("Britt Pay: " + str(bPayAmt))
#print("Matt Pay: " + str(mPayAmt))
print("Britt Paychecks:")
print(bPaycheck)
print ("=======================")
print("Matt Paychecks:")
print(mPaycheck) 
#csv = open(path_do_csvs + '/ExportedTransactions.csv')
