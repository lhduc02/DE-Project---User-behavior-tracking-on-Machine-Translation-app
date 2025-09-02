# Code giao diện Machine Translation với Streamlit
import streamlit as st
from translation import machine_translation
import time

# Thiết kế giao diện Streamlit
st.title("AI Speech & Text Assistant")


# Danh sách ngôn ngữ hỗ trợ
languages = [
    "English", "French", "German", "Spanish", "Italian", "Portuguese", "Dutch", "Russian"
]

# Sidebar
with st.sidebar:
    st.title("📌 Menu")
    choice = st.radio("Chọn chức năng:", ["🔤 Translation", "✅ Spell Check", "📄 Text Summary"])


# Xử lý logic
if choice == "🔤 Translation":
    st.write("Chức năng dịch ngôn ngữ.")
    a1, a2 = st.columns(2)
    b1, b2, b3, b4, b5, b6 = st.columns(6)
    # Chọn ngôn ngữ nguồn và đích
    with a1:
        language_source = st.selectbox("Select source language:", languages, index=0)
        input_content = st.text_area("Enter text to translate:", "", height=200)

    with a2:
        language_destination = st.selectbox("Select target language:", languages, index=1)


    with b1:
        if st.button("Voice"):
            pass

    with b3:
        if st.button("Translate"):
            pass
            start_time = time.time()
            if input_content.strip():
                output_content = machine_translation(language_source, language_destination, input_content)
                with a2:
                    st.text_area("Translated text:", output_content, height=200)
            else:
                st.warning("Please enter text to translate.")
            end_time = time.time()
            print("Time run:", end_time - start_time)

    with b6:
        if st.button("Listen"):
            pass



elif choice == "✅ Spell Check":
    st.write("Kiểm tra chính tả.")






elif choice == "📄 Text Summary":
    st.write("Tóm tắt văn bản.")







