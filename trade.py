from scrape import get_daily_top_n
from alpha_vantage.timeseries import TimeSeries

key = "RROECGAUHBTD2S5B"

top_5  = get_daily_top_n(5)

ts = TimeSeries(key=key)
for name in top_5:
    data, meta = ts.get_intraday(symbol=name)
    print(data)
