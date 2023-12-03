import streamlit as st
import os

# st.secrets hat Zugriff auf alles
st.write("DB Benutzername:", st.secrets["db_username"])
st.write("DB Passwort:", st.secrets["db_password"])
st.write("Dinge, die ich mag:", st.secrets["grouped_variables"]["things_i_like"])

# Root-Level Variablen können ebenfalls abgefragt weren:
st.write(
    "Benutzername überschrieben:",
    os.environ["db_username"] == st.secrets["db_username"],
)