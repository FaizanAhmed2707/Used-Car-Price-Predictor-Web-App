# Test if each library is correctly installed

try:
    import seaborn as sns
    print("Seaborn is installed successfully.")
except ImportError:
    print("Seaborn is not installed.")

try:
    import sklearn
    print("scikit-learn (sklearn) is installed successfully.")
except ImportError:
    print("scikit-learn (sklearn) is not installed.")

try:
    import xgboost
    print("XGBoost is installed successfully.")
except ImportError:
    print("XGBoost is not installed.")

try:
    import joblib
    print("Joblib is installed successfully.")
except ImportError:
    print("Joblib is not installed.")

try:
    import tkinter
    print("Tkinter is installed successfully.")
except ImportError:
    print("Tkinter is not installed.")
