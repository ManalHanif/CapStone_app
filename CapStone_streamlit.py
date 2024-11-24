import streamlit as st
import pandas as pd

# Raw URL of your CSV file from GitHub
df=pd.read_csv("youtube_data_eda_2.csv")# Replace with your actual file path

st.title("Display DataFrame from GitHub CSV")
df
