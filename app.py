import pickle
import streamlit as st
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
st.title('Super Petrol Price Predictor')

mean_exchange_rate_input = st.number_input('Enter Mean Exchange Rate')
crude_oil_prices_usd_per_barrel_input=st.number_input('Enter Crude Oil Price in USD ($/Barrel)')
crude_oil_prices_kes_per_litre_input = st.number_input('Enter Crude Oil Price  in Shillings (KES/Litre)')

if st.button('Predict'):
    predicted_super_petrol_value = predict_super_petrol(mean_exchange_rate_input, crude_oil_prices_usd_per_barrel_input,crude_oil_prices_kes_per_litre_input)
    st.success(f'Predicted Super Petrol (KES/Litre): {predicted_super_petrol_value:.2f}')
