import streamlit as st
from streamlit_lottie import st_lottie
import requests
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def load_lottie_url(url: str):
    """Fetches a Lottie animation from a URL."""
    try:
        r = requests.get(url)
        r.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
        return r.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error loading Lottie animation: {e}")
        return None

def get_car_recommendations(preferred_brand, budget, fuel_type, transmission_type, car_age, car_type, min_mileage):
    """
    Generates car recommendations using Gemini AI based on user preferences.
    """
    try:
        # Generate prompt for Gemini AI
        prompt = (
            f"You are a Car Expert, with high expertise in Indian Car market and sales. Recommend cars with the following criteria:\n"
            f"Preferred Brand: {preferred_brand}\n"
            f"Budget: {budget} lakhs\n"
            f"Fuel Type: {fuel_type}\n"
            f"Transmission: {transmission_type}\n"
            f"Max Age: {car_age} years\n"
            f"Car Type: {car_type}\n" 
            f"Minimum Mileage: {min_mileage} km/l\n"
        )
        response = genai.GenerativeModel("models/gemini-2.5-flash").generate_content(prompt)
        return response.text
    except Exception as e:
        if "quota" in str(e).lower() or "429" in str(e):
            return f"""🚗 **Car Recommendations** - Rate Limit Reached

⚠️ **API Rate Limit Reached** - Here are some general recommendations:

**Budget:** {budget} lakhs
**Fuel Type:** {fuel_type}
**Transmission:** {transmission_type}
**Car Type:** {car_type}

💡 **Popular Options in Your Range:**
- **{fuel_type} cars under {budget} lakhs:**
  - Maruti Swift (if budget allows)
  - Hyundai i10/i20
  - Tata Tiago
  - Renault Kwid

🔍 **Where to Look:**
- CarDekho, CarWale for detailed comparisons
- OLX, Quikr for used car listings
- Official brand websites for specifications

🔄 **Try again in a few minutes** when the rate limit resets."""
        else:
            return f"❌ Error getting recommendations: {str(e)[:100]}..."

def car_recommendation_system():
    """Main function for the Streamlit car recommendation app."""
    st.title("Car Recommendation System")
    st.markdown("Enter your preferences to get a list of recommended cars.")

    # Load and display Lottie animation
    lottie_recommend = load_lottie_url("https://lottie.host/1516b4ba-ba1a-498c-86e7-0f621597ebb6/QUwETgTJDM.json")
    if lottie_recommend:
        st_lottie(lottie_recommend, height=300, key="search_animation")
    
    # User preference inputs
    st.subheader("Enter Your Preferences")
    preferred_brand = st.text_input('Preferred car brand (optional)')
    budget = st.number_input('Enter your budget (in Lakhs)', min_value=2.5, max_value=100.0, step=0.1)
    fuel_type = st.selectbox('Preferred fuel type', ('Petrol', 'Diesel', 'CNG'))
    transmission_type = st.selectbox('Preferred transmission type', ('Manual', 'Automatic'))
    car_age = st.slider('Maximum age of the car (years)', min_value=0, max_value=20)
    car_type = st.selectbox('Preferred car type', ('SUV', 'Sedan', 'Hatchback', 'Convertible', 'Coupe', 'Wagon', 'Van', 'Jeep'))
    min_mileage = st.number_input('Minimum mileage (km/l)', min_value=0, max_value=50, step=1)
    
    if st.button("Recommend Cars"):
        # Corrected function call: ensuring arguments are in the right order
        recommendations = get_car_recommendations(preferred_brand, budget, fuel_type, transmission_type, car_age, car_type, min_mileage)
        
        st.markdown("## Recommended Cars:")
        st.write(recommendations)

# Run the app
if __name__ == "__main__":
    car_recommendation_system()
