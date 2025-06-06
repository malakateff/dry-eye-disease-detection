import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.title("Dry Eye Disease Prediction")

gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 18, 100, 30)
sleep_duration = st.slider("Sleep Duration (hours)", 0, 12, 6)
sleep_quality = st.slider("Sleep Quality (0-10)", 0, 10, 5)
stress_level = st.slider("Stress Level (0-10)", 0, 10, 5)
bp = st.number_input("Blood Pressure (mmHg)", 80, 200, 120)
heart_rate = st.slider("Heart Rate (bpm)", 50, 120, 75)
daily_steps = st.slider("Daily Steps", 0, 30000, 7000)
physical_activity = st.slider("Physical Activity (mins/day)", 0, 180, 30)
height = st.number_input("Height (cm)", 120, 220, 165)
weight = st.number_input("Weight (kg)", 30, 150, 60)
screen_time = st.slider("Screen Time (hrs/day)", 0, 24, 5)

gender_val = 1 if gender == "Male" else 0
input_data = np.array([[gender_val, age, sleep_duration, sleep_quality,
                        stress_level, bp, heart_rate, daily_steps,
                        physical_activity, height, weight, screen_time]])

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("🔴 Likely Dry Eye Disease")
    else:
        st.success("✅ No Dry Eye Disease Detected")
