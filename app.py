import json

with open("tu_archivo.json") as f:
    data = json.load(f)

# Reemplazar saltos de línea en private_key
data['private_key'] = data['private_key'].replace('\n', '\\n')

# Guardar JSON listo para TOML
toml_ready = json.dumps(data)
print(toml_ready)
