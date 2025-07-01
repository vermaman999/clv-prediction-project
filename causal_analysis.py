import pandas as pd
from causalinference import CausalModel
import plotly.express as px

# Load data
data = pd.read_csv('customer_data.csv')

# Causal inference
Y = data['MonthlySpend'].values
D = data['ReceivedOffer'].values
X = data[['CreditScore', 'TenureMonths']].values
causal = CausalModel(Y, D, X)
causal.est_propensity()
causal.est_via_matching()
effect = causal.estimates['matching']['ate']

# Visualize
fig = px.bar(x=['Offer Impact'], y=[effect], title='Causal Effect of Offer on Spending')
fig.write_image('causal_plot.png')
fig.show()
print(f"Offer increases spending by ${effect:.2f} per month")
