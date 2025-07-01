import streamlit as st
import pandas as pd

st.title("CLV Project Test")
try:
    data = pd.read_csv('customer_data.csv')
    st.write("Customer Data Preview:")
    st.dataframe(data.head())
except:
    st.write("Error: Run generate_data.py first.")