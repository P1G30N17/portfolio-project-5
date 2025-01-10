import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def shorten_categories(categories, cutoff):
    """
    Takes country value counts and checks to see if they are greater or less than the cutoff value,
    if less than, the country is added to a new category 'Other'.
    """
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map


def clean_experience(x):
    """
    Removes any string from the from the df.
    """
    if x == 'Less than 1 year':
        return 0.5
    return float(x)


def clean_education(x):
    """
    Simplifies the education levels into more globally recognized categories.
    """
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x:
        return 'Post grad'
    return 'Less than a Bachelor’s'


# To speed up load times
st.cache_data
def load_data():
    """
    Loads and cleans the dataset with the same parameters from the notebook.
    """
    df = pd.read_csv("/workspace/portfolio-project-5/inputs/developer_salary_survey/survey_results_public.csv")
    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedCompYearly"]]
    df = df.rename({"ConvertedCompYearly": "Salary"}, axis=1)
    df = df[df["Salary"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed, full-time"]
    df = df.drop("Employment", axis=1)

    country_map = shorten_categories(df.Country.value_counts(), 100)
    df['Country'] = df['Country'].map(country_map)
    df = df[df["Salary"] <= 250000]
    df = df[df["Salary"] >= 10000]

    df['YearsCodePro'] = df['YearsCodePro'].apply(clean_experience)
    df['EdLevel'] = df['EdLevel'].apply(clean_education)
    return df


df = load_data()

def explore_page_body():
    st.write("### The Global Software Engineer Job Market as of 2024")

    data = df["Country"].value_counts().drop("Other")

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", startangle=90)
    ax1.axis("equal")

    st.write("""#### Distribution of our Data by Country""")
    st.pyplot(fig1)
    st.info(
        f"As stated in the summary we have removed the Other Countries category as it "
        f"makes up 15.9% of Software Engineer Jobs distribution but this should be "
        f"ignored as it is an amalgamation of the remaining 164 countries that did not "
        f"meet the dataset requirement of each country having over 100 entries. \n"
        f"In context to our business model requirements we can clearly see that the "
        f"top three countries with most software engineers are 'United States of "
        f"America', 'Germany' and 'United Kingdom of Great Britain and Northern "
        f"Ireland'. So theoretically these countries should have the best job "
        f"prospects for a new software engineer."
    )

    st.write("""#### Average Salary in $USD by Country for Software Engineers""")
    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)
    st.info(
        f"Here we see the average salary for Software Engineers by Country, but it "
        f"should be noted that extreme salary outliers were excluded from the study "
        f"and model, so as to not skew the data but rather give a general inquiry "
        f"into what the majority of software engineers would earn per annum. \n"
        f"From the graph we can clearly see that the best salary on offer would be "
        f"from America', however 'Australia', 'Canada', 'Denmark', 'Israel', "
        f"'Switzerland', and 'United Kingdom of Great Britain and Northern "
        f"Ireland' all offer salaries averaging above $85000 per annum, making "
        f"these 7 countries great prospects for a job in softwawre engineering."
    )

    st.write("""#### Average Salary in $USD by Years of Experience for Software Engineers""")
    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)
    st.info(
        f"Here we see that years of coding experience has an exponential effect "
        f"on salary growth up to around 13 years, at which point the growth at "
        f"which salary increases begins to decay, but doesn't become negative. \n"
        f"From 32 years of experience and onwards the growth of salaries becomes "
        f"more sporadic. However it still sits comfortably above $100000 per annum "
        f"bar one outlier of 47 years of experience."
    )

    st.write("""#### Conclusion""")
    st.success(
        f"With the following information at hand one could quite easily make an "
        f"assumption as to the best long term future and job opportunities for a "
        f"potential new software engineer into the industry. However one would have "
        f"to apply there own living factors to the summary and make their choice that "
        f"best suits them, things like 'Nationality', 'Family', Housing Costs', "
        f"'Work Visas', etc. would all play vital factors in attracting or detracting "
        f"from a new software engineer entering the job market in their chosen country. \n"
        f"So in summary for our business case, the client has access to a British "
        f"and South African Nationality, giving us a clear 'Best' option for them, that "
        f"being, that if they so chose, starting a career in Software Engineering in "
        f"Great Britain or Northern Ireland will offer an ample job market and decent "
        f"salary along with good salary growth over the course of their career, meaning "
        f"they can comfortably provide for their family going forward."
    )
