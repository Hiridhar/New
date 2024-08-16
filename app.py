import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load the dataset
@st.cache
def load_data(uploaded_file):
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        return data
    else:
        return None

# Main app function
def main():
    st.title("Comprehensive Data Analysis App")

    # File uploader
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    
    # Load the data
    data = load_data(uploaded_file)
    
    if data is not None:
        # Data Preview
        st.write("## Data Preview")
        st.dataframe(data.head())

        # Dataset Information
        st.write("## Dataset Information")
        buffer = io.StringIO()
        data.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)

        # Summary Statistics
        st.write("## Summary Statistics")
        st.write(data.describe())

        # Missing Values
        st.write("## Missing Values")
        missing_values = data.isnull().sum()
        st.write(missing_values)

        # Data Types
        st.write("## Data Types")
        st.write(data.dtypes)

        # Unique Values
        st.write("## Unique Values per Column")
        unique_values = data.nunique()
        st.write(unique_values)

        # Value Counts for Categorical Columns
        st.write("## Value Counts for Categorical Columns")
        categorical_columns = data.select_dtypes(include=['object', 'category']).columns
        for col in categorical_columns:
            st.write(f"### {col}")
            st.write(data[col].value_counts())

        # Correlation Heatmap
        if st.checkbox("Show Correlation Heatmap"):
            st.write("### Correlation Heatmap")
            plt.figure(figsize=(10, 6))
            sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt='.2f')
            st.pyplot(plt)

        # Pairplot
        if st.checkbox("Show Pairplot"):
            st.write("### Pairplot")
            sns.pairplot(data)
            st.pyplot(plt)
       
        
    else:
        st.write("Please upload a CSV file to proceed.")

if __name__ == "__main__":
    main()
