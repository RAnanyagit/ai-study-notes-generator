import streamlit as st 
from ai_engine import summarize_text
text_input=st.text_area("Paste your content here:")
if st.button("Generate notes"):
    if text_input.strip():
        result=summarize_text(text_input)
        st.success(result)
    else:
        st.warning("Please enter some content to summarize")
