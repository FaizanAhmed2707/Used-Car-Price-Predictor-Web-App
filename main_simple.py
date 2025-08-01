import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import GradientBoostingRegressor

# Page configuration
st.set_page_config(page_title="Used Car Price Predictor", layout="wide")

def load_model():
    """Load the trained model."""
    try:
        model = joblib.load('car_price_predictor.pkl')
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

def simple_prediction_page():
    """Simple prediction page without external dependencies."""
    st.title("🚗 Used Car Price Predictor")
    st.write("Predict the market value of used cars using machine learning.")
    
    # Load model
    model = load_model()
    if model is None:
        st.error("Model could not be loaded. Please check the model file.")
        return
    
    st.subheader("Input Car Details")
    
    # Input fields
    present_price = st.number_input('Current ex-showroom price (in Lakhs)', 
                                   min_value=2.5, max_value=25.0, step=0.1, value=5.0)
    kms_driven = st.number_input('Distance completed (in Kilometers)', 
                                min_value=100, max_value=500000, step=100, value=50000)
    
    fuel_type = st.selectbox('Fuel Type', ('Petrol', 'Diesel', 'CNG'))
    fuel_type_encoded = {'Petrol': 0, 'Diesel': 1, 'CNG': 2}[fuel_type]
    
    seller_type = st.selectbox('Seller Type', ('Dealer', 'Individual'))
    seller_type_encoded = {'Dealer': 0, 'Individual': 1}[seller_type]
    
    transmission = st.selectbox('Transmission Type', ('Manual', 'Automatic'))
    transmission_encoded = {'Manual': 0, 'Automatic': 1}[transmission]
    
    owner = st.slider("Number of Previous Owners", min_value=0, max_value=3, value=0)
    
    purchase_year = st.number_input('Purchase Year', min_value=1990, max_value=2024, value=2020)
    age = 2024 - purchase_year
    
    if st.button('Predict Price'):
        # Create input data
        input_data = pd.DataFrame({
            'Present_Price': [present_price],
            'Kms_Driven': [kms_driven],
            'Fuel_Type': [fuel_type_encoded],
            'Seller_Type': [seller_type_encoded],
            'Transmission': [transmission_encoded],
            'Owner': [owner],
            'Age': [age]
        })
        
        try:
            # Make prediction
            prediction = model.predict(input_data)
            
            if prediction[0] > 0:
                st.success(f'💰 **Predicted Price: {prediction[0]:.2f} Lakhs**')
                st.info(f'This car can be sold for approximately ₹{prediction[0]*100000:.0f}')
            else:
                st.warning("⚠️ This car may not be suitable for resale.")
                
        except Exception as e:
            st.error(f"Error making prediction: {e}")

def home_page():
    """Simple home page."""
    st.title("🚗 Welcome to Used Car Price Predictor")
    st.write("""
    This application helps you predict the market value of used cars using machine learning.
    
    **Features:**
    - 🎯 Accurate price predictions
    - 📊 Based on comprehensive data analysis
    - 🚀 Fast and easy to use
    
    **How to use:**
    1. Navigate to the "Predict Price" page
    2. Enter your car details
    3. Get instant price predictions
    """)

# Simple navigation
pages = {
    "Home": home_page,
    "Predict Price": simple_prediction_page
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Display the selected page
pages[selection]() 