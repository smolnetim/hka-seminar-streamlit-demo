import streamlit as st

st.set_page_config(
    page_title="Willkommen",
    page_icon="👋",
)

st.write("# Willkommen in meiner App!👋")

st.markdown(
    """
		Streamlit ermöglicht es dir, Daten einfach und schnell zu visualisieren.
		Dieser Text wurde mit **Markdown** formatiert.

		### Keine Lust auf aufwendige Formatierung?
		- Streamlit kann auch automatisch Listen erstellen
		- Oder Tabellen
		- Oder Diagramme

		### Du willst mehr erfahren?
		> Es folgt etwas Werbung

		❗Folge dieser Arbeit, um mehr über Streamlit zu erfahren
	"""
)
