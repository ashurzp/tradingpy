import matplotlib
import matplotlib.pyplot as plt
import mpl_finance
import pandas

matplotlib.style.use('ggplot')


def stockPricePlot(ticker):
    print('dsqdsq')
    # Step 1. load data

    history = pandas.read_csv(
        './Data/IntradayUS/' + ticker + '.csv', parse_dates=True, index_col=0)

    # Step 2. Data manipulation
    close = history['close']
    close = close.reset_index()
    close['timestamp'] = close['timestamp'].map(matplotlib.dates.date2num)

    ohlc = history[['open', 'high', 'low', 'close']].resample('1H').ohlc()
    ohlc = ohlc.reset_index()
    ohlc['timestamp'] = ohlc['timestamp'].map(matplotlib.dates.date2num)
    # Step 3. Plot Figures.
    # Subplot 1. scatter plot.
    subplot1 = plt.subplot2grid((2, 1), (0, 0), rowspan=1, colspan=1)
    subplot1.xaxis_date()
    subplot1.plot(close['timestamp'], close['close'], 'b.')
    plt.title(ticker)

    # Subplot 2. candle stick plot
    subplot2 = plt.subplot2grid(
        (2, 1), (1, 0), rowspan=1, colspan=1, sharex=subplot1)
    mpl_finance.candlestick_ohlc(
        ax=subplot2, quotes=ohlc.values, width=0.01, colorup='g', colordown='r')
    plt.show()


stockPricePlot('AAWW')
