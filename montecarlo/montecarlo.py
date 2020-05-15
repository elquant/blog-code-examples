import random
import matplotlib.pyplot as plt

plt.style.use('ggplot')

initial_capital = 10000

pnl_serie = random.choices(population=range(-50, 200), k=1000)
pnl_serie_shuffled = random.sample(population=pnl_serie, k=len(pnl_serie))
pnl_serie_sorted = pnl_serie.copy()
pnl_serie_sorted.sort()
pnl_serie_sorted_reversed = pnl_serie.copy()
pnl_serie_sorted_reversed.sort(reverse=True)

def calculate_equity_curve(serie):
    current_capital = initial_capital
    equity_curve = [current_capital]
    for pnl in serie:
        current_capital += pnl
        equity_curve.append(current_capital)
    return equity_curve

original_equity_curve = calculate_equity_curve(pnl_serie)
shuffled_equity_curve = calculate_equity_curve(pnl_serie_shuffled)
wort_case_equity_curve = calculate_equity_curve(pnl_serie_sorted)
best_case_equity_curve = calculate_equity_curve(pnl_serie_sorted_reversed)

fig = plt.figure()
fig.suptitle("Monte Carlo Simulation (without repetition)")
plt.plot(original_equity_curve)
plt.plot(shuffled_equity_curve)
plt.plot(wort_case_equity_curve)
plt.plot(best_case_equity_curve)
plt.axhline(y=initial_capital, color='black', linestyle='--')
plt.xlabel('Trade')
plt.ylabel('Equity')
plt.show()
