import streamlit as st
import pickle
import numpy as np 

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def load_predict_page():
    st.title("Software Engineer Salary Predictor")
    st.write("""## Please enter your desired software engineer credentials to make a salary prediction""")
