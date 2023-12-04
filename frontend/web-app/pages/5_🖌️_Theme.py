import streamlit as st

st.set_page_config(page_title="Theme", page_icon="🖌️")

'''
# Theme 🖌️
Diese App wurde in der **config.toml** angepasst.
'''

code = '''[theme]
primaryColor="#3b8e77"
backgroundColor="white"
secondaryBackgroundColor="#F0F2F6"
textColor="#193b34"
font="monospace"'''
st.code(code, language='toml')

st.button("Primärfarbe", type="primary")
st.button("Sekundärfarbe", type="secondary")