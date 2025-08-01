import streamlit as st
import pandas as pd
import datetime
from sklearn.ensemble import GradientBoostingRegressor
import joblib
import requests
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
import os
import google.generativeai as genai
from dotenv import load_dotenv

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load environment variables
load_dotenv()

# Configure Gemini AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load the pre-trained model
model = joblib.load('car_price_predictor.pkl')

def main():

    # Horizontal navigation bar
    selected = option_menu(
        menu_title="Mini Project by 028", 
        options=["Predict Used Car Prices", "Compare Cars", "Get Car Recommendations"], 
        icons=["car", "columns", "clipboard-data"], 
        menu_icon="cast", 
        default_index=0, 
        orientation="vertical",
        
    )

     # Load Lottie animation
    lottie_car = load_lottie_url("https://lottie.host/e639c2a9-3015-437b-adfc-aa5325d48a21/CZEhVgtO68.json")

    # Display the Lottie animation at the start of the app
    st_lottie(lottie_car, height=300, key="car_animation")

    if selected == "Predict Used Car Prices":
        car_price_prediction()
    elif selected == "Compare Cars":
        car_comparison_tool()
    elif selected == "Get Car Recommendations":
        car_recommendation_system()

def car_price_prediction():
    # Custom HTML and CSS for the header
    html_temp = """
    <div style="background-color: #45171d; padding:16px; border-radius: 30px;">
        <h1 style="color: #fecea8; text-align:center;">Used Car Price Predictor</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Additional custom CSS
    css_code = """
    <style>
        .reportview-container {
            background-color: #D0B8A8 !important;
        }
        .sidebar .sidebar-content {
            background-color: #E2E2B6;
        }
        .stButton>button {
            background-color: #dc2f2f;
            color: white;
            border-radius: 5px;
        }
        .stButton>button:hover {
            background-color: orange;
            color: black;
        }
        .stSelectbox>div>div {
            background-color: #45171d;
        }
    </style>
    """
    st.markdown(css_code, unsafe_allow_html=True)

    # Input fields for user data
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

    # Create the DataFrame for prediction
    data_new = pd.DataFrame({

        'Present_Price': [p1],
        'Kms_Driven': [p2],
        'Fuel_Type': [p3],
        'Seller_Type': [p4],
        'Transmission': [p5],
        'Owner': [p6],
        'Age': [p7]
    })

    # Predict and display the result
    try:
        if st.button('Predict'):
            prediction = model.predict(data_new)
            if prediction > 0:
                st.balloons()
                st.success(f'You can sell the car for {prediction[0]:.2f} lakhs.')
            else:
                st.warning("You will not be able to sell this car!")   
    except Exception as e:
        st.warning(f"Oops! Something went wrong: {e}")
    if st.button("Get Tips related to Used Cars"):
        car_tips = get_car_tips()
        st.markdown("## Recommended Cars:")
        st.write(car_tips)

def car_comparison_tool():
    # Custom HTML and CSS for the header
    html_temp = """
    <div style="background-color: #45171d; padding:16px; border-radius: 30px;">
        <h1 style="color: #fecea8; text-align:center;">Car Comparison Tool</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    # Custom CSS for Car Comparison Tool
    css_code = """
    <style>
        .reportview-container {
            background-color: #D0B8A8 !important; /* Change to your desired color */
        }
        .stTextInput>div>div>input {
            background-color: #45171d;
        }
        .stButton>button {
            background-color: #dc2f2f;
            color: white;
            border-radius: 5px;
        }
        .stButton>button:hover {
            background-color: orange;
            color: black;
        }
    </style>
    """
    st.markdown(css_code, unsafe_allow_html=True)

    # Input fields for car comparison
    st.subheader("Enter Details for Car 1")
    car1_brand = st.text_input("Enter the brand of the first car")
    car1_model = st.text_input("Enter the model of the first car")
    
    st.subheader("Enter Details for Car 2")
    car2_brand = st.text_input("Enter the brand of the second car")
    car2_model = st.text_input("Enter the model of the second car")
    
    if st.button("Compare Cars"):
        car1_details = get_car_details(car1_brand, car1_model)
        car2_details = get_car_details(car2_brand, car2_model)
        
        if car1_details and car2_details:
            comparison_result = compare_cars(car1_details, car2_details)
            st.markdown("## Comparison Results:")
            st.write(comparison_result)
        else:
            st.warning("Unable to fetch details for one or both cars.")

def car_recommendation_system():
    # Input fields for car recommendation
    st.subheader("Enter Your Preferences")
    budget = st.number_input('Enter your budget (in Lakhs)', min_value=2.5, max_value=100.0, step=0.1)
    fuel_type = st.selectbox('Preferred fuel type', ('Petrol', 'Diesel', 'CNG'))
    transmission_type = st.selectbox('Preferred transmission type', ('Manual', 'Automatic'))
    car_age = st.slider('Maximum age of the car (years)', min_value=0, max_value=20)
    car_type = st.selectbox('Preferred car type', ('SUV', 'Sedan', 'Hatchback', 'Convertible', 'Coupe', 'Wagon', 'Van', 'Jeep'))
    preferred_brand = st.text_input('Preferred car brand (optional)')
    min_mileage = st.number_input('Minimum mileage (km/l)', min_value=0, max_value=50, step=1)
    
    if st.button("Recommend Cars"):
        recommendations = get_car_recommendations(budget, fuel_type, transmission_type, car_age, car_type, preferred_brand, min_mileage)
        st.markdown("## Recommended Cars:")
        st.write(recommendations)

def get_car_tips():
    # Generate prompt for Gemini AI
    prompt = f"Imagine You are a Car Expert, provide the User with one tip on buying or selling of used cars."
    response = genai.GenerativeModel("models/gemini-1.5-pro").generate_content(prompt)
    return response.text

def get_car_details(brand, model):
    # Generate prompt for Gemini AI
    prompt = f"Get details for the car brand: {brand} and model: {model}."
    response = genai.GenerativeModel("models/gemini-1.5-pro").generate_content(prompt)
    return response.text

def compare_cars(car1_details, car2_details):
    # Generate prompt for Gemini AI
    prompt = f"Compare the following two cars and also Highlight the Valuable features between them:\n\nCar 1: {car1_details}\n\nCar 2: {car2_details}."
    response = genai.GenerativeModel("models/gemini-1.5-pro").generate_content(prompt)
    return response.text

def get_car_recommendations(preferred_brand, budget, fuel_type, transmission_type, car_age, car_type, min_mileage):
    # Generate prompt for Gemini AI
    prompt = (
        f"You are a Car Expert, Recommend cars with the following criteria:\n"
        f"Preferred Brand: {preferred_brand}\n"
        f"Budget: {budget} lakhs\n"
        f"Fuel Type: {fuel_type}\n"
        f"Transmission: {transmission_type}\n"
        f"Max Age: {car_age} years\n"
        f"Car Type: {car_type}\n" 
        f"Minimum Mileage: {min_mileage} km/l\n"
    )
    response = genai.GenerativeModel("models/gemini-1.5-pro").generate_content(prompt)
    return response.text

if __name__ == '__main__':
    main()
