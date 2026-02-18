
import json
import os

ARCHIVO_DATOS = "coleccion.json"

def cargar_datos():
    if not os.path.exists(ARCHIVO_DATOS):
        return []
    try:
        with open(ARCHIVO_DATOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def guardar_datos(coleccion):
    try:
        with open(ARCHIVO_DATOS, 'w', encoding='utf-8') as f:
            json.dump(coleccion, f, indent=4)
    except IOError as e:
        print(f"Error al guardar: {e}")

def validar_valoracion(entrada):
    try:
        valoracion = float(entrada)
        if 0.0 <= valoracion <= 10.0:
            return round(valoracion, 4)
        return None
    except ValueError:
        return None