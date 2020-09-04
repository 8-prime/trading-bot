from alpha_vantage.timeseries import TimeSeries

key = "RROECGAUHBTD2S5B"
ts = TimeSeries(key=key)



try:
    data = ts.get_intraday(symbol='TDC')
    print("Made it!")
except:
    pass


print(ts)