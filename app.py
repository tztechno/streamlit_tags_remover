import streamlit as st

st.title('Tags Remover')

text_area_key = "input_text_area"
text = st.text_area("Input", key=text_area_key)

col1, col2, col3, col4 = st.columns(4)

with col1:
    remove_newlines = st.checkbox("Newlines")
with col2:
    remove_tabs = st.checkbox("Tabs")
with col3:
    remove_leading_trailing_spaces = st.checkbox("Lead/Trail Spaces")
with col4:
    remove_all_spaces = st.checkbox("All Spaces")

def remover(text):
    if remove_newlines:
        text = text.replace("\n", "")
    if remove_tabs:
        text = text.replace("\t", "")
    if remove_leading_trailing_spaces:
        text = text.strip()
    if remove_all_spaces:
        text = "".join(text.split())
    return text

if st.button("Remove"):
    result = remover(text)
    st.text_area("Result", value=result)
