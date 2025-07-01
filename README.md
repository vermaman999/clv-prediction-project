# clv-prediction-project
maximize customer lifetime value (CLV) by retaining high-value cardholders and optimizing offers (e.g., cashback, travel rewards). This project predicts how long customers stay (tenure) and how much they’ll spend, plus estimates how offers impact spending

Dynamic CLV Prediction
Predicts customer lifetime value using survival analysis and causal inference.
How to Run

Install: pip install pandas numpy lifelines causalinference plotly kaleido streamlit.
Run generate_data.py, then clv_prediction.py, causal_analysis.py, streamlit run app.py.
View dashboard on Streamlit Cloud (link TBD).

Output

Survival curve: clv_plot.png.
Causal effect: causal_plot.png.
Stats: clv_stats.csv.
