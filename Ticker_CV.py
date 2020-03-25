import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import yfinance as yf
import numpy as np
import pandas as pd
import requests
import csv
import datetime

from os import getcwd



#define the ticker symbol

tickerSymbol = str(input("Enter stock ticker: "))

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2020-1-22', end='2020-2-23')

sCloses = tickerDf['Close'].to_list()

#print(tCloses)

sDates = tickerDf.index.to_list()
#print(tDates)



url = "https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv"

directory = getcwd()
print("directory is ", directory)
filename = r'C:\Users\dubco\OneDrive\Documents\ncov_history.csv'

# r = requests.get(url)

# sr = str(r.content
# f = open(filename,'w')
# f.write(sr)
# f.close()
# print("length of sr is ", len(sr))

print(filename)
print("starting")
covid_data = pd.read_csv(filename)
df = pd.DataFrame(covid_data, columns= ['Date','Country/Region','Confirmed'])
#print("COVID")
#print(covid_data)
#print("DF")
#print(df)
# print("Df date: ")
# print(df["Date"])

# start_date = pd.to_datetime('2020-01-22')
# end_date = pd.to_datetime('2020-01-23')
start_date = '2020-01-22'
end_date = '2020-02-23'



tDates = []
tCases = []

tdate = start_date

while True:
    #print("tdate is ", tdate)
    #mask = (df['Date'] >= tdate) & (df['Date'] <= tdate)
    mask = (df['Date'] == tdate)
    #print("mask is ")
    #print(mask)
    df2 = df.loc[mask]
    #print("DF2 is")
    #print(df2)
    tconfirm = df2['Confirmed'].sum()
    #print("Date: ", tdate, "\tConfirmed cases: ", tconfirm)
    tDates.append(tdate)
    tCases.append(tconfirm)

    if tdate == end_date:
         break
    tdate1 = pd.to_datetime(tdate)
    tdate1 = tdate1 + datetime.timedelta(days=1)
    tdate = tdate1.strftime("%Y-%m-%d")
    #print("Next date ", tdate)



# Create some mock data
#t = np.arange(0.01, 10.0, 0.01)
#data1 = np.exp(t)
#data2 = np.sin(2 * np.pi * t)

# sX = [range(1,len(sDates))]
# tX = [range(1,len(Dates))]
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('date')
ax1.set_ylabel('price', color=color)
ax1.plot(sX, sCloses, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('cases', color=color)  # we already handled the x-label with ax1

ax2.plot(tX, tCases, color=color)
ax2.tick_params(axis='y', labelcolor=color)

#fig = plt.figure(figsize=(12, 6))
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()

# plt.plot(sDates, sCloses, ccases.values())
# plt.show()

