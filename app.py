import streamlit as st
import json

# Leer el secreto
google_json = st.secrets["GOOGLE_SHEETS_JSON"]
credentials_dict = json.loads(google_json)

