import streamlit as st
from home import home_page
from predict import car_price_prediction
from compare import car_comparison_tool
from recommend import car_recommendation_system

# Page configuration
st.set_page_config(page_title="Used Car Web App", layout="wide")

# Page selector
pages = {
    "Home": home_page,
    "Predict Used Car Prices": car_price_prediction,
    "Compare Cars": car_comparison_tool,
    "Get Car Recommendations": car_recommendation_system
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Display the selected page
pages[selection]()
