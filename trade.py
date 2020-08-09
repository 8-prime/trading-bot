import stock
from scrape import get_daily_top_n
from alpha_vantage.timeseries import TimeSeries

#setup for using alpha vantage for getting currenty prices for stocks
key = "RROECGAUHBTD2S5B"
ts = TimeSeries(key=key)

#retrieve top n changers for the day
top_5  = get_daily_top_n(5)

#handling the amount of held stocks and the money
money = 1000
held_stocks = []
top_5_stocks = []

def sell(stock):
    #sell remove stock from the list of held stocks and add the money the amount of stocks are worth to the money
    return 0

def buy(stock):
    #add amount of bought stocks to the list of held stocks and remove the cost from money
    return 0

#return true if a stock is worth buying
def check_stock_buyabulity():
    return True

#check if the maximum stop loss has been reached or if the stock fell under the daily average
def check_stock_sellability(stock):
    return True

def update_all_stocks(held_stocks, known_stocks):
    for stock in held_stocks:
        updated = False
        while(not updated):
            try:
                stock.set_price_hist(ts.get_intraday(stock.get_name()))
                updated = True
            except:
                pass



#this is where the program will be most of the time
while(True):
    update_all_stocks(held_stocks, known_stocks)
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


    


"""
for name in top_5:
    data, meta = ts.get_intraday(symbol=name)
    stonks += [data]
    print(data[0])
"""