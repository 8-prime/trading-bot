from alpha_vantage.timeseries import TimeSeries
import csv
import pandas
import json


key = "RROECGAUHBTD2S5B"
ts = TimeSeries(key=key, output_format='pandas', indexing_type='integer')

data = None

try:
    data = ts.get_intraday(symbol='TDC')
    print(data[0]['1. open'][0])
except Exception:
    pass



tdict = {}

tdict['IBM'] = {
    'sliding_average' : 0.0,
    'amout_held' : 0,
    'current_price' : 0.0
}

tdict['Money'] = {
    'stonks' : 100000000
}

with open('test.json', 'w') as open:
    json.dump(tdict,open, indent=4)

