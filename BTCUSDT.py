import requests
import time
import pandas as pd
from sys import exit
from datetime import datetime
pd.set_option('expand_frame_repr', False)
from urllib.request import urlopen

BASE_URL = 'https://api.binance.com'
limit = 1000
end_time = int(time.time() // 60*60*1000)
#print(end_time)
start_time = int(end_time - limit*60*1000)
df1 = pd.DataFrame(columns =['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_volumn', 'trades', 'taker_base_volumn', 'taker_quote_volumn', 'ignore'])
#df1.set_index('open_time', inplace=True)
currency_pair = str('MATICUSDT')
Time = str('hour')
#exit()

while True:
    url = BASE_URL + '/api/v1/klines' + '?symbol='+ currency_pair +'&interval=1m&limit=' + str(limit) + '&startTime=' + str(start_time) +'&endTime=' + str(end_time)
    print(url)
    #exit()
    resp = requests.get(url)
    data = resp.json()
    #df = pd.DataFrame(data)
    df = pd.DataFrame(data, columns ={'open_time':0, 'open':1, 'high':2, 'low':3, 'close':4, 'volume':5, 'close_time':6, 'quote_volumn':7, 'trades':8, 'taker_base_volumn':9, 'taker_quote_volumn':10, 'ignore':11})
    #exit()
    #df['open_time']= pd.to_datetime(df['open_time'])
    #df['close_time']= pd.to_datetime(df['close_time'])
    #df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
    #df['close_time'] = pd.to_datetime(df['close_time'], unit='ms')
    #df.set_index('open_time', inplace=True)
    #df.index = pd.to_datetime(df.index, unit='ms')
    #df1.index = pd.to_datetime(df1.index, unit='ms')
    
    df1 = df1.append(df)
    #df1.index.astype('int')
    #df1.index = pd.to_datetime(df1.index, unit='ms')
    #df1.to_csv(str(end_time)+'.csv')
    #print(df)
    #if start_time < 1546272000000: #day
    #if start_time < 1577808000000: #hour
    if start_time < 1621270861000: #min
        #df1.to_csv('BTCUSDT0104.csv')
        #if start_time < 1590940800000:  #2
    #if start_time < 1609430400000:  #3
    #if start_time < 1609430400000:  #4
        #df1.to_excel("BTCUSDT.xlsx", sheet_name="BTCUSDT")
        #df1.to_csv('BTCUSDT202006-202104.csv')
        df1.to_csv(currency_pair + '_Data.csv')
        break
    #if start_time < 1546272000000:
    #    df1.to_excel("BTCUSDT.xlsx", sheet_name="BTCUSDT")
    #    #df1.to_csv('BTCUSDT1.csv')
    #    break
    end_time = start_time
    start_time = int(end_time - limit*60*1000)
 