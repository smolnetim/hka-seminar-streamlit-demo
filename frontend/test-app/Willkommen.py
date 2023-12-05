# Titel für die Seite
import streamlit as st
st.write("# Hallo Welt 👋🏻")

# Dataset als Tabelle ausgeben
import seaborn as sns
df = sns.load_dataset('mpg')
st.dataframe(df)

# Als Graph ausgeben
import plotly.express as px
fig = px.scatter(df, x='horsepower', y='mpg', color='origin')
st.plotly_chart(fig)
