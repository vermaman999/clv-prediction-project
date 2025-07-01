import pandas as pd
import numpy as np
from lifelines import KaplanMeierFitter
import plotly.express as px

# Step 1: Load data
try:
    data = pd.read_csv('customer_data.csv')
    print("Data loaded successfully!")
except FileNotFoundError:
    print("Error: File 'customer_data.csv' not found.")
    exit()

# Step 2: Fit Kaplan-Meier model for tenure
kmf = KaplanMeierFitter()
kmf.fit(data['TenureMonths'], event_observed=data['Churn'])
survival_prob = kmf.survival_function_

# Step 3: Calculate CLV (simplified: tenure * monthly spend)
data['CLV'] = data['TenureMonths'] * data['MonthlySpend']

# Step 4: Visualize survival curve
fig = px.line(survival_prob, x=survival_prob.index, y='KM_estimate',
              title='Customer Survival Curve (Probability of Staying)')
fig.write_image('clv_plot.png')
fig.show()

# Step 5: Save CLV stats
clv_stats = data[['CustomerId', 'CLV', 'MonthlySpend', 'TenureMonths']].describe()
clv_stats.to_csv('clv_stats.csv')
print("CLV Stats:\n", clv_stats)