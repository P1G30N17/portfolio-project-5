import streamlit as st
from pages.multipage import MultiPage

# Load pages scripts
from pages.explore_page import explore_page_body
from pages.predict_salary_page import predict_salary_page_body
from pages.hypothesis_page import hypothesis_page_body
from pages.summary_page import summary_page_body

# Create an instance of the app
app = MultiPage(app_name="Software Engineer Job Market") 

# Add your app pages here using .add_page()
app.add_page("Project Summary", summary_page_body)
app.add_page("Predict Salary", predict_salary_page_body)
app.add_page("Explore the Global Job Market", explore_page_body)
app.add_page("Project Hypothesis", hypothesis_page_body)

# Run the app
app.run()
