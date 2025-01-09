import streamlit as st

def hypothesis_page_body():
    st.write("### Project Hypothesis and Validation")
    st.info(
        f"We suspect that a higher level of education and years of experience "
        f"both positively effect software engineers and their salary. \n"
        f"Job location is also another factor that can affect salary, "
        f"countries deemed as '1st world' tend to have higher salaries "
        f"on offer as opposed to others."
        )
    st.success(
        f"It was clear to see that years of experience in software engineering "
        f"exponentially increases an employees potential salary, and the '1st "
        f"World' Countries clearly fell into the higher salary bracket."
    )