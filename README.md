Car Price Prediction — Machine Learning Web App
A Machine Learning-powered web application that predicts the resale price of used cars based on key features like present price, kilometers driven, fuel type, seller type, transmission, and car age.

🌐 Live Demo
🔗 
https://carprediction-agajcbc3jjxqsl7y6ib9wx.streamlit.app/

📌 Table of Contents
About the Project
Features
Tech Stack
Dataset
Project Structure
How It Works
Installation & Setup
Screenshots
Model Performance
Future Improvements
Author
📖 About the Project
Buying or selling a used car? Determining the right price can be tricky. This project solves that problem by using Machine Learning to predict the fair market price of a used car.

The model is trained on a real-world dataset of 892 used car listings and deployed as an interactive Streamlit web application where users can input car details and get an instant price estimate.

✨ Features
🔮 Instant Price Prediction — Get estimated resale value in seconds
🧹 Automated Data Cleaning — Handles missing values, invalid entries, and formatting
🏗️ Feature Engineering — Derives meaningful features like Car Age
🎯 One-Hot Encoding — Properly handles categorical variables
🖥️ Interactive Web App — Clean, user-friendly Streamlit interface
💾 Persistent Model — Pre-trained model saved with Pickle for fast loading
🛠️ Tech Stack
Category	Technology
Language	Python 3.8+
ML Library	scikit-learn
Data Processing	Pandas, NumPy
Web Framework	Streamlit
Model Serialization	Pickle
Algorithm	Decision Tree Regressor
📊 Dataset
Property	Details
Source	Used Car Dataset (CSV)
Total Records	892 entries
Records after cleaning	816 entries
Features	Car_Name, Company, Year, Price, Kms_Driven, Fuel_Type
Features Used for Prediction:
Feature	Type	Description
Present_Price	Numerical	Current ex-showroom price (in Lakhs)
Kms_Driven	Numerical	Total kilometers driven
Owner	Numerical	Number of previous owners (0–3)
Car_Age	Numerical	Age of the car (engineered feature)
Fuel_Type	Categorical	Petrol / Diesel
Seller_Type	Categorical	Dealer / Individual
Transmission	Categorical	Manual / Automatic
📁 Project Structure

car_prediction-main/
│
├── app.py              # Streamlit web application
├── main.py             # Model training script
├── car_data.csv        # Raw dataset
├── model.pkl           # Trained ML model (serialized)
├── columns.pkl         # Feature column names (serialized)
└── README.md           # Project documentation
⚙️ How It Works

┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Raw CSV Data   │────▶│  Data Cleaning   │────▶│    Feature      │
│  (car_data.csv) │     │  & Preprocessing │     │   Engineering   │
└─────────────────┘     └──────────────────┘     └────────┬────────┘
                                                          │
                                                          ▼
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   Prediction    │◀────│  Trained Model   │◀────│  Train/Test     │
│   (Streamlit)   │     │  (model.pkl)     │     │  Split (80/20)  │
└─────────────────┘     └──────────────────┘     └─────────────────┘
Step-by-step:

Load & Clean Data — Remove invalid prices, clean kms, handle missing values
Feature Engineering — Create Car_Age from Year, drop irrelevant columns
Encoding — One-Hot Encode categorical variables (drop_first=True)
Train/Test Split — 80% training, 20% testing (random_state=42)
Train Model — Fit DecisionTreeRegressor on training data
Save Model — Serialize with Pickle (model.pkl + columns.pkl)
Deploy — Streamlit app loads model and predicts in real-time
🚀 Installation & Setup
Prerequisites
Python 3.8 or higher
pip (Python package manager)
Steps
bash

# 1. Clone the repository
git clone https://github.com/<your-username>/car_prediction.git
cd car_prediction
# 2. Install dependencies
pip install streamlit pandas scikit-learn
# 3. Train the model (optional — model.pkl is already included)
python main.py
# 4. Run the web app
streamlit run app.py
The app will open in your browser at http://localhost:8501

📸 Screenshots
📌 Add screenshots of your running app here

📈 Model Performance
Metric	Train	Test
R² Score	0.9986	0.1800
MAE	—	₹1,92,450
RMSE	—	₹6,77,135
⚠️ Note: The high train R² and low test R² indicate overfitting — a known characteristic of unpruned Decision Trees. See 
Future Improvements
 for planned fixes.

🔮 Future Improvements
 Replace Decision Tree with Random Forest or XGBoost for better generalization
 Add hyperparameter tuning (max_depth, min_samples_split) using GridSearchCV
 Implement k-fold cross-validation for more reliable evaluation
 Add feature importance visualization (bar chart)
 Deploy on Streamlit Cloud for public access
 Add Exploratory Data Analysis (EDA) page with charts
 Use joblib instead of pickle for model serialization
 Add input validation and error handling in the app
🤝 Contributing
Contributions are welcome! Feel free to:

Fork the repository
Create a feature branch (git checkout -b feature/improvement)
Commit your changes (git commit -m 'Add new feature')
Push to the branch (git push origin feature/improvement)
Open a Pull Request
👨‍💻 Author
Ujjwal Goyal

🔗 GitHub: 
github.com/your-username
🔗 LinkedIn: 
linkedin.com/in/your-profile
📧 Email: 
your.email@example.com
📄 License
This project is open source and available under the 
MIT Lice
