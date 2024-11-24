import streamlit as st
import pandas as pd

# Raw URL of your CSV file from GitHub
df=pd.read_csv("youtube_data_eda_2.csv")# Replace with your actual file path

st.title("رائج")
st.write("""
<div style='text-align: right; direction: rtl;'>
    قد فكرت في يوم في القنوات اللي بتحقق أعلى نسب مشاهدة في السعودية؟ 
    من اللي ورا نجاحها؟ كم مصدر دخلهم؟ يوتيوب ما صار مجرد منصة ترفيهية؛ 
    اليوم هو المكان اللي يجمع كل شيء: الضحك، الدراما، التعليم، وحتى القصص اللي تعيشها كأنها واقع.
</div>
""", unsafe_allow_html=True)
df
