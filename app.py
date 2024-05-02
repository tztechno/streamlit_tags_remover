import streamlit as st

st.title('Tags Remover')

text_area_key = "input_text_area"
text = st.text_area("Input text", key=text_area_key)

def remover(text):
    # 改行を削除
    text = text.replace("\n", "")
    # タブを削除
    text = text.replace("\t", "")
    # 行頭・行末のスペースを削除
    text = text.strip()
    # 全てのスペースを削除
    text = "".join(text.split())
    return text

if st.button("Remove Tags"):
    text2 = remover(text)
    st.write(f"Result: {text2}")
