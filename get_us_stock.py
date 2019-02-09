import datetime
import io
import os
import time

import pandas
import requests

# API KEY: WRP4CN95OUBC57X5


def dataframeFromUrl(url):
    dataString = requests.get(url).content
    parsedResult = pandas.read_csv(io.StringIO(
        dataString.decode('utf-8')), index_col=0)
    return parsedResult


def stockPriceIntraday(ticker, folder):
    # Step 1. Get data online
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&apikey=WRP4CN95OUBC57X5&interval=1min&outputsize=full&datatype=csv'.format(
        ticker=ticker)
    intraday = dataframeFromUrl(url)

    # Step 2. Append if history exists
    file = folder + '/' + ticker + '.csv'
    if os.path.exists(file):
        history = pandas.read_csv(file, index_col=0)
        intraday.append(history)

    # Step 3. Inverse based on index
    intraday.sort_index(inplace=True)

    # Step 4. Save
    intraday.to_csv(file)
    print('Intraday for [' + ticker + '] got.')


def get_us_stocks():
    # Step 1. get online company list from nasdaq
    url = 'https://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download'

    dataString = requests.get(url).content
    tickersRawData = pandas.read_csv(io.StringIO(dataString.decode('utf-8')))
    tickers = tickersRawData['Symbol'].tolist()

    # Step 2. save the ticker list to a local file
    dateToday = datetime.datetime.today().strftime('%Y%m%d')
    file = './Data/TickerListUS/TicketList' + dateToday + '.csv'
    tickersRawData.to_csv(file, index=False)
    print('Tickers saved')

    # Step 3. Get stock price(intraday)
    for i, ticker in enumerate(tickers):
        try:
            print('Intraday', i, '/', len(tickers))
            stockPriceIntraday(ticker, folder='./Data/IntradayUS')
            time.sleep(12)
        except Exception:
            pass
    print('Intraday for all stock got.')


get_us_stocks()
