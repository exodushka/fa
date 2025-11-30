import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("STARTING CRYPTO PORTFOLIO ANALYSIS...")

# 1. DATA DOWNLOAD
tickers = ['BTC-USD', 'ETH-USD', 'BNB-USD', 'SOL-USD', 'XRP-USD']
end_date = '2024-01-01'
start_date = '2023-01-01'

print("Downloading data...")
raw = yf.download(tickers, start=start_date, end=end_date)

if raw.empty:
    raise SystemExit("yf.download вернул пустой DataFrame — проверьте подключение и тикеры.")

# пытаемся получить Adjusted Close, потом Close, иначе используем получённый DF как есть
if isinstance(raw.columns, pd.MultiIndex):
    try:
        data = raw['Adj Close']
    except KeyError:
        try:
            data = raw['Close']
        except KeyError:
            try:
                data = raw.xs('Adj Close', axis=1, level=1)
            except Exception:
                try:
                    data = raw.xs('Close', axis=1, level=1)
                except Exception:
                    data = raw
else:
    if 'Adj Close' in raw.columns:
        data = raw['Adj Close']
    elif 'Close' in raw.columns:
        data = raw['Close']
    else:
        data = raw

data = data.dropna()

# 2. RETURNS CALCULATION
returns = np.log(data / data.shift(1)).dropna()

# Basic metrics
metrics = pd.DataFrame({
    'Return_annual_%': returns.mean() * 252 * 100,
    'Volatility_annual_%': returns.std() * np.sqrt(252) * 100
})

print("\nASSET METRICS:")
print(metrics.round(2))

# 3. VISUALIZATION
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))

# Plot 1: Normalized prices
normalized_prices = (data / data.iloc[0]) * 100
normalized_prices.plot(ax=ax1, linewidth=2)
ax1.set_title('Normalized Crypto Prices')
ax1.set_ylabel('Price (% from start)')

# Plot 2: Volatility
metrics['Volatility_annual_%'].plot(kind='bar', ax=ax2, color='lightcoral')
ax2.set_title('Annual Volatility')
ax2.set_ylabel('Volatility (%)')

# Plot 3: Correlation heatmap
correlation_matrix = returns.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
            square=True, fmt='.2f', ax=ax3)
ax3.set_title('Asset Correlations')

# Plot 4: BTC returns distribution
ax4.hist(returns['BTC-USD'], bins=40, alpha=0.7, color='skyblue', edgecolor='black')
ax4.axvline(returns['BTC-USD'].mean(), color='red', linestyle='--', linewidth=2)
ax4.set_title('BTC Daily Returns Distribution')
ax4.set_xlabel('Daily Return')
ax4.set_ylabel('Frequency')

plt.tight_layout()
plt.savefig('portfolio_charts.png')  # Save charts to file
plt.show()

# 4. PORTFOLIO ANALYSIS
print("\nPORTFOLIO COMPARISON:")

portfolios = {
    'Only BTC': [1, 0, 0, 0, 0],
    'Equal Weight': [0.2, 0.2, 0.2, 0.2, 0.2],
    'Conservative': [0.5, 0.3, 0.1, 0.05, 0.05],
    'Aggressive': [0.1, 0.2, 0.3, 0.2, 0.2]
}

def calculate_portfolio(weights, returns):
    portfolio_return = np.sum(returns.mean() * weights) * 252
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
    sharpe_ratio = portfolio_return / portfolio_volatility
    return portfolio_return, portfolio_volatility, sharpe_ratio

results = []
for name, weights in portfolios.items():
    ret, vol, sharpe = calculate_portfolio(weights, returns)
    results.append({
        'Portfolio': name,
        'Return_%': ret * 100,
        'Risk_%': vol * 100,
        'Sharpe': sharpe
    })

results_df = pd.DataFrame(results)
print(results_df.round(3))

# 5. RISK ANALYSIS (VaR)
print("\nRISK ANALYSIS (VaR):")

best_idx = results_df['Sharpe'].idxmax()
best_portfolio = results_df.loc[best_idx]
# заменено: получаем имя лучшего портфеля и берем веса из словаря portfolios
best_name = best_portfolio['Portfolio']
best_weights = np.array(portfolios[best_name])

portfolio_returns = returns.dot(best_weights)
var_95 = np.percentile(portfolio_returns, 5)
var_95_amount = abs(var_95 * 1000)

print(f"Best portfolio: {best_portfolio['Portfolio']}")
print(f"Daily VaR (95% confidence): {var_95*100:.2f}%")
print(f"Potential losses per $1000: ${var_95_amount:.2f}")