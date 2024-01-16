import streamlit as st
import numpy as np
import joblib

# Load the saved model
model = joblib.load("model_1.sav")

def predict_sales(social_media, tv_ads, magazine, banners):
    features = np.array([[social_media, tv_ads, magazine, banners]])
    prediction = model.predict(features)
    return int(round(prediction[0]))

def show_sales_prediction():
    st.write("## Enter the Advertising Spend Values:")
    st.markdown("---")

    # Taking user input
    
    social_media = st.number_input("Social Media Spend", value=200.0, format='%f')
    
    tv_ads = st.number_input("TV Ads", value=50.0, format='%f')
    
    magazine = st.number_input("Magazine Spend", value=75.0, format='%f')
    
    banners = st.number_input("Banners Spend", value=150.0, format='%f')

    if st.button("Predict Sales"):
        predicted_sales = predict_sales(social_media, tv_ads, magazine, banners)
        st.markdown(f"## Predicted Sales: {predicted_sales}%")


        
