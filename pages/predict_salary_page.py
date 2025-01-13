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

def predict_salary_page_body():
    st.write("### Software Engineer Salary Predictor")
    st.info("Please enter your desired software engineer credentials to make a salary prediction")

    countries = ( 
        "United States of America", 
        "Germany", 
        "United Kingdom of Great Britain and Northern Ireland", 
        "Ukraine", 
        "India", 
        "France", 
        "Canada", 
        "Brazil", 
        "Spain", 
        "Italy", 
        "Netherlands", 
        "Australia", 
        "Other"
    )

    education = (
        "Post grad", 
        "Master’s degree", 
        "Bachelor’s degree", 
        "Less than a Bachelor’s"
    )

    # Code Credit Patrick Loeber
    country = st.selectbox("Country of Job Location", countries)
    ed_level = st.selectbox("Highest Education Qualification", education)
    experience = st.slider("Years of Experience in Software Engineering/Developer Industry", 0, 50, 1)
    predict = st.button("Calculate Salary")
    if predict:
        # Using the same code from the notebook steps to take in user input and transform it using the label encoder
        X = np.array([[country, ed_level, experience]])
        X[:, 0] = le_country.transform(X[:, 0])
        X[:, 1] = le_education.fit_transform(X[:,1])
        X = X.astype(float) 
        # Predicting the user's salary
        salary = regressor.predict(X)
        st.subheader(f"Your predicted salary if you were to find work in {country} is ${salary[0]:.2f} per annum.")