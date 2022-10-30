import requests
import datetime
import pandas as pd

#set root URL
ROOT_URL = "https://api.binance.com"

#construct request URL
req = "{root_url}/{endpoint}?symbol={symbol}&interval={interval}&limit={limit}&startTime={since}" \
         .format(root_url="https://api.binance.com",
                 endpoint="api/v3/klines",
                 symbol="BTCUSDT",
                 interval="1d",
                 limit="75",
                 since=1661983200)
print(req)

#send request to the Binance server and get response
resp = requests.get(req)
print(resp)

#convert to DataFrame
data = pd.DataFrame.from_records(
        resp.json(),
        columns=["time","open", "high", "low", "close",".",".",".",".",".",".","."]
    )
data = data[["time","open", "high", "low", "close"]]
data['time']=data['time']/1000
data.index = data.pop("time").map(datetime.datetime.fromtimestamp)
print(data)


#Final step: Homework 6 define function, which retrieves 75 observations of klines data for a generic currency pair since a generic date.
def get_klines(currency_pair,startTime):
    """
    """
    req = "{root_url}/{endpoint}?symbol={symbol}&interval={interval}&limit={limit}&startTime={since}" \
         .format(root_url="https://api.binance.com",
                 endpoint="api/v3/klines",
                 symbol=currency_pair,
                 interval="1d",
                 limit="75",
                 since=startTime)
    resp = requests.get(req)
    data = pd.DataFrame.from_records(
        resp.json(),
        columns=["time","open", "high", "low", "close",".",".",".",".",".",".","."])
    data = data[["time","open", "high", "low", "close"]]
    data['time']=data['time']/1000
    data.index = data.pop("time").map(datetime.datetime.fromtimestamp)
    return data

klines_data=get_klines("BTCUSDT",1661983200)
print(klines_data)