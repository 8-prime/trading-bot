import yfinance as yf
from alpha_vantage.timeseries import TimeSeries

key = "RROECGAUHBTD2S5B"

ts = TimeSeries(key=key)
aapl, meta = ts.get_intraday(symbol='AAPL')
print(aapl)


