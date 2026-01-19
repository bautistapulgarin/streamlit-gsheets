import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import json

st.title("Registro de datos en Google Sheets")

# --------------------------
# 1️⃣ Cargar credenciales desde el secreto
# --------------------------
google_json = st.secrets["GOOGLE_SHEETS_JSON"]
credentials_dict = json.loads(google_json)

# --------------------------
# 2️⃣ Conectarse a Google Sheets
# --------------------------
# Definir alcance (scopes)
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

# Crear credenciales usando ServiceAccount
credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, scope)

# Conectar con Google Sheets
gc = gspread.authorize(credentials)

# --------------------------
# 3️⃣ Abrir hoja de Google Sheets
# --------------------------
# Reemplaza con tu ID de hoja de cálculo
SHEET_ID = "TU_ID_DE_HOJA_DE_GOOGLE"  # Ej: "1AbCdEfGhIjKlMnOpQrStUvWxYz1234567890"
sheet = gc.open_by_key(SHEET_ID).sheet1  # Usamos la primera hoja

# --------------------------
# 4️⃣ Formulario de registro
# --------------------------
st.header("Formulario de registro")

with st.form(key="registro_form"):
    nombre = st.text_input("Nombre")
    correo = st.text_input("Correo")
    comentario = st.text_area("Comentario")
    enviar = st.form_submit_button("Enviar")

# --------------------------
# 5️⃣ Guardar datos en Google Sheets
# --------------------------
if enviar:
    # Crear fila con datos
    nueva_fila = [nombre, correo, comentario]
    
    # Agregar al final de la hoja
    sheet.append_row(nueva_fila)
    
    st.success("Datos guardados correctamente en Google Sheets!")

# --------------------------
# 6️⃣ Mostrar los registros existentes
# --------------------------
st.header("Registros existentes")
data = sheet.get_all_records()  # Trae todos los datos
df = pd.DataFrame(data)
st.dataframe(df)
