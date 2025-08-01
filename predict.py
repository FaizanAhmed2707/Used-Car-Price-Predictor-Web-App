import streamlit as st
import pandas as pd
import datetime
import xgboost as xgb
from streamlit_lottie import st_lottie
import requests
import joblib


# Load the model
model = joblib.load('car_price_predictor.pkl')


def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def car_price_prediction():
    st.title("Predict Used Car Prices")
    
    lottie_car = load_lottie_url("https://lottie.host/ce2413bb-6b81-4a4d-9d6f-6ac7b3926c73/u4fatRJr4p.json")
    st_lottie(lottie_car, height=300, key="car_animation")

    # Your existing car price prediction code
    st.subheader("Input Car Details")
    st.text_input("Car Brand (e.g. Toyota, Honda, Ford)")
    st.text_input("Car Model (e.g. Corolla, Civic, Focus)")
    
    p1 = st.number_input('What is the current ex-showroom price of the car? (In Lakhs)', min_value=2.5, max_value=25.0, step=0.1) 
    p2 = st.number_input('What is the distance completed by the car in Kilometers?', min_value=100, max_value=50000000, step=100)
    s1 = st.selectbox('What is the fuel type of the car?', ('Petrol', 'Diesel', 'CNG'))
    p3 = {'Petrol': 0, 'Diesel': 1, 'CNG': 2}[s1]
    s2 = st.selectbox('Are you a dealer or an individual?', ('Dealer', 'Individual'))
    p4 = {'Dealer': 0, 'Individual': 1}[s2]
    s3 = st.selectbox('What is the Transmission Type?', ('Manual', 'Automatic'))
    p5 = {'Manual': 0, 'Automatic': 1}[s3]
    p6 = st.slider("Number of Owners the car previously had", min_value=0, max_value=3)
    years = st.number_input('In which year was the car purchased?', min_value=1990, max_value=datetime.datetime.now().year, step=1)
    p7 = datetime.datetime.now().year - years

    data_new = pd.DataFrame({
        'Present_Price': [p1],
        'Kms_Driven': [p2],
        'Fuel_Type': [p3],
        'Seller_Type': [p4],
        'Transmission': [p5],
        'Owner': [p6],
        'Age': [p7]
    })

    if st.button('Predict'):
        prediction = model.predict(data_new)
        if prediction > 0:
            st.success(f'You can sell the car for {prediction[0]:.2f} lakhs.')
        else:
            st.warning("You will not be able to sell this car!")
