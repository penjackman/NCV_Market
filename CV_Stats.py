
#Goal: Scrape Worldometers
#authors: Mihir, Bharadwaj, <add more>

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import yfinance as yf
import numpy as np
import pandas as pd
import requests
import csv
import datetime

from os import getcwd

url = "https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv"

directory = getcwd()
print("directory is ", directory)
filename = r'C:\Users\dubco\OneDrive\Documents\ncov_history.csv'

# r = requests.get(url)

# sr = str(r.content)

# f = open(filename,'w')
# f.write(sr)
# f.close()
# print("length of sr is ", len(sr))

print(filename)
print("starting")
covid_data = pd.read_csv(filename, nrows=4)
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
end_date = '2020-01-23'

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
    print("Date: ", tdate, "\tConfirmed cases: ", tconfirm)
    if tdate == end_date:
         break
    tdate1 = pd.to_datetime(tdate)
    tdate1 = tdate1 + datetime.timedelta(days=1)
    tdate = tdate1.strftime("%Y-%m-%d")
    print("Next date ", tdate)

# tsdate = "2020-1-22"
# tedate = "2020-1-25"
# after_start_date = df["Date"] >= tsdate
# before_end_date = df["Date"] <= tedate
# between_two_dates = after_start_date & before_end_date
# touts = df.loc[between_two_dates]


# # covid_data = csv.DictReader(open(filename))
# # for row in covid_data:
# #     print(row['Date/Country'])

# print("done")