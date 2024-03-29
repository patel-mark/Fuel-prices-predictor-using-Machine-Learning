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
st.title('Super Petrol Price Predictor Using Machine Lerning.')

image_url = "https://images.squarespace-cdn.com/content/v1/5acf87facc8fedbe1a9c205b/1523632453714-FACRKR4F8SRQD400SQRG/Lexo+Energy+petrol+fuel+station+Kenya+technology+3.jpg"
st.image(image_url, caption='Your Image Caption', use_column_width=True) 

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
