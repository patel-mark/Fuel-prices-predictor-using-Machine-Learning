# Predictive Pricing Model for the Kenyan Fuel Market

## Business Problem: Developing a Predictive Pricing Model for the Kenyan Fuel Market
Fuel prices in Kenya are often subject to fluctuations and inconsistencies, raising concerns about potential manipulation and unfair pricing practices. Consumers and regulators require insights into these dynamics for better transparency and market regulation.

## Objective
The objective is to utilize a Kenyan fuel prices dataset to develop a robust predictive pricing model. The focus is on creating a model that can forecast fuel prices accurately and independently of any manipulation.


## Project Files

- **Fuel prices predictor using Machine Learning.ipynb:** Jupyter notebook containing the Python code and model development.
- **app.py:** Streamlit web application code for performing record linkage.
- **Fuel Prices in Kenya since 2010 - Sheet1.csv:** CSV file containing Fuel prices data from 2010 t0 2023.
- **Fuel Prices in Kenya since 2010 - Sheet1.xlsx:** Excel workbook containig data analysis and visualization of the fuel data.

## Libraries Used

- pandas
- numpy
- matplotlib.pyplot
- seaborn as sns
- sklearn
- pickle

## Project Structure

### 1. Data Cleaning
Data is loaded and column names renamed for easier interpretation.
Missing values are checked and three null values are dropped.
Column data types are checked with 'Price Commencement Date' being converted to datetime from object type.

### 2. Data Exploration
Checked column correlation and visualized it using a matrix heat map in seaborn.


### 3. Feature Engineering
Used Mean Absolute error to check feature importance.
Droped "Price Commencement Date", "Diesel (KES/Litre)", "Kerosene (KES/Litre)" and "Year" as i wasnt going to use them in building the machine learning model.

### 4. Model Building
I deployed the use of ensemble learning in building my model to come up with the best posible model.
Algorithms used were DecisionTreeRegressor, LinearRegression, KNeighborsRegressor and ensemble learning VotingRegressor.
Carried out cross validation on the data using standard scaler too before trainig the ML model.

### 4. Model Evaluation
I used "model.score" on the scaled features and seaborn to visualize the accurecy of each algorithm on the data and the results were as follows:
         Linear Regression Test set Accuracy: 0.946
         KNeighbors Regressor Test set Accuracy: 0.942
         Decision Tree Regressor Test set Accuracy: 0.961 
The Voting Regressor produced an accurecy of 0.962
I saved the trained Voting Regressor model using pickle.


### 8. Streamlit Web Application
The Streamlit app includes the following features:
- A title, project description section, excel data analysis dashboard picture and the model section.
- The model section labled "Super Petrol machine learning Price Predictor" has three entry section named:
         'Enter Mean Exchange Rate'
         'Enter Crude Oil Price in USD ($/Barrel)'
         'Enter Crude Oil Price  in Shillings (KES/Litre)'
- Upon entering those values, the user is reuired to click a button labeled 'Predict' for the model to predict the price of super petrol per the parameters provided.


