import json
import time
from datetime import datetime
from scrape import get_daily_top_n
from alpha_vantage.timeseries import TimeSeries

'''
    Global variables needed for operation
'''
key = ''
fd =  './keyfile'
with open(fd, 'r') as file:
    key = file.readlines()
print(key)
ts = TimeSeries(key=key[0], output_format='pandas', indexing_type='integer')
CURRENT_PRICE_INDEX = '1. open'
SLEEP_DURATION = 900

stocks_of_interest = {}
data = {}
data['Money'] = 1000

'''
Because the script is only supposed to do things when the stock market is open
the opening and closing times have to be saved
'''
opening_time = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)
closing_time = datetime.now().replace(hour=20, minute=0, second=0, microsecond=0)
'''
Structure for the data dictionary:
    a Stock has its name as the key and has a dict as the value  with the following fields
    'name' : {
        'price_time_of_purchace'
        'sliding_average'
        'amount_held'
        'current_price'
    }

The stocks of interes dictionary hold the name of stocks that are currently interesing to the user
as well as the price so that it can be immediately used when the stock is to be bought
    'name' : {
        'current_price'
    }

'''

def list_compare(a,b):
    sa = sorted(a)
    sb = sorted(b)
    if (len(sa) != len(sb)):
        return False
    for i in range (len(sa)):
        if sa[i] != sb[i]:
            return False
    return True

def persist():
    print('Writing data to file')
    with open('data.json', 'w') as file:
        json.dump(data,file,indent=4)

def test_for_buying():
    print('Looking at potential stocks to buy')
    if data['Money'] > 0:
        names_interested = list(stocks_of_interest.keys())
        for name in names_interested:
            if data['Money'] > stocks_of_interest[name]['current_price']:
                print('Buying ' + name + ' for: ' + str(stocks_of_interest[name]['current_price']) + '$')
                data['Money'] -= stocks_of_interest[name]['current_price']
                if not name in list(data.keys()):
                    data[name] = {}
                    data[name]['amount_held'] = 1
                else:
                    data[name]['amount_held'] += 1
                data[name]['current_price'] = stocks_of_interest[name]['current_price']
                data[name]['sliding_average'] = stocks_of_interest[name]['current_price']


#when checking for stocks to sell iterato trough the list of keys,
#exlude 'Money' and then check of the condition to sell is met
def test_for_selling():
    stock_list = list(data.keys())
    stock_list.remove('Money')
    print('Testing for sellable stocks')
    for stock in stock_list:
        if data[stock]['current_price'] < data[stock]['price_top']:
            print('Selling ' + stock)
            data['Money'] += data[stock]['current_price'] * data[stock]['amount_held']
            del data[stock]

#update data for the stocks of interest
def update_interested():
    print('Updating stocks of interest')
    names_interested = list(stocks_of_interest.keys())
    for name in names_interested:
        while True:
            try:
                updated_price = ts.get_intraday(name)
                stocks_of_interest[name]['current_price'] = updated_price[0][CURRENT_PRICE_INDEX][0]
                print('Updated potential stock ' + name)
                return
            except Exception:
                pass

#update data for the owned stocks
def update_held_stocks():
    names_held_stocks = list(data.keys())
    names_held_stocks.remove('Money')
    print('Updating held stocks')
    for name in names_held_stocks:
        while True:
            try:
                updated_price = ts.get_intraday(name)
                data[name]['sliding_average'] = (data[name]['sliding_average'] + updated_price[0][CURRENT_PRICE_INDEX][0]) / 2
                data[name]['current_price'] = updated_price[0][CURRENT_PRICE_INDEX][0]
                print('Updated held stock ' + name)
                return
            except Exception:
                pass



def populate_of_interest():
    names_of_interest = get_daily_top_n(5)
    print('Top five retreived')
    global stocks_of_interest
    # if the list has changed it will be replaced by the new top n
    if not stocks_of_interest or not list_compare(names_of_interest, list(stocks_of_interest.keys())):
        print('New stocks found')
        stocks_of_interest = {}
        for name in names_of_interest:
            while True:
                try:
                    print('Trying to retreive data for ' + name)
                    current_price_history = ts.get_intraday(name)
                    stocks_of_interest[name] = {
                        'current_price' : current_price_history[0][CURRENT_PRICE_INDEX][0]
                    }
                    break
                except ValueError: # catches the case that the name from the daily top n is not available trough alpha vantage
                    break
                except Exception: # Catches the exception thrown when the max api calls were used
                    pass

while True:
    #if True:#opening_time > datetime.now() and datetime.now() < closing_time:
        #stockmarket is open baby
    populate_of_interest()
    update_held_stocks()
    update_interested()
    test_for_selling()
    test_for_buying()
    persist()
    time.sleep(SLEEP_DURATION)