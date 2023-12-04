import streamlit as st
import numpy as np

st.set_page_config(page_title="Navigation", page_icon="🧭")

tab1, tab2 = st.tabs(["📈 Graph", "🗃 Daten"])
data = np.random.randn(10, 1)

tab1.subheader("Ein Tab mit einem Graphen")
tab1.line_chart(data)

tab2.subheader("Ein Tab mit einer Tabelle")
tab2.write(data)