#module for functions
from calendar import monthlen
import time

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

    last_day = monthlen(int(start_yr), int(start_month))

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


def check_day(yr, mo, day):
    last_day = monthlen(yr, mo)
    if day > last_day:
        return last_day
    else:
        return day