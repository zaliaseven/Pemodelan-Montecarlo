import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
start = dt.datetime(2018, 1, 1)
end = dt.datetime(2019, 1, 1)

prices = web.DataReader('GOOGL', 'yahoo', start, end)['Close']
returns = prices.pct_change()

last_price = prices[-1]

num_simulations = 1000
num_days = 252

simulation_df = pd.DataFrame()

for x in range(num_simulations):
    count = 0
    daily_vol = returns.std()

    price_series = []

    price = last_price * (1 + np.random.normal(0, daily_vol))
    price_series.append(price)

    for y in range(num_days):
        if count == 252:
            break
        price = price_series[count] * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)
        count += 1

    simulation_df[x] = price_series

fig = plt.figure()
fig.suptitle('Simulasi MonteCarlo : Google (Rizaldi Fadilah - 152017131)')
plt.plot(simulation_df)
plt.axhline(y = last_price, color = 'r', linestyle = '-')
plt.xlabel('Hari')
plt.ylabel('Harga')
plt.show()

