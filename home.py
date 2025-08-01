import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def home_page():
    st.markdown("""
        <style>
        .custom-title {
            font-size: 3em;
            color: gold;
            text-align: center;
            font-weight: bold;
            margin-top: 20px;
            margin-bottom: 30px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="custom-title">Welcome to the Used Car Web App</h1>', unsafe_allow_html=True)

    
    lottie_car = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_tfb3estd.json")
    st_lottie(lottie_car, height=300, key="car_animation")

    # Custom CSS for metric cards
    st.markdown("""
        <style>
        .card-container {
            display: flex;
            justify-content: space-around;
            margin-top: 50px;
        }
        .card {
            background-image: url('https://wallpapers.com/images/high/aesthetic-red-background-1920-x-1080-ywl7o7kzf4smivjg.webp');
            border-radius: 8px;
            padding: 20px;
            width: 30%;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
            transition: transform 0.3s ease;
        }
        .card:hover {
            transform: translateY(-10px);
            box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.2);
        }
        .card-title {
            font-style: bold;
            font-size: 2em;
            margin-bottom: 15px;
            text-align: center;
            color: gold;
        }
        .card-description {
            font-style: italic;
            font-size: 1em;
            margin-bottom: 15px;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

    # HTML for metric cards
    st.markdown("""
        <div class="card-container">
            <div class="card">
                <div class="card-title">Car Price Prediction</div>
                <div class="card-description">
                    Uncover the true value of your vehicle with our intelligent car price prediction tool. Simply input your car’s details, and let our advanced machine learning model estimate the best market price—fast, accurate, and reliable.
                </div>
            </div>
            <div class="card">
                <div class="card-title">Car Comparison Tool</div>
                <div class="card-description">
                    Navigate the road to your perfect ride with our car comparison tool. Effortlessly compare specs, features, and prices to find out which car stands out in a side-by-side showdown
                </div>
            </div>
            <div class="card">
                <div class="card-title">Car Recommendation System</div>
                <div class="card-description">
                    Find your dream car with just a few clicks. Our personalized recommendation system takes your preferences and budget into account to suggest the best matches tailored just for you.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
