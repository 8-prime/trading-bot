from stock import Stock
from scrape import get_daily_top_n
from alpha_vantage.timeseries import TimeSeries

#########All of this is just primary setup that will run one when the programm is started ###########

#setup for using alpha vantage for getting currenty prices for stocks
key = "RROECGAUHBTD2S5B"
ts = TimeSeries(key=key, output_format='pandas', indexing_type='integer')

#retrieve top n changers for the day
top_5  = get_daily_top_n(5)

#handling the amount of held stocks and the money
money = 1000
held_stocks = []
top_5_stocks = []





########## These are functions that are needed for the programm to work #######



def sell(stock):
    #sell remove stock from the list of held stocks and add the money the amount of stocks are worth to the money
    return 0

#return true if a stock is worth buying
def check_stock_buyabulity():
    return True

def buy(stock):
    #add amount of bought stocks to the list of held stocks and remove the cost from money
    return 0

#check if the maximum stop loss has been reached or if the stock fell under the daily average
def check_stock_sellability(stock):
    return True

#this updates the sliding average for all the stocks
def update_all_stocks(held_stocks, top_5_stocks):
    for stock in held_stocks:
        updated = False
        while(not updated):
            try:
                print("Updating Price history for stock ", stock.get_name())
                stock.set_price_hist(ts.get_intraday(stock.get_name()))
                updated = True
            except:
                pass
    for stock in top_5_stocks:
        updated = False
        while(not updated):
            try:
                print("Updating Price history for stock ", stock.get_name())
                stock.set_price_hist(ts.get_intraday(stock.get_name()))
                updated = True
            except:
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

def is_known_stock(name_of_stock):
    for i in held_stocks:
        if i.get_name() == name_of_stock:
            return True
    for i in top_5_stocks:
        if i.get_name() == name_of_stock:
            return True
    return False

#checks if there are new stocks in the top 5
def check_for_new_stocks():
    if (not list_compare(get_daily_top_n(5), top_5)):
        #delete current list of top 5
        top_5_stocks = []
        #overwrites top 5 names of stocks as to not be influenced by the accessability of the given stock for alpha vantage
        top_5 = get_daily_top_n(5)
        for name in top_5:
            if is_known_stock(name):
                break
            #check if the stock already exists in the current top 5 or in the known stocks
            newStock = Stock(name=name)
            #create stock with name and the price hist for the given name. this has to be done in try cath as it relys on the api
            accessed = False
            viable_stock = True
            while(not accessed):
                try:
                    print("trying to get data for ", name)
                    current_price_hist = ts.get_intraday(name)
                    newStock.set_price_hist(current_price_hist)
                    accessed = True
                except ValueError:
                    viable_stock = False
                    accessed = True
                except:
                    pass
            if viable_stock:
                top_5_stocks += [newStock]


######### This is the main programm ##########



while(True):
    #check of top 5 changed. if so update list of top5 stocks
    
            

    update_all_stocks(held_stocks, top_5_stocks)
    #check if i have to sell stocks because their value is decreasing
    for stock in held_stocks:
        if check_stock_sellability(stock):
            sell(stock)
    #first check of there is money to spend
        #take the ith entry from the list of stocks and then check if the stock is cheap enough to buy for us right now
    #price / 5-i
    for name in top_5:
        #if miney / 5-i is greater than the price of the stock, fecking go mate
        #if we already own stock for this changer, we will check the next one and so on, potentially not buying at all
        i = 312 # dummy shit to avoid errors
