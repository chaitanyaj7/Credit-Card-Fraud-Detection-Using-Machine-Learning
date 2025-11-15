# Filename: app_manual_input.py
import streamlit as st
import pandas as pd
import joblib

# ----------------- Load Trained Model -----------------
model = joblib.load("xgb_fraud_model.pkl")
# Scaler removed, using raw input

# ----------------- Page Config -----------------
st.set_page_config(page_title="Credit Card Fraud Detection", layout="wide")

# ----------------- Header -----------------
st.title("Credit Card Fraud Detection System")
st.write("""
Enter transaction details manually and check if it is fraudulent.
""")

# ----------------- Manual Input -----------------
st.subheader("Transaction Input")

# Create dictionary to store user input
input_data = {}

# Time input
input_data['Time'] = st.number_input("Time", min_value=0.0, value=0.0, step=1.0)

# V1 to V28 inputs
for i in range(1, 29):
    input_data[f'V{i}'] = st.number_input(f"V{i}", value=0.0, step=0.01)

# Amount input
input_data['Amount'] = st.number_input("Amount", min_value=0.0, value=0.0, step=1.0)

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# ----------------- Prediction -----------------
if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    result = "Normal ✅" if prediction == 0 else "Fraudulent ⚠️"
    st.markdown(f"### Prediction Result: **{result}**")

# ----------------- Footer -----------------
st.markdown("---")
st.markdown("""
<p style="text-align:center; color:gray; font-size:14px;">
Developed by <b>Chaitanya Jamdar</b> | 
LinkedIn: <a href="https://www.linkedin.com/in/chaitanya-jamdar" target="_blank">Chaitanya Jamdar</a> | 
Email: <a href="mailto:jamdarchaitanya127@gmail.com">jamdarchaitanya127@gmail.com</a>
</p>
""", unsafe_allow_html=True)
