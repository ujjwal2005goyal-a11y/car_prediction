import streamlit as st
import pickle
import pandas as pd

# Load model + columns
model = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

st.title("🚗 Car Price Prediction")

st.write("Fill details below:")

# Inputs
present_price = st.number_input("Present Price (Lakhs)", 0.0, 50.0)
kms_driven = st.number_input("KMs Driven", 0, 500000)
owner = st.selectbox("Owner", [0, 1, 2, 3])
car_age = st.slider("Car Age", 0, 20)

fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

# Create input dataframe
input_dict = {
    "Present_Price": present_price,
    "Kms_Driven": kms_driven,
    "Owner": owner,
    "Car_Age": car_age,
    "Fuel_Type_Diesel": 1 if fuel_type == "Diesel" else 0,
    "Fuel_Type_Petrol": 1 if fuel_type == "Petrol" else 0,
    "Seller_Type_Individual": 1 if seller_type == "Individual" else 0,
    "Transmission_Manual": 1 if transmission == "Manual" else 0
}

input_df = pd.DataFrame([input_dict])

# Ensure same column order
input_df = input_df.reindex(columns=columns, fill_value=0)

# Prediction
if st.button("Predict Price"):
    prediction = model.predict(input_df)
    st.success(f"💰 Estimated Price: ₹ {round(prediction[0], 2)} Lakhs")