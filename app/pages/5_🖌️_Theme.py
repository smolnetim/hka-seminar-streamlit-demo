import streamlit as st

'''
# Theme 🖌️
Diese App wurde in der **config.toml** angepasst.
'''

code = '''[theme]
primaryColor="#3b8e77"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#193b34"
font="monospace"'''
st.code(code, language='toml')

st.button("Primärfarbe", type="primary")
st.button("Sekundärfarbe", type="secondary")