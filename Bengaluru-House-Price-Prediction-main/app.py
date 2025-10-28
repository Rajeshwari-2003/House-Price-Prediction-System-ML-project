
import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os



import os
import pickle
import streamlit as st  # make sure you import streamlit

# Find the absolute path to the model file
model_path = os.path.join(os.path.dirname(__file__), "random_forest_house_price_model.pkl")

# Load the model safely
try:
    with open(model_path, "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("❌ Model file not found! Please make sure 'random_forest_house_price_model.pkl' is in the same folder as app.py.")
    st.stop()  # Stop the app from running further
    

dataset = pickle.load(open('Bengaluru-House-Price-Prediction-main/dataset.pkl', 'rb'))


locations = dataset['location'].unique()

st.title("Bangalore House Price Prediction")

location = st.selectbox('Location', locations)
total_sqft = st.number_input('Total Square Foot', min_value=0.0, value=1000.0)
col1, col2 = st.columns(2)
with col1:
    bath = st.number_input('Number of Bathrooms', min_value=1, max_value=10, value=2)
with col2:
    bhk = st.number_input('Number of Bedrooms (BHK)', min_value=1, max_value=10, value=2)
    availability=st.selectbox('Availability',['Ready to move','Under construction'])

if st.button('Predict'):
    input_data = pd.DataFrame([[location, total_sqft, bath, bhk, availability]], 
                              columns=['location', 'total_sqft', 'bath', 'BHK', 'availability'])
    prediction = model.predict(input_data)[0]
    st.write(f"The predicted price is {prediction:.2f} lakhs")

