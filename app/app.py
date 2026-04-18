import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("models/traffic_model.pkl")

st.title(" AI Traffic Congestion Predictor")

st.markdown("Enter traffic details to predict congestion level")

# Inputs
vehicle_count = st.slider("Vehicle Count", 0, 200, 50)
avg_speed = st.slider("Average Speed", 0, 100, 40)
signal_delay = st.slider("Signal Delay (seconds)", 0, 100, 10)

is_peak_hour = st.selectbox("Peak Hour?", [0, 1])
accident_reported = st.selectbox("Accident Reported?", [0, 1])

weather = st.selectbox("Weather", ["clear", "rain", "fog"])
road_type = st.selectbox("Road Type", ["city", "highway"])
traffic_density = st.selectbox("Traffic Density", ["low", "medium", "high"])
location = st.selectbox("Location", ["Delhi", "Mumbai", "Chandigarh", "Ludhiana", "Bangalore"])

# Encode manually (same as training)
encode = {
    'low': 0, 'medium': 1, 'high': 2,
    'city': 0, 'highway': 1,
    'clear': 0, 'fog': 1, 'rain': 2
}

input_data = pd.DataFrame([{
    "location": 0,
    "vehicle_count": vehicle_count,
    "avg_speed": avg_speed,
    "traffic_density": encode[traffic_density],
    "road_type": encode[road_type],
    "weather": encode[weather],
    "is_peak_hour": is_peak_hour,
    "accident_reported": accident_reported,
    "signal_delay": signal_delay
}])

# Predict
if st.button("Predict"):
    prediction = model.predict(input_data)[0]

    labels = {0: "Low", 1: "Medium", 2: "High"}
    result = labels[prediction]

    if result == "Low":
        st.success(f"Traffic Level: {result} ")
    elif result == "Medium":
        st.warning(f"Traffic Level: {result} ")
    else:
        st.error(f"Traffic Level: {result} ")

joblib.dump(model, "models/traffic_model.pkl")
print("Model saved successfully!")
