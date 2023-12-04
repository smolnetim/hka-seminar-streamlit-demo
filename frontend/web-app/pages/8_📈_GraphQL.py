import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="GraphQL", page_icon="📈")

st.write('# 📈 Graphql')
st.write('Diese Seite funktioniert nur in der Lokalen Docker Compose Umgebung mit dem Hasura Backend.')

# GraphQL Query
query = """
query {
    dataset {
        createdAt
        value1
        value2
    }
}
"""

# Lade Daten
result = requests.post('http://172.17.0.1:8083/v1/graphql', json={'query': query})
data = result.json()["data"]["dataset"]

# Transformiere Daten und zeige sie an
df = pd.DataFrame(data)
df['createdAt'] = pd.to_datetime(df['createdAt'])
st.line_chart(df, x="createdAt", y=["value1","value2"])