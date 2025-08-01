import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini AI
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("❌ Error: GOOGLE_API_KEY not found in .env file")
    print("Please create a .env file with your API key:")
    print("GOOGLE_API_KEY=your_api_key_here")
    exit(1)

genai.configure(api_key=api_key)

# List available models
print("🔍 Available models:")
try:
    for m in genai.list_models():
        print(f"  - {m.name}")
        print(f"    Supported methods: {m.supported_generation_methods}")
    print("\n✅ API key is working!")
except Exception as e:
    print(f"❌ Error: {e}")
    print("Please check your API key and try again.") 