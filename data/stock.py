import pandas as pd


def read_all(symbol):
    return pd.read_csv('data/stock/{}.csv'.format(symbol))


def read_date(symbol):
    df = read_all(symbol)
    return df['Date']


def read_open_price(symbol):
    df = read_all(symbol)
    return df['Open']


def read_high_price(symbol):
    df = read_all(symbol)
    return df['High']


def read_low_price(symbol):
    df = read_all(symbol)
    return df['Low']


def read_close_price(symbol):
    df = read_all(symbol)
    return df['Close']


def read_adjusted_close_price(symbol):
    df = read_all(symbol)
    return df['Adj Close']


def read_volume(symbol):
    df = read_all(symbol)
    return df['Volume']
