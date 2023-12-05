# Titel für die Seite
import streamlit as st
st.write("# Hallo Welt 👋🏻")

import pandas as pd
import numpy as np
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)
