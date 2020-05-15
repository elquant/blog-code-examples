import pandas_datareader as web
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

plt.style.use('ggplot')

ticker = 'MSFT'
data_source = 'yahoo'
start = dt.datetime(2019, 1, 1)
end = dt.datetime(2019, 12, 31)
num_simulations = 50
num_days = 252

prices = web.DataReader(ticker, data_source, start, end)['Close']
returns = prices.pct_change()
daily_vol = returns.std()
last_price = prices[-1]

simulation_df = pd.DataFrame()

for i in range(num_simulations):
    synthetic_price_serie = [last_price]
    for j in range(num_days):
        synthetic_price = synthetic_price_serie[j] * (1 + np.random.normal(0, daily_vol))
        synthetic_price_serie.append(synthetic_price)
    simulation_df[i] = synthetic_price_serie

fig = plt.figure()
fig.suptitle(f"Monte Carlo Simulation ({ticker}, with synthetic prices)")
plt.plot(simulation_df)
plt.axhline(y=last_price, color='black', linestyle='--')
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()
