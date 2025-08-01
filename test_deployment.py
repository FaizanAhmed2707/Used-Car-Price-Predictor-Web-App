#!/usr/bin/env python3
"""
Test file to verify all dependencies can be imported successfully.
This helps debug deployment issues on Streamlit Cloud.
"""

def test_imports():
    """Test importing all required packages."""
    try:
        import streamlit as st
        print("✅ streamlit imported successfully")
    except ImportError as e:
        print(f"❌ streamlit import failed: {e}")
        return False
    
    try:
        import pandas as pd
        print("✅ pandas imported successfully")
    except ImportError as e:
        print(f"❌ pandas import failed: {e}")
        return False
    
    try:
        import numpy as np
        print("✅ numpy imported successfully")
    except ImportError as e:
        print(f"❌ numpy import failed: {e}")
        return False
    
    try:
        import sklearn
        print("✅ scikit-learn imported successfully")
    except ImportError as e:
        print(f"❌ scikit-learn import failed: {e}")
        return False
    
    try:
        import xgboost as xgb
        print("✅ xgboost imported successfully")
    except ImportError as e:
        print(f"❌ xgboost import failed: {e}")
        return False
    
    try:
        import joblib
        print("✅ joblib imported successfully")
    except ImportError as e:
        print(f"❌ joblib import failed: {e}")
        return False
    
    try:
        from streamlit_lottie import st_lottie
        print("✅ streamlit-lottie imported successfully")
    except ImportError as e:
        print(f"❌ streamlit-lottie import failed: {e}")
        return False
    
    try:
        from streamlit_option_menu import option_menu
        print("✅ streamlit-option-menu imported successfully")
    except ImportError as e:
        print(f"❌ streamlit-option-menu import failed: {e}")
        return False
    
    try:
        import requests
        print("✅ requests imported successfully")
    except ImportError as e:
        print(f"❌ requests import failed: {e}")
        return False
    
    try:
        import google.generativeai as genai
        print("✅ google-generativeai imported successfully")
    except ImportError as e:
        print(f"❌ google-generativeai import failed: {e}")
        return False
    
    try:
        from dotenv import load_dotenv
        print("✅ python-dotenv imported successfully")
    except ImportError as e:
        print(f"❌ python-dotenv import failed: {e}")
        return False
    
    print("\n🎉 All imports successful!")
    return True

if __name__ == "__main__":
    test_imports() 