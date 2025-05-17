import streamlit as st
import joblib
import pandas as pd

   # Load the model
model = joblib.load("spending_score_predictor.pkl")

st.title("Spending Score Predictor")

   # Input fields
age = st.number_input("Age", min_value=18, max_value=100, value=30)
income = st.number_input("Annual Income (k$)", min_value=0, max_value=200, value=50)
sentiment = st.number_input("Sentiment Score", min_value=-1.0, max_value=1.0, value=0.0)

   # Predict button
if st.button("Predict"):
    input_data = pd.DataFrame({
           'Age': [age],
           'Annual Income (k$)': [income],
           'Watson_Sentiment': [sentiment]
    })
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Spending Score: {prediction:.2f}")