
#Goal: Scrape Worldometers

import yfinance as yf

#define the ticker symbol
tickerSymbol = 'AAPL'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2020-3-1', end='2020-3-20')

#see your data
print (tickerDf)
