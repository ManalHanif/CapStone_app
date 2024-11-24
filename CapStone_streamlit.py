import streamlit as st
import pandas as pd

# Raw URL of your CSV file from GitHub
csv_url = "https://github.com/ManalHanif/CapStone_app/blob/main/youtube_data_eda_2.csv"  # Replace with your actual file path

st.title("Display DataFrame from GitHub CSV")

# Read CSV file into a DataFrame
try:
    df = pd.read_csv(csv_url)
    st.write("DataFrame loaded successfully!")
    st.dataframe(df)
except Exception as e:
    st.error("An error occurred while loading the CSV file.")
    st.text(str(e))
