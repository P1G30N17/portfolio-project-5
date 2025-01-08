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


# @st.cache_data
def load_data():
    """
    Loads and cleans the dataset with the same parameters from the notebook.
    """
    df = pd.read_csv("inputs/developer_salary_survey/survey_results_public.csv")
    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedCompYearly"]]
    df = df.rename({"ConvertedCompYearly": "Salary"}, axis=1)
    df = df[df["Salary"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed, full-time"]
    df = df.drop("Employment", axis=1)

    country_map = shorten_categories(df.Country.value_counts(), 400)
    df['Country'] = df['Country'].map(country_map)
    df = df[df["Salary"] <= 250000]
    df = df[df["Salary"] >= 10000]

    df['YearsCodePro'] = df['YearsCodePro'].apply(clean_experience)
    df['EdLevel'] = df['EdLevel'].apply(clean_education)
    return df


df = load_data()

def explore_page_body():
    st.write("### The Global Software Engineer Job Market as of 2024")

    data = df["Country"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", startangle=90)
    ax1.axis("equal")

    st.write("""#### Distribution of our Data by Country""")
    st.pyplot(fig1)

    st.write("""#### Average Salary in $USD by Country for Software Engineers""")
    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write("""#### Average Salary in $USD by Years of Experience for Software Engineers""")
    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)
