import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the trained model
try:
    model = joblib.load('malaria_climate_model.pkl')
except:
    model = None

st.set_page_config(page_title="Malaria Prevalence Predictor", layout="centered")

st.title("🦟 Malaria Prevalence Predictor")
st.write("This interactive app predicts the estimated state-level malaria prevalence rate in Nigeria based on annual meteorological factors using a Random Forest model trained on integrated DHS & Open-Meteo data.")

st.sidebar.header("Input Environmental Factors")

# User inputs
temp_input = st.sidebar.slider(
    "Annual Mean Temperature (°C)",
    min_value=20.0,
    max_value=32.0,
    value=26.5,
    step=0.1,
    help="Average daily mean temperature over the course of the year."
)

rain_input = st.sidebar.slider(
    "Annual Total Precipitation (mm)",
    min_value=200.0,
    max_value=3500.0,
    value=1100.0,
    step=10.0,
    help="Total accumulated rainfall throughout the year."
)

st.subheader("Prediction Results")

if model is not None:
    # Predict
    input_data = pd.DataFrame([[temp_input, rain_input]], columns=['annual_mean_temp_c', 'annual_total_precipitation_mm'])
    prediction = model.predict(input_data)[0]
    
    # Display Gauge / Metrics
    st.metric(label="Predicted Malaria Prevalence (RDT %)", value=f"{prediction:.2f}%")
    
    # Contextual Guidance
    if prediction < 20:
        st.success("🟢 Low Prevalence Risk Zone")
    elif prediction < 45:
        st.warning("🟡 Moderate Prevalence Risk Zone")
    else:
        st.error("🔴 High Prevalence Risk Zone")
        
    st.info(f"Input Parameters: Average Temperature of {temp_input}°C and total annual rainfall of {rain_input}mm.")
else:
    st.error("Model file 'malaria_climate_model.pkl' not found. Please make sure to run the training block inside your notebook first.")
