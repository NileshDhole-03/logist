import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open("Logi.pkl", "rb"))

# Streamlit app title
st.title("Result Predition ")

# Input field for experience
age = st.text_input("Enter your age:")

# Prediction logic
if st.button("Predict"):
    if age:  # Check if input is not empty
        if age.replace('.', '', 1).isdigit():  # Validate numeric input (including decimals)
            age = float(age)
            prediction = model.predict([[age]])[0]
            if(prediction==1):
                st.success(f"Predicted Result: {prediction}")
            else:
                st.error(f"Predicted Result:{prediction}")
        else:
            st.error("Please enter a valid numeric value for age .")
    else:
        st.error("Input field cannot be empty.")
