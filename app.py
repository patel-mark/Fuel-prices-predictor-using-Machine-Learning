import pickle
import streamlit as st
import requests
from PIL import Image
from sklearn.preprocessing import StandardScaler

# Load the model and scaler
with open('voting_regressor_model.pkl', 'rb') as file:
    loaded_model, loaded_scaler = pickle.load(file)

# Define the predict function
def predict_super_petrol(mean_exchange_rate, crude_oil_prices_usd_per_barrel, crude_oil_prices_kes_per_litre):
    # Load the model and scaler
    with open('voting_regressor_model.pkl', 'rb') as file:
        loaded_model, loaded_scaler = pickle.load(file)

    # Scale the input features using the loaded scaler
    input_features = [[mean_exchange_rate,crude_oil_prices_usd_per_barrel, crude_oil_prices_kes_per_litre]]
    input_features_scaled = loaded_scaler.transform(input_features)

    # Make the prediction using the loaded model
    predicted_super_petrol = loaded_model.predict(input_features_scaled)

    return predicted_super_petrol[0]


# Create the Streamlit app
#title
st.markdown("<h1 style='text-align: center; color: darkturquoise;'>Predictive Pricing Model for the Kenyan Fuel Market</h1>", unsafe_allow_html=True)

#pump image
image_url = "https://images.squarespace-cdn.com/content/v1/5acf87facc8fedbe1a9c205b/1523632453714-FACRKR4F8SRQD400SQRG/Lexo+Energy+petrol+fuel+station+Kenya+technology+3.jpg"

st.markdown(
    f'<img src="{image_url}" style="height: 300px; width: 100%;">',
    unsafe_allow_html=True,
)

#About the project
st.markdown("""
   Extreme fluctuations and inconsistencies in fuel prices in Kenya for the past five years have raised eyebrows among consumers. 
   
   In this project, I take a look at the trends and patterns in fuel pricing to come up with a machine-learning model that will aid in predicting future prices. 
   
   Using fuel data from 2010 to 2023, I analyzed trends and patterns and then created a visual to drive insights from the data using Excel.
    
   I created a machine learning model that takes in three input parameters: 
   1. Average mean exchange rate.
   2. Average crude oil price in USD per barrel. 
   3. Average crude oil price in Kenyan shillings per liter. 
        
   By using these inputs, this model will be able to predict future fuel prices and in particular Super petrol. 
   
   This project aims to create a more transparent fuel pricing system for consumers and all stakeholders that can help inform their future decisions creating a fair and stable fuel market.
""")

#Excell visualization chart.
st.markdown("<h3 style='text-align: center; color: darkturquoise'>Analysis of Oil Price Trends and Economic Impact in Kenya (2010 - 2023)</h3>", unsafe_allow_html=True)

image2=image_url="https://raw.githubusercontent.com/patel-mark/Fuel-prices-predictor-using-Machine-Learning/main/viz%20p.webp"
st.markdown(
    f'<img src="{image2}" alt="Your Image Caption" style="height: 100%; width: 100%;">',
    unsafe_allow_html=True,
)

#model title
st.markdown("<h3 style='text-align: center; color: darkturquoise'>Super Petrol machine learning Price Predictor</h3>", unsafe_allow_html=True)

# Add contact information
st.sidebar.title("Mark Patel")
st.sidebar.write("Data Scientist")
st.sidebar.write("You can reach me at:")
st.sidebar.subheader("patelmarkjohn@gmail.com")
st.sidebar.subheader("[LinkedIn](https://www.linkedin.com/in/mark-patel-In-Data001)")
st.sidebar.subheader("[GitHub](https://github.com/patel-mark)")

#Skills
st.sidebar.header("Skills")
st.sidebar.write("Here are some of my top skills:")
st.sidebar.write("- Machine learning")
st.sidebar.write("- Data analysis and visualization")
st.sidebar.write("- Python programming")
st.sidebar.write("- SQL")
st.sidebar.write("- Feature Engineering & Feature Selection")


mean_exchange_rate_input = st.number_input('Enter Mean Exchange Rate')
crude_oil_prices_usd_per_barrel_input=st.number_input('Enter Crude Oil Price in USD ($/Barrel)')
crude_oil_prices_kes_per_litre_input = st.number_input('Enter Crude Oil Price  in Shillings (KES/Litre)')

if st.button('Predict'):
    predicted_super_petrol_value = predict_super_petrol(mean_exchange_rate_input, crude_oil_prices_usd_per_barrel_input,crude_oil_prices_kes_per_litre_input)
    st.success(f'Predicted Super Petrol (KES/Litre): {predicted_super_petrol_value:.2f}')
