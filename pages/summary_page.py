import streamlit as st

def summary_page_body():
    st.write("### Project Summary")
    st.info(
        f"**General Information**\n"
        f"The Software industry is a global booming market, it would only be fair to assume that jobs within this "
        f"market would be too. This project aims to give a brief insight into this growing market with an "
        f"investiagtion into the availability of Software Engineering jobs, their associated salary and which "
        f"countries have the most jobs (This is an assumption off the current number of people employed within "
        f"the field). \n\n"
        f"**Project Dataset** \n"
        f"The dataset used was taken from a survey of 65000 people done by [StackOverflow]"
        f"(https://survey.stackoverflow.co/) as of 2024, and gives an incredibly detailed list of variables all "
        f"pertaining to aspects of Software Engineers and their experiences within the current job market."
    )
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/P1G30N17/portfolio-project-5/blob/main/README.md).")
    

    st.success(
        f"The project has 3 business requirements: \n"
        f"* 1 - The client is interested in having a study to investigate the best location(Country with most jobs) "
        f"for a potential job in the software engineering market \n"
        f"* 2 - The client is interested in determining whether experience in the software engineering industry "
        f"affects potential salary \n"
        f"* 3 - The client wishes to be able to predict their potential salary based off of their qualification, "
        f"years of experience and where they would be able to live(Country)."
        )