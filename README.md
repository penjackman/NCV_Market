# NCV_Market
This project collects novel corona virus stats and plots it against the stock market.

The goal here is to have a website where people can visit to check the novel corona virus stats (such as total cases per country) against the stock market (for instance, against S&P index by default).

For instance, a person can visit the website and enter a stock ticker symbol XXX into a box, and the website will show a graph from Jan 1st to now with Coronavirus stats and the stock price of XXX.

So, this project has many stages and we have to execute this quickly to take the website live. It definitely needs to be collaborative as there is - surprisingly - a lot of work to be done.

At this point, the "README" is just a plan to develop this project. Here are the various stages for the minimum viable project (MVP):

Data_Process:
- Get stock market data from yfinance
- Scrape Coronavirus data from Worldometers and/or from somewhere with history
- Build history if not available elsewhere on Web
- Persist data
- Use panda or matplotlib to plot graphs

Website:
- Register a website (name and hosting: to be determined)
- Have some basic white background 
- Have an input for ticker symbol

Finally, integrate Data_Process into Website. 

Sources:
1. Johns Hopkins CSSEGI: https://github.com/CSSEGISandData/COVID-19
2. Cleaned up data Worldwide: https://github.com/datasets/covid-19/blob/master/data/time-series-19-covid-combined.csv
3. Worldometers (daily status): https://www.worldometers.info/coronavirus/



Target Date for MVP: March 25, 2020.
