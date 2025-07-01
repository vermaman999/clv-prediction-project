import pandas as pd
import numpy as np

# Generate synthetic customer data
np.random.seed(42)
n = 1000
data = {
    'CustomerId': range(1, n+1),
    'TenureMonths': np.random.exponential(scale=60, size=n).astype(int),
    'Churn': np.random.binomial(1, 0.3, n),
    'MonthlySpend': np.random.normal(500, 200, n),
    'CreditScore': np.random.normal(650, 50, n).astype(int),
    'ReceivedOffer': np.random.binomial(1, 0.5, n),
}
df = pd.DataFrame(data)
df['MonthlySpend'] = df['MonthlySpend'] + df['ReceivedOffer'] * np.random.normal(100, 50, n)
df.to_csv('customer_data.csv', index=False)
print("Synthetic data saved to customer_data.csv")