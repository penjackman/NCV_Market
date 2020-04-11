from flask import render_template
from flask import request
from flask import Flask

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
#import numpy as np
import yfinance as yf
import pandas as pd
import datetime
from io import BytesIO
import base64
import math

app = Flask(__name__)
def Ticker(start_date, end_date, tickerSymbol):
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)
    sCloses = tickerDf['Close'].to_list()
    sDates = tickerDf.index.to_list()
    sDates = pd.to_datetime(sDates)
    sDates = sDates.strftime("%Y-%m-%d")
    return sDates, sCloses

def CV_Stats(tdate, sDates, sCloses, df, end_date):
    cCases = {}
    tCases = []
    scDates = []
    scCloses = []
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
    i=0
    for sd in sDates:
        if sd in cCases.keys():
            tCases.append(cCases[sd])
            scDates.append(sd)
            scCloses.append(sCloses[i])
        else:
            print("Can't find ", sd, " in ccases.")
        i += 1

    return scDates, tCases, scCloses


def Plot(sDates1, sCloses, tickerSymbol, tCases):
    fig, ax1 = plt.subplots(figsize=(10, 5))
    color = 'tab:blue'
    ax1.set_title('Stock: ' + tickerSymbol, fontsize= 16, color='b')
    ax1.set_xlabel('date', fontsize=14, color='b')
    ax1.set_ylabel('price', fontsize=14, color='b')
    ax1.plot(sDates1, sCloses, color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    i=0
    for label in ax1.xaxis.get_ticklabels()[::1]:
        if (i%6 != 0):
            label.set_visible(False)
        i= i+1
    ax1.tick_params(axis='x', which='major', labelsize=10)
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    color = 'tab:red'
    ax2.set_ylabel('confirmed cases', fontsize=14, color='r')
    ax2.plot(sDates1, tCases, color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    j = 0
    for label in ax2.xaxis.get_ticklabels()[::1]:
        if (i%6 != 0):
            label.set_visible(False)
        j = j+1

    ax2.tick_params(axis='x', which='major', labelsize=10)
    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return plot_url

def Correlation(sDates, sCloses, tCases):
    diffSeries = []
    ticks = sDates
    xlist1 = sCloses
    xlist2 = tCases
    maxl1 = max(xlist1)
    maxl2 = max(xlist2)
    #print("xlist1 is ", xlist1)
    #print("max of xlist1 is ", maxl1)
    xlist1Norm = [x/ maxl1 for x in xlist1]
    #print("Normalized xlist1 is ", xlist1Norm)
    #print("xlist2 is ", xlist2)
    #print("max of xlist2 is ", maxl2)
    xlist2Norm = [x/ maxl2 for x in xlist2]
    #print("Normalized xlist2 is ", xlist2Norm)

    sumDS = 0
    for i in range(len(ticks)):
        diffSeries.append((xlist1Norm[i] - xlist2Norm[i])**2) #squares of differences
        sumDS += math.sqrt(diffSeries[i])

    #print("diffSeries is ", diffSeries)
    meanDS = sumDS/len(diffSeries)
    #print("The mean of the squares is ", meanDS)
    score = (1 - meanDS)*10
    #print("The sum of squares is ", sumDS)
    if score < 2.5:
        gbw = 'bad'
    elif score > 2.5 and score < 3.0:
        gbw = 'mediocre'
    elif score > 3.0 and score < 3.6:
        gbw = 'good'
    elif score > 3.6:
        gbw = 'excellent'
    return score, gbw

@app.route('/')
def index():
    start_date = '2020-01-22'
    end_date = str(datetime.date.today())
    query = 'tickersymbol'
    url = "https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv"
    filename = url
    df = pd.read_csv(filename, lineterminator='\n')
    tdate = start_date

    if query in request.args:
        tickerSymbol = request.args[query].upper()
    else:
        tickerSymbol = 'SPY'
    sDates, sCloses = Ticker(start_date, end_date, tickerSymbol)
    scDates, tCases, scCloses = CV_Stats(tdate, sDates, sCloses, df, end_date)
    sDates = scDates
    sCloses = scCloses
    sDates1 = pd.to_datetime(sDates)
    sDates1 = sDates1.strftime("%m-%d")
    plot_url = Plot(sDates1, sCloses, tickerSymbol, tCases)
    score, gbw = Correlation(sDates, sCloses, tCases)
    return render_template('index.html', title=('%s vs COVID-19' % tickerSymbol), plot_url=plot_url, symbol=tickerSymbol, score=score, gbw=gbw)
