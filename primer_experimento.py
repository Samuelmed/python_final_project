import krakenex
import pandas as pd
import matplotlib.pyplot as plt

k = krakenex.API()
k.load_key('kraken.key')

pair = 'XETHZUSD'


            

ohlc = pd.DataFrame (k.query_public('OHLC', data = {'pair': pair, 'interval' : 1,'since': None})['result'][pair])

ohlc.columns = [
                'time', 'open', 'high', 'low', 'close',
                'vwap', 'volume', 'count',]

print(ohlc)                

print('javi que pesao')


#df = pd.DataFrame(resp['result'][pair])
#plt.bar(df[0], df[1])
#plt.show()
#clear
# print(df)