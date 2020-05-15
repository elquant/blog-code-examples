import random
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

initial_capital = 10000
num_trades = 5000
num_simulations = 200

pnl_serie = random.choices(population=range(-200, 200), k=num_trades)

simulation_df = pd.DataFrame()

for i in range(num_simulations):
    current_capital = initial_capital
    equity_curve = [current_capital]
    pnl_simulation = random.choices(population=pnl_serie, k=num_trades)
    for j in range(num_trades):
        current_capital += pnl_simulation[j]
        equity_curve.append(current_capital)
    simulation_df[i] = equity_curve

fig = plt.figure()
fig.suptitle("Monte Carlo Simulation (with repetition)")
plt.plot(simulation_df)
plt.axhline(y=initial_capital, color='black', linestyle='--')
plt.xlabel('Trade')
plt.ylabel('Equity')
plt.show()
