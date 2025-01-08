import streamlit as st

def hypothesis_page_body():
    st.write("### Project Hypothesis")
    st.success(
        f"We suspect that a higher level of education and years of experience "
        f"both positively effect software engineers and their salary. \n"
        f"Job location is also another factor that can affect salary, "
        f"countries deemed as '1st world' tend to have higher salaries "
        f"on offer as opposed to others."
        )