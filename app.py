import streamlit as st
import pandas as pd

st.title("Amex CLV Prediction Dashboard")

# Show CLV stats
try:
    clv_stats = pd.read_csv('clv_stats.csv')
    st.write("CLV Statistics:")
    st.dataframe(clv_stats)
except:
    st.write("Error: Run clv_prediction.py first.")

# Show plots
st.image('clv_plot.png')
st.image('causal_plot.png')