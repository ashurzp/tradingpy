import datetime
import os

import pandas
import tushare


def stockPriceIntraday(ticker, folder):
    # Step 1. Get intraday data online
    intraday = tushare.get_hist_data(ticker, ktype='5')

    # Step 2. If the history exists, append
    file = folder + '/' + ticker + '.csv'
    if os.path.exists(file):
        history = pandas.read_csv(file, index_col=0)
        intraday.append(history)

    # Step 3. Inverse based on index
    intraday.sort_index(inplace=True)
    intraday.index.name = 'timestamp'

    # Step 4. Save
    intraday.to_csv(file)
    print('Intraday for [' + ticker + '] got.')


def get_cn_stocks():
    # Step 1. get tickets online
    tickersRawData = tushare.get_stock_basics()
    tickers = tickersRawData.index.tolist()
    # Step 2. Save the ticker list to a local file
    dateToday = datetime.datetime.today().strftime('%Y%m%d')
    file = './Data/TickerListCN/TicketList' + dateToday + '.csv'
    tickersRawData.to_csv(file, index=False)
    print('Tickers saved')
    # Step 3. Get stock price(in traday) for all
    for i, ticker in enumerate(tickers):
        try:
            print('Intraday', i, '/', len(tickers))
            stockPriceIntraday(ticker, folder='./Data/IntradayCN')
        except Exception:
            pass
    print('Intraday for all stock got.')


get_cn_stocks()
