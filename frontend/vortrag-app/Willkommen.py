import streamlit as st

st.write("# Hallo Welt 👋🏻")

import seaborn as sb
df = sb.load_dataset("mpg")
st.dataframe(df)

import plotly.express as px
fig = px.scatter(df, x="horsepower", y="mpg", color="origin")
st.write(fig)
