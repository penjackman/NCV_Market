import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import yfinance as yf
import numpy as np
import pandas as pd
import requests
import csv
import datetime
import string


from os import getcwd
def Ticker(start_date, end_date):
    #define the ticker symbol

    tickerSymbol = str(input("Enter stock ticker: "))

    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)

    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)

    sCloses = tickerDf['Close'].to_list()

    #print(sCloses)

    sDates = tickerDf.index.to_list()
    sDates = pd.to_datetime(sDates)
    sDates = sDates.strftime("%Y-%m-%d")

    return sDates, sCloses



def CV(df, tdate, cCases, end_date, sDates, tCases):
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
        # tdate1 = pd.to_datetime(tdate)
        # tdate2 = tdate1.strftime("%m-%d")
        cCases.update( {str(tdate) : tconfirm} )
        if tdate == end_date:
            break
        tdate1 = pd.to_datetime(tdate)
        tdate1 = tdate1 + datetime.timedelta(days=1)
        tdate = tdate1.strftime("%Y-%m-%d")
        #print("Next date ", tdate)



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



def Plot(sDates1, sCloses, tCases):
    fig, ax1 = plt.subplots(figsize=(12,6))

    color = 'tab:blue'
    ax1.set_xlabel('date')
    ax1.set_ylabel('price', color=color)
    ax1.plot(sDates1, sCloses, color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    for label in ax1.xaxis.get_ticklabels()[::2]:
        label.set_visible(False)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:red'
    ax2.set_ylabel('cases', color=color)  # we already handled the x-label with ax1

    ax2.plot(sDates1, tCases, color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    for label in ax2.xaxis.get_ticklabels()[::2]:
        label.set_visible(False)

    ax1.tick_params(axis='x', which='major', labelsize=8)
    ax2.tick_params(axis='x', which='major', labelsize=8)
    #fig.tight_layout()  # otherwise the right y-label is slightly clipped
    #fig.figure(figsize=(14, 8))
    plt.show()

def main():
    url = "https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv"

    start_date = '2020-01-22'
    end_date = str(datetime.date.today())
    filename = url
    print(filename)
    print("starting")
    df = pd.read_csv(filename, lineterminator='\n')

    cCases = {}
    tCases = []
    
    tdate = start_date
    
    sDates, sCloses = Ticker(start_date, end_date)
    
    sDates1 = pd.to_datetime(sDates)
    sDates1 = sDates1.strftime("%m-%d")
    
    CV(df, tdate, cCases, end_date, sDates, tCases)
    Plot(sDates1, sCloses, tCases)

if __name__ == "__main__":
    main()
