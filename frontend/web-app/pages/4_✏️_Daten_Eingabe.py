import streamlit as st
import pandas as pd
import random

# Prüfen, ob 'dataframe' bereits im Session State existiert
if 'dataframe' not in st.session_state:
    st.session_state['dataframe'] = pd.DataFrame({"Zahl": []})

with st.form("mein_formular"):
   st.write("Mein Formular")
   number_val = st.number_input("Gib eine Zahl ein", value=random.randint(0, 100))

   submitted = st.form_submit_button("Submit")
   if submitted:
        new_row = pd.DataFrame({"Zahl": [number_val]})
        st.session_state['dataframe'] = pd.concat([st.session_state['dataframe'], new_row], ignore_index=True)

st.dataframe(st.session_state['dataframe'])
