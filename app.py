import streamlit as st
import json

# Cargar secreto
google_json = st.secrets["GOOGLE_SHEETS_JSON"]

# Convertir la cadena JSON en diccionario Python
credentials_dict = json.loads(google_json)

st.write("JSON cargado correctamente")
