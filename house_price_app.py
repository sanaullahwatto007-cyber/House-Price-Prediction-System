

import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("house_price_prediction_model.pkl")

# Load feature names
features = joblib.load("features.pkl")

st.title("🏠 House Price Prediction")

st.write("Enter house details to predict the price.")

# Input fields
square_footage = st.number_input("Square Footage", min_value=0.0)
num_bedrooms = st.number_input("Number of Bedrooms", min_value=0)
num_bathrooms = st.number_input("Number of Bathrooms", min_value=0)
year_built = st.number_input("Year Built", min_value=1800, max_value=2026)
lot_size = st.number_input("Lot Size", min_value=0.0)
garage_size = st.number_input("Garage Size", min_value=0)
neighborhood_quality = st.number_input(
    "Neighborhood Quality", min_value=0.0
)

# Prediction button
if st.button("Predict House Price"):

    # Create input data
    input_data = pd.DataFrame([[
        square_footage,
        num_bedrooms,
        num_bathrooms,
        year_built,
        lot_size,
        garage_size,
        neighborhood_quality
    ]], columns=features)

    # Prediction
    prediction = model.predict(input_data)

    st.success(f"Predicted House Price:$ {prediction[0]:,.2f}")

