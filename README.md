# 🚗 Used Car Price Prediction Web App

A comprehensive Streamlit web application for predicting used car prices, comparing cars, and getting personalized car recommendations using machine learning and AI.

## ✨ Features

- **🎯 Car Price Prediction**: Predict the market value of used cars using a trained machine learning model
- **🔍 Car Comparison Tool**: Compare different car models side-by-side with AI-powered insights
- **💡 Car Recommendation System**: Get personalized car recommendations based on your preferences and budget
- **🎨 Beautiful UI**: Modern, responsive interface with animations and intuitive design

## 🛠️ Technologies Used

- **Frontend**: Streamlit
- **Machine Learning**: Scikit-learn, XGBoost
- **AI Integration**: Google Gemini AI
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly, Seaborn
- **Animations**: Lottie

## 📋 Prerequisites

- Python 3.8 or higher
- Google Gemini AI API key (for comparison and recommendation features)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd car-price-prediction
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root and add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## 🎯 Usage

1. **Run the application**
   ```bash
   streamlit run main.py
   ```

2. **Open your browser**
   Navigate to `http://localhost:8501`

3. **Explore the features**:
   - **Home**: Overview of the application
   - **Predict Used Car Prices**: Input car details to get price predictions
   - **Compare Cars**: Compare two different car models
   - **Get Car Recommendations**: Get personalized car suggestions

## 📊 Model Information

The car price prediction model is trained on a dataset of used car listings with features including:
- Present Price
- Kilometers Driven
- Fuel Type
- Seller Type
- Transmission
- Number of Owners
- Car Age

## 📁 Project Structure

```
├── main.py                 # Main Streamlit application
├── home.py                 # Home page component
├── predict.py              # Car price prediction functionality
├── compare.py              # Car comparison tool
├── recommend.py            # Car recommendation system
├── car_data_new.csv        # Dataset
├── car_price_predictor.pkl # Trained model
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
└── README.md              # Project documentation
```

## 🔧 Configuration

### Environment Variables
- `GOOGLE_API_KEY`: Your Google Gemini AI API key for advanced features

### Model Files
- `car_price_predictor.pkl`: Pre-trained machine learning model
- `car_data_new.csv`: Training dataset

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 🙏 Acknowledgments

- Dataset: Used car price dataset
- Streamlit: For the web framework
- Google Gemini AI: For AI-powered features
- Lottie: For beautiful animations

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Note**: Make sure to keep your API keys secure and never commit them to version control. 