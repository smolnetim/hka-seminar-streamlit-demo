import streamlit as st
import pandas as pd

st.set_page_config(page_title="Datenvisualisierung", page_icon="🪄")

dataframe = pd.DataFrame({
    'Spalte 1': [1, 2, 3, 4],
    'Spalte 2': [10, 20, 30, 40],
})

col1, col2 = st.columns(2)

with col1:
    st.write(dataframe)

with col2:
    st.dataframe(dataframe)