from alpha_vantage.timeseries import TimeSeries
import csv
import pandas
key = "RROECGAUHBTD2S5B"
ts = TimeSeries(key=key, output_format='pandas', indexing_type='integer')

data = []

try:
    data = ts.get_intraday(symbol='TDC')
    print("Made it!")
except:
    pass


print(data[0]['1. open'])