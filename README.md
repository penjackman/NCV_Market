# NCV_Market
This project is a website for people to check the strength index of stocks in the time of the corona virus pandemic. The RSI (relative strength index) of the stock is evaluated as well as how the stock correlates to the total and daily confirmed cases. 

One key purpose is to keep people's searches in a database of tickers (i.e. stock symbols). The RSI for this database is updated daily. So instead of having every stock's RSI in there, we encorage people to find their own stocks. In return, people can also look at what others have searched. 

In the final launch, we will also have Sentiment. People who search for a stock or just look at the existing stocks can enter their sentiment. 

We will also have feedback and comments (at least in the initial launch) and gather them in a separate database.

Data_Process:
- Get stock market data from yfinance
- Scrape Coronavirus data from Worldometers and/or from somewhere with history
- Build history if not available elsewhere on Web
- Persist data
- Use panda or matplotlib to plot graphs

Statistical functions:
- Pearson method correlation from numpy (numpy.corrcoef) between stock performance and confirmed cases
- 65-day moving average of RSI of a stock with a period of 10-days (10 trading days)

Database
- Sqlite3 (python) for stocks and for feedback/commments

Website FrontEnd (FE):
- Register a website (name and hosting: will it be tickerCV.com)

Finally, connect Website FE with Data_Process to complete the mvp.

Sources:
1. Johns Hopkins CSSEGI: https://github.com/CSSEGISandData/COVID-19
2. Cleaned up data Worldwide: https://github.com/datasets/covid-19/blob/master/data/time-series-19-covid-combined.csv
3. Worldometers (daily status): https://www.worldometers.info/coronavirus/



Target Date for MVP: April 25, 2020.
