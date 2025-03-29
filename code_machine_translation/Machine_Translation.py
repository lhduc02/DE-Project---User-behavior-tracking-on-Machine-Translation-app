# Code giao diện Machine Translation với Streamlit
import streamlit as st
from translation import machine_translation
import time
import os
import asyncio


os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())


# Danh sách ngôn ngữ hỗ trợ
languages = [
    "English", "French", "German", "Spanish", "Italian", "Portuguese", "Dutch", "Russian"
]

# Thiết kế giao diện Streamlit
st.title("Translation App")

c1, c2 = st.columns(2)
# Chọn ngôn ngữ nguồn và đích
with c1:
    language_source = st.selectbox("Select source language:", languages, index=0)
    input_content = st.text_area("Enter text to translate:", "", height=200)

with c2:
    language_destination = st.selectbox("Select target language:", languages, index=1)

if st.button("Translate"):
    start_time = time.time()
    if input_content.strip():
        output_content = machine_translation(language_source, language_destination, input_content)
        with c2:
            st.text_area("Translated text:", output_content, height=200)
    else:
        st.warning("Please enter text to translate.")
    end_time = time.time()
    print("Time run:", end_time - start_time)

