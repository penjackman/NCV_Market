from flask import render_template
from flask import request
from flask import Flask

import matplotlib
matplotlib.use("Agg")
#import numpy as np
import pandas as pd
import datetime

import Ticker
import CV_Stats
import Plot

app = Flask(__name__)

@app.route('/')
def index():

    end_date = str(datetime.date.today())
    start_date1 = pd.to_datetime(end_date)
    start_date = start_date1 - datetime.timedelta(days=30)
    tdate = str(start_date.strftime("%Y-%m-%d"))

    query = 'tickersymbol'
    url = "https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv"
    filename = url
    df = pd.read_csv(filename, lineterminator='\n')
    tdate = start_date

    if query in request.args:
        tickerSymbol = request.args[query].upper()
    else:
        tickerSymbol = 'SPY'
    sDates, sCloses = Ticker.Ticker(start_date, end_date, tickerSymbol)
    scDates, tCases, scCloses = CV_Stats.CV_Stats(tdate, sDates, sCloses, df, end_date)
    sDates = scDates
    sCloses = scCloses
    sDates1 = pd.to_datetime(sDates)
    sDates1 = sDates1.strftime("%m-%d")

    score = 4.9
    score1 = 7.5
    CorrName = 'MSFT'
    CorrScore = 7.0
    SoarName = 'NFLX'
    SoarScore = 8.3
    SoarName = str(SoarName)
    SoarScore = float(str(SoarScore))
    CorrName = str(CorrName)
    CorrScore = float(str(CorrScore))

    plot_url = Plot.Plot(sDates1, sCloses, tickerSymbol, tCases)
    plot_url2 = ""
    return render_template('index.html', title=('%s vs COVID-19' % tickerSymbol), plot_url1=plot_url1, plot_url2=plot_url2, plot_url=plot_url, symbol=tickerSymbol)

@app.route('/feedback', methods = ['GET', 'POST'])
def feedback():

    if request.method == 'POST':
        uname = request.form.get('name1')
        ucomment = request.form.get('comment1')
        return render_template('showfb.html', uname=uname, ucomment=ucomment)

    return render_template('feedback.html')
