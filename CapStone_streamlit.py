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
قد فكرت في يوم في القنوات اللي بتحقق أعلى نسب مشاهدة في السعودية؟ من اللي ورا نجاحها؟ كم مصدر دخلهم؟

يوتيوب ما صار مجرد منصة ترفيهية؛ اليوم هو المكان اللي يجمع كل شيء: الضحك اللي يبهجك، الدراما اللي تأخذك لعوالمها، التعليم اللي يثري معرفتك، وحتى القصص اللي تعيشها وكأنها واقع.

صنّاع المحتوى مو بس أشخاص خلف الكاميرا. هم أصحاب رؤية وأفكار تحولت إلى نجاحات تلهم الملايين. أفكارهم صارت جزءًا من حياتنا اليومية، تعلّمنا، تضحكنا، وتخلينا نفكر
</div>
""", unsafe_allow_html=True)
df
