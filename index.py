import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
@st.cache
def load_data():
    return pd.read_csv("WomensClothingE-CommerceReviews.csv")  

# Main function to analyze and visualize the data
def main():
    st.title("Dataset Analysis")

    # Load the data
    data = load_data()

    # Display the first few rows of the dataset
    st.subheader("Sample Data")
    st.write(data.head())

    # Display basic statistics
    st.subheader("Basic Statistics")
    st.write(data.describe())

    # Visualize the distribution of ratings
    st.subheader("Distribution of Ratings")
    rating_counts = data['Rating'].value_counts()
    plt.bar(rating_counts.index, rating_counts.values)
    plt.xlabel('Rating')
    plt.ylabel('Count')
    st.pyplot()

    # Visualize the distribution of recommended vs. not recommended
    st.subheader("Distribution of Recommended vs. Not Recommended")
    recommendation_counts = data['Recommended IND'].value_counts()
    plt.bar(recommendation_counts.index, recommendation_counts.values)
    plt.xlabel('Recommended')
    plt.ylabel('Count')
    plt.xticks([0, 1], ['Not Recommended', 'Recommended'])
    st.pyplot()

    # Display a scatter plot of Age vs. Positive Feedback Count
    st.subheader("Scatter Plot of Age vs. Positive Feedback Count")
    plt.scatter(data['Age'], data['Positive Feedback Count'])
    plt.xlabel('Age')
    plt.ylabel('Positive Feedback Count')
    st.pyplot()

if __name__ == "__main__":
    main()
