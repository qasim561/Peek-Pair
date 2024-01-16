# demand_predict.py
import pandas as pd
import streamlit as st


def predict_units_sold(model, total_price, base_price):
    features = pd.DataFrame([[total_price, base_price]], columns=["Total Price", "Base Price"])
    prediction = model.predict(features)
    return int(round(prediction[0]))

def show_demand_prediction():
    st.write("## Enter the Total-Price & Base-Price of the product:",unsafe_allow_html=True)
    st.markdown("---")

    content = ""
    return content
