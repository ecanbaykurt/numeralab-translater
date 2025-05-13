import streamlit as st
from numeralab_core.code_translater import translate_fortran_to_python

st.set_page_config(page_title="NumeraLab Code Translator", layout="wide")
st.title("🛠 NumeraLab: Fortran → Python Code Translator (MVP)")

input_code = st.text_area("Paste your Fortran code below:", height=400)
if st.button("Translate to Python"):
    translated_code = translate_fortran_to_python(input_code)
    st.write("### Translated Python Code:")
    st.code(translated_code, language='python')

    st.write("### AI Suggestion:")
    st.info("This is an early MVP translation. Please check array indexing (starts from 0 in Python), data structures (use NumPy), and loop adjustments. Mathematical functions may require numpy or scipy adjustments.")
