import streamlit as st
import numpy as np
import joblib
import os

BASE_DIR = os.path.dirname(__file__)

model = joblib.load(os.path.join(BASE_DIR, "rf_model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "scaler.pkl"))
features = joblib.load(os.path.join(BASE_DIR, "features.pkl"))

st.title("💳 Credit Card Fraud Detection")

st.write("Enter transaction details:")

input_data = []

for feature in features:
    value = st.number_input(f"{feature}", value=0.0)
    input_data.append(value)

if st.button("Predict"):
    input_array = np.array([input_data])
    input_scaled = scaler.transform(input_array)

    prediction = model.predict(input_scaled)
    prob = model.predict_proba(input_scaled)[0][1]

    if prediction[0] == 1:
        st.error(f"🚨 Fraud Detected ({prob:.2f})")
    else:
        st.success(f"✅ Legit Transaction ({prob:.2f})")