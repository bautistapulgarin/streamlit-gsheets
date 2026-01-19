import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import json

# --------------------------
# 1️⃣ Título de la app
# --------------------------
st.title("Registro de datos en Google Sheets")

# --------------------------
# 2️⃣ Cargar credenciales desde el secreto
# --------------------------
google_json = st.secrets["GOOGLE_SHEETS_JSON"]
credentials_dict = json.loads(google_json)

# --------------------------
# 3️⃣ Conectarse a Google Sheets
# --------------------------
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, scope)
gc = gspread.authorize(credentials)

# --------------------------
# 4️⃣ Abrir hoja de Google Sheets
# --------------------------
SHEET_ID = "1HQEodjV1h0n0bleOAkfXToi_3VpGEWmuP7C9TTAa0rs"
sheet = gc.open_by_key(SHEET_ID).sheet1  # Primera hoja de la hoja de cálculo

# --------------------------
# 5️⃣ Formulario de registro
# --------------------------
st.header("Formulario de registro")

with st.form(key="registro_form"):
    nombre = st.text_input("Nombre")
    correo = st.text_input("Correo")
    comentario = st.text_area("Comentario")
    enviar = st.form_submit_button("Enviar")

# --------------------------
# 6️⃣ Guardar datos en Google Sheets
# --------------------------
if enviar:
    if nombre.strip() == "" or correo.strip() == "":
        st.warning("Por favor completa los campos obligatorios: Nombre y Correo.")
    else:
        nueva_fila = [nombre, correo, comentario]
        sheet.append_row(nueva_fila)
        st.success("Datos guardados correctamente en Google Sheets!")

# --------------------------
# 7️⃣ Mostrar los registros existentes
# --------------------------
st.header("Registros existentes")
data = sheet.get_all_records()
df = pd.DataFrame(data)
st.dataframe(df)
