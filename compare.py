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
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def car_comparison_tool():
    st.title("Car Comparison Tool")

    lottie_compare = load_lottie_url("https://lottie.host/e48cfccc-34c1-48fe-9fd4-dc550093cf27/rqB1OfW4dS.json")
    st_lottie(lottie_compare, height=300, key="search_animation")
    
    # Your existing car comparison code
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

def get_car_details(brand, model): 
    try:
        prompt = f"Get details for the car brand: {brand} and model: {model}, the region is India-specific unless the model and brand is not released in india." 
        response = genai.GenerativeModel("models/gemini-2.5-flash").generate_content(prompt) 
        return response.text
    except Exception as e:
        if "quota" in str(e).lower() or "429" in str(e):
            # Provide helpful fallback information
            return f"""📋 **{brand} {model}** - Basic Information
            
⚠️ **API Rate Limit Reached** - Here's what I can tell you:

**Brand:** {brand}
**Model:** {model}

💡 **Tips:**
- Check the official {brand} website for detailed specifications
- Visit car review sites like CarDekho, Autocar India
- Compare prices on platforms like OLX, CarWale
- Consider fuel efficiency, maintenance costs, and resale value

🔄 **Try again in a few minutes** when the rate limit resets."""
        else:
            return f"❌ Error getting car details: {str(e)[:100]}..." 

  

def compare_cars(car1_details, car2_details): 
    try:
        prompt = f"Compare the following two cars and also Highlight the Valuable features between them:\n\nCar 1: {car1_details}\n\nCar 2: {car2_details}." 
        response = genai.GenerativeModel("models/gemini-1.5-flash").generate_content(prompt) 
        return response.text
    except Exception as e:
        if "quota" in str(e).lower() or "429" in str(e):
            return f"⚠️ Rate limit exceeded. Please wait a moment and try again. (Error: {str(e)[:100]}...)"
        else:
            return f"❌ Error comparing cars: {str(e)[:100]}..." 