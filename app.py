import streamlit as st
import json

# Cargar secreto
google_json = st.secrets["GOOGLE_SHEETS_JSON"]

# Reemplazar cualquier posible salto de línea mal interpretado
google_json = google_json.replace("\\n", "\n")

# Convertir a diccionario
credentials_dict = json.loads(google_json)

st.write("JSON cargado correctamente")
