from datetime import datetime
from scrape import get_daily_top_n
from alpha_vantage.timeseries import TimeSeries
from stock import Stock


'''
    Global variables needed for operation
'''
key = ''
fd =  './keyfile'
with open(fd, 'r') as file:
    key = file.readlines()
ts = TimeSeries(key=key[0], output_format='pandas', indexing_type='integer')
top_n_changer_names = []
top_n_changers_stock = []
held_stocks = []
stonks = 1000
MONEY_INDEX = '1. open'






#this will buy the stock and if its not yet know, create a new stock.
#  if it is already known it will just add however stocks are to be bought
def buy_stock(name, amount, data):
    #check for existing stock
        
    for stock in held_stocks:
        if stock.get_name() == name:
            stock.set_amount_held(stock.get_amount_held() + amount)
            stonks -= (data[0][MONEY_INDEX][0] * amount)
    #create new stock
    while (True):
        current_price = data[0][MONEY_INDEX][0]
        held_stocks += Stock(current_price, 0, amount, current_price, name, data)
        stonks -= current_price * amount
        return

def update_stock(name):
    while(True):
        try:
            print ('Trying to update stock ' + name)
            data = ts.get_intraday(name)
            return data
        except Exception:
            pass
        


def create_empty_stock(name):
    while(True):
        try:
            data = ts.get_intraday(name)
            current_price = data[0][MONEY_INDEX][0]
            print(type(current_price))
            return Stock(0,0,0,current_price,name,data)
        except Exception:
            pass


def list_compare(a,b):
    sa = sorted(a)
    sb = sorted(b)
    if (len(sa) != len(sb)):
        return False
    for i in range (len(sa)):
        if sa[i] != sb[i]:
            return False
    return True

'''
Because the script is only supposed to do things when the stock market is open
the opening and closing times have to be saved
'''
opening_time = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)
closing_time = datetime.now().replace(hour=20, minute=0, second=0, microsecond=0)


run = True

while(run):
    #check if stock market is currently open
    if(datetime.now() > opening_time and datetime.now() < closing_time):
        #get top 5 changers
        top_n_changer_names = get_daily_top_n(5)
        for name in top_n_changer_names:
            top_n_changers_stock += [create_empty_stock(name)]
        #check if there is money to buy any

        #update all held stocks

        #check if stocks should be sold

        #persist money and held stocks into json

    #while testing for now in dont want infinite loop