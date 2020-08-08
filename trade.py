from scrape import get_daily_top_n
from alpha_vantage.timeseries import TimeSeries
"""
key = "RROECGAUHBTD2S5B"

ts = TimeSeries(key=key)
aapl, meta = ts.get_intraday(symbol='AAPL')
print(aapl)
"""
print(get_daily_top_n(5))
