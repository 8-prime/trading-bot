from scrape import get_daily_top_n
from alpha_vantage.timeseries import TimeSeries

#setup for using alpha vantage for getting currenty prices for stocks
key = "RROECGAUHBTD2S5B"
ts = TimeSeries(key=key)

#retrieve top n changers for the day
top_5  = get_daily_top_n(5)


for name in top_5:
    data, meta = ts.get_intraday(symbol=name)
    stonks += [data]
    print(data[0])

#handling the amount of held stocks and the money
money = 1000
held_stocks = []

def sell(name_of_stock):
    #sell remove stock from the list of held stocks and add the money the amount of stocks are worth to the money
    return 0

def buy(name_of_stock):
    #add amount of bought stocks to the list of held stocks and remove the cost from money
    return 0


