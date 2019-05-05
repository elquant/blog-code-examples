import pandas as pd
import matplotlib.pyplot as plt


def data_test():
    symbol = 'CAT'
    df = pd.read_csv('../data/stocks/{}.csv'.format(symbol))
    print(df)
    print(df.head())
    print(df.tail())
    print(df[10:20])
    print(symbol, df['Close'].max())
    df['Close'].plot()
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title('Caterpillar Inc. Closing Price')
    plt.show()


if __name__ == '__main__':
    data_test()
