import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


@st.cache
def load_data():
    data = pd.read_csv('./data/ted.csv')
    return data


df = load_data()


def main():
    page = st.sidebar.selectbox(
        "Select a Page",
        [
            # Starting with just Homepage
            "Homepage",
            "Bar Plot"
        ]
    )

    # Show header
    if page == "Homepage":
        # st.header("Data Application")
        """
        # Building apps with Streamlit 
        Please select a page on the left 
        """
        #  Load in balloons prior this (of course)
        st.balloons()
        #  Show it as a table
        st.write(df)
    # Chosen pages
    elif page == "Bar Plot":
        bar_chart()


# Creating bar chart
def bar_chart():
    fig = plt.figure(figsize=(12, 5))
    plt.xticks(rotation=86)
    bar_data = df.sort_values(by="views", ascending=False)
    bar_data = bar_data.head(20)
    plt.ticklabel_format(style="plain")
    plt.xlabel("Titles")
    plt.ylabel("Views")
    plt.title("Ted Talk Titles and Views Plot")
    plt.bar(bar_data["title"], bar_data["views"])
    st.pyplot(fig)


if __name__ == "__main__":
    main()

