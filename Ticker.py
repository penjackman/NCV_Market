
#Goal: Scrape Worldometers
#authors: Mihir, Bharadwaj, <add more>

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import yfinance as yf

#define the ticker symbol
tickerSymbol = 'AAPL'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2020-3-1', end='2020-3-20')

tCloses = tickerDf['Close'].to_list()

#print(tCloses)

tDates = tickerDf.index.to_list()
print(tDates)

#print(tickerDf[['Open', 'Close']]) 
# tickerNp = tickerDf.to_numpy()
# print(tickerNp)

fig = plt.figure(figsize=(12, 6))
plt.plot(tDates, tCloses)
plt.show()
