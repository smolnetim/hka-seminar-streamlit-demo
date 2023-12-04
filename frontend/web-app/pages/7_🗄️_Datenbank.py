import streamlit as st

st.set_page_config(page_title="Datenbank", page_icon="🗄️")

st.write('# 🗄️ Datenbank')
st.write('Diese Seite funktioniert nur in der Lokalen Docker Compose Umgebung mit der PostgreSQL Datenbank.')

# Verbinde zur Datenbank
conn = st.experimental_connection('demo_db', type='sql')

# Daten laden und anzeigen
df = conn.query('select * from dataset')
st.line_chart(df, x="created_at", y=["value1","value2"])