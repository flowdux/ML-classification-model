import streamlit as st, joblib, pandas as pd

model = joblib.load("fault_model.joblib")
st.title("Industrial Fault Detector")

t = st.slider("Temperature (C)", 40.0, 120.0, 60.0)
v = st.slider("Vibration (mm/s)", 0.0, 12.0, 2.0)
p = st.slider("Pressure (bar)", 2.0, 9.0, 6.0)
c = st.slider("Current (A)", 5.0, 25.0, 10.0)
r = st.slider("RPM", 1200.0, 1700.0, 1500.0)

if st.button("Predict"):
    X = pd.DataFrame([[t, v, p, c, r]],
        columns=["temperature", "vibration", "pressure", "current", "rpm"])
    st.success(f"Predicted state: {model.predict(X)[0]}")