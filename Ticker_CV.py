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
tickerDf = tickerData.history(period='1d', start='2020-1-22', end='2020-3-20')

sCloses = tickerDf['Close'].to_list()

#print(tCloses)

sDates = tickerDf.index.to_list()
sDates = pd.to_datetime(sDates)
sDates = sDates.strftime("%m-%d")
#print(tDates)

url = "https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv"

directory = getcwd()
print("directory is ", directory)
filename = r'C:\Users\dubco\OneDrive\Documents\ncov_history.csv'
#filename = "https://raw.githubusercontent.com/Dubcoder/NCV_Market/master/ncov_history.csv?token=ALYJT3EEXIDNYVVNI5Z73XC6POGDA"

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
# print("COVID")
# print(covid_data)
# print("DF")
# print(df)
# print("Df date: ")
# print(df["Date"])


start_date = '2020-01-22'
end_date = '2020-03-20'


cCases = {}
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
    tdate1 = pd.to_datetime(tdate)
    tdate2 = tdate1.strftime("%m-%d")
    cCases.update( {str(tdate2) : tconfirm} )   
    if tdate == end_date:
        break
    tdate1 = tdate1 + datetime.timedelta(days=1)
    tdate = tdate1.strftime("%Y-%m-%d")
    #print("Next date ", tdate)

i=0

# for td in cCases.keys():
#     print("case date is ", td, " stock date is ", sDates[i])
#     i+=1
#     if (i == len(sDates)):
#         break

for td in sDates:
    if td in cCases.keys():
        tCases.append(cCases[td])
    else:
        print("Can't find ", td, " in ccases.")



# Create some mock data
#t = np.arange(0.01, 10.0, 0.01)
#data1 = np.exp(t)
#data2 = np.sin(2 * np.pi * t)

# sX = [range(1,len(sDates))]
# tX = [range(1,len(Dates))]
fig, ax1 = plt.subplots(figsize=(12,6))

color = 'tab:blue'
ax1.set_xlabel('date')
ax1.set_ylabel('price', color=color)
ax1.plot(sDates, sCloses, color=color)
ax1.tick_params(axis='y', labelcolor=color)
for label in ax1.xaxis.get_ticklabels()[::2]:
    label.set_visible(False)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:red'
ax2.set_ylabel('cases', color=color)  # we already handled the x-label with ax1

ax2.plot(sDates, tCases, color=color)
ax2.tick_params(axis='y', labelcolor=color)
for label in ax2.xaxis.get_ticklabels()[::2]:
    label.set_visible(False)

ax1.tick_params(axis='x', which='major', labelsize=8)
ax2.tick_params(axis='x', which='major', labelsize=8)
#fig.tight_layout()  # otherwise the right y-label is slightly clipped
#fig.figure(figsize=(14, 8))
plt.show()
