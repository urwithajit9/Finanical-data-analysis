import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pyfolio as pf

# Function to generate random daily returns
def generate_random_returns(start_date, end_date):
    date_range = pd.date_range(start_date, end_date)
    returns = np.random.normal(0.0001, 0.01, len(date_range))
    return pd.Series(returns, index=date_range)

# Generate random daily returns for two assets and a benchmark
start_date = "2022-01-01"
end_date = "2022-12-31"
returns_asset1 = generate_random_returns(start_date, end_date)
returns_asset2 = generate_random_returns(start_date, end_date)
benchmark_returns = generate_random_returns(start_date, end_date)

# Create a DataFrame with the returns
returns_data = pd.DataFrame({
    'Asset1': returns_asset1,
    'Asset2': returns_asset2,
    'Benchmark': benchmark_returns
})

# Calculate cumulative returns
cumulative_returns = (1 + returns_data).cumprod()

# Plot cumulative returns
cumulative_returns.plot(figsize=(10, 6))
plt.title('Cumulative Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.show()

# Use Pyfolio for performance analysis
returns_data['Benchmark'] = benchmark_returns
pf.create_returns_tear_sheet(returns_data['Asset1'], benchmark_rets=returns_data['Benchmark'])
