from flask import render_template
from flask import request
from flask import Flask

import matplotlib
matplotlib.use("Agg")
#import numpy as np
import pandas as pd
import datetime
from datetime import date
import sqlite3

import Ticker
import CV_Stats
import Plot

import sql_feedback as sfb

app = Flask(__name__)

fb_file = ':memory:' # in-memory

# CREATE a database in RAM or file
fdb = sqlite3.connect(fb_file)

cursor = sfb.createfb_db(fdb)


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

    plot_url = Plot.Plot(sDates1, sCloses, tickerSymbol, tCases)
    #cmap2 = matplotlib.cm.bone
    #plot_url1 = HeatMap.HeatMap(score, tickerSymbol, cmap2, CorrName, CorrScore)
    plot_url1 = ""

    #cmap = matplotlib.cm.plasma
    #plot_url2 = HeatMap.HeatMap(score1, tickerSymbol, cmap, SoarName, SoarScore)
    plot_url2 = ""
    return render_template('index.html', title=('%s vs COVID-19' % tickerSymbol), plot_url1=plot_url1, plot_url2=plot_url2, plot_url=plot_url, symbol=tickerSymbol)

@app.route('/feedback', methods = ['GET', 'POST'])
def feedback():

    if request.method == 'POST':
        uname = request.form.get('name1')
        ucomment = request.form.get('comment1')
        udate = date.today().strftime('%Y-%m-%d')
        sfb.updatefb_db(fdb, uname, ucomment, udate)
        return render_template('showfb.html', uname=uname, ucomment=ucomment)

    cursor = fdb.cursor()

    all_rows = sfb.getrecentfb_db(cursor, 5)
    return render_template('feedback.html', all_rows=all_rows)
