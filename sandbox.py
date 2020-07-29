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


#######Getting current day
params = functions.get_date_parameters()
print(params)
