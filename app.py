import streamlit as st
import numpy as np
import pickle

# Load the pre-trained model
with open('product_delivery_prediction.pkl', 'rb') as model_file:
    dtc = pickle.load(model_file)

# Set the title
st.title("Delivery Prediction App")

# Create input fields for user input
warehouse_block_mapping = {'A': 3, 'B': 4, 'C': 0, 'D': 1, 'F': 2}
mode_of_shipment_mapping = {'Ship': 0, 'Flight': 2, 'Road': 1}
product_importance_mapping = {'low': 1, 'medium': 2, 'high': 0}
gender_mapping = {'male': 0, 'female': 1}

warehouse_block = st.selectbox('Warehouse Block:', list(warehouse_block_mapping.keys()))
mode_of_shipment = st.selectbox('Mode of Shipment:', list(mode_of_shipment_mapping.keys()))
customer_care_calls = st.slider('Customer Care Calls:', min_value=0, max_value=10, value=4)
customer_rating = st.slider('Customer Rating:', min_value=1, max_value=5, value=2)
cost_of_the_product = st.slider('Cost of the Product:', min_value=0, max_value=500, value=177)
prior_purchases = st.slider('Prior Purchases:', min_value=0, max_value=10, value=3)
product_importance = st.selectbox('Product Importance:', list(product_importance_mapping.keys()))
gender = st.selectbox('Gender:', list(gender_mapping.keys()))
discount_offered = st.slider('Discount Offered:', min_value=0, max_value=100, value=44)
weight_in_gms = st.slider('Weight in grams:', min_value=0, max_value=2000, value=1233)

# Convert input data to NumPy array
input_array = np.array([[warehouse_block_mapping[warehouse_block],
                         mode_of_shipment_mapping[mode_of_shipment],
                         customer_care_calls, customer_rating, cost_of_the_product,
                         prior_purchases, product_importance_mapping[product_importance],
                         gender_mapping[gender], discount_offered, weight_in_gms]])

# Make a prediction
prediction = dtc.predict(input_array)

# Display the prediction result
if prediction[0] == 0:
    st.success("Product Delivered On Time")
else:
    st.error("Product Not Delivered On Time")
