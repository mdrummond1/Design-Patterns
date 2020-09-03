#module for functions
from calendar import monthrange
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from winreg import QueryValueEx, OpenKey, HKEY_CURRENT_USER
import getpass
import transaction

def get_date_parameters():
    '''get_date_parameters()-> dict
        return a dictionary of strings representing dates.
        format : mm/dd/yyyy
        start_date is one month from end date.
        end_date is todays date
        dates are the date value in the string "arguments[0].setAttribute('value', '06/21/2020')"
        for use in the calling program
    '''

    today = time.localtime()
    start_day = str(today.tm_mday)
    start_month = str(today.tm_mon - 1)
    start_yr = str(today.tm_year)

    if start_month == 0:
        start_month = '12'
        start_yr = str(today.tm_year - 1)

    last_day = monthrange(int(start_yr), int(start_month))[1]

    #take care of months that have different number of days
    if int(start_day) > last_day:
            start_day = str(last_day)

    end_day = start_day
    end_month = str(today.tm_mon)
    end_yr = start_yr
    
    start_date = "arguments[0].setAttribute('value', '" + start_month + '/' + start_day + '/' + start_yr + "')"
    end_date = "arguments[0].setAttribute('value', '" + end_month + '/' + end_day + '/' + end_yr + "')"

    date = {
        'start_date': start_date,
        'end_date' : end_date
    }
    return date

def get_log_info():
    log = []
    log.append(input("Enter User Name: "))
    log.append(getpass.getpass("Enter password: "))
    return log

def login(user, password, driver):
    '''login(user, password, driver) -> void
        takes a username/password combo and driver
        finds login element and insert login info
    '''
    username = WebDriverWait(driver, 5).until(lambda d:d.find_element_by_id("UserName"))
    username.send_keys(user)
    passwd = driver.find_element_by_id("Password")
    passwd.send_keys(password + Keys.RETURN)    

def wait_and_click(id, driver, tm):
    '''wait_and_click(id, driver, time) -> void
        Takes an id, driver and time.
        User driver to search page for id with timeout of tm
    '''
    elem = WebDriverWait(driver, tm).until(EC.element_to_be_clickable((By.ID, id)))
    time.sleep(.5)
    elem.click()
    return elem

def input_dates(date, driver):
    '''input_dates(date, driver) -> void
    takes in a dictionary of start and end date
    and inputs them into the value of the correct elements
    end date is todays date
    '''
    start = driver.find_element_by_id("Parameters_StartDate")
    driver.execute_script(date['start_date'], start)
    end = driver.find_element_by_id("Parameters_EndDate")
    driver.execute_script(date['end_date'], end)

def get_downloads():
    '''() -> string
    returns the location of the Downloads folder as a string
    '''
    with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
        return QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0] + '\\'

def clean_rows(readers):
    '''(readers) -> [Transactions]
    Takes in a readers object (list of lists), and returns an array of Transactions
    Runs through 3 for loops
    '''
    #TODO: Optimize this function to not use 3 for loopst
    t = []
    for row in readers:
        for cat in categories.values():
            for sub in cat:
                if sub.lower() in row[csv_fields['desc']].lower():#clean the descriptions
                    row[csv_fields['desc']] = sub
                    break
        t.append(transaction.Transaction(row))

    return t
    
def get_account_order():
    '''() -> void
    takes no parameters.
    opens a file containing the order of the account transactions
    and returns that order in a list.
    Now we can track where the transactions happened.'''
    f = open("./order.txt", 'r')
    a = f.readlines()
    for i in range(len(a)):
        if a[i][-1] == '\n':
            a[i] = a[i][:-1]#strip out the \n at the end
    f.close()
    return a

#Dictionary to access correct column of transaction
csv_fields = {
    'trans_id' : 0,
    'post' : 1,
    'effective' : 2,
    'trans_type' : 3,
    'amt' : 4,
    'chk_num' : 5,
    'ref_num' : 6,
    'desc' : 7,
    'trans_cat' : 8,
    'type' : 9,
    'balance' : 10,
    'memo' : 11,
    'ext_desc' : 12
}

#Dictionary to check descriptions and categorize
#TODO: add categories for accounts other than checking 0400
categories = {
    'income' : ['VIA CHRISTI', 'STATE OF KANSAS', 'APY Earned'],
    'credit cards' : ['CAPITAL ONE', 'PAYMENT FOR AMZ', 'CHASE CREDIT CRD'],
    'car insurance' : ['PROG N WESTERN'],
    'fuel' : ['QuikTrip'],
    'renters insurance' : ['STATE FARM'],
    'utilities' : ['COX', 'Evergy', 'KANSAS GAS', 'ATT', 'WASTELINK'],
    'loans' : ['GREAT LAKES'],
    'gym' : ['YMCA'],
    'groceries' : ['Walmart', 'Aldi', 'Dillons'],
    'dining' : ['Spangles', 'Braum\'s', 'Fazoli\'s']

}

