import streamlit as st
import pandas as pd

# Raw URL of your CSV file from GitHub
df=pd.read_csv("youtube_data_eda_2.csv")# Replace with your actual file path

st.markdown("""
<div style="text-align: center;">
    <h1>رائج</h1>
</div>
""", unsafe_allow_html=True)
st.write("""
<div style='text-align: right; direction: rtl;'>
قد فكرت في يوم في القنوات اللي بتحقق أعلى نسب مشاهدة في السعودية؟ من اللي ورا نجاحها؟ كم مصدر دخلهم؟ يوتيوب ما صار مجرد منصة ترفيهية؛ اليوم هو المكان اللي يجمع كل شيء: الضحك، الدراما، التعليم، وحتى القصص اللي تعيشها كأنها واقع. صنّاع المحتوى مو بس أشخاص خلف الكاميرا. هم أصحاب رؤية وأفكار تحولت إلى نجاحات.لكن يبقى السؤال: هل صناع المحتوى معظمهم من شبابنا ؟
</div>
""", unsafe_allow_html=True)
df
