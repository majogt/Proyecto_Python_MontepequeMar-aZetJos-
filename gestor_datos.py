import json
import os

ARCHIVOS_DATOS = {
    "Libro": "libros.json",
    "Película": "peliculas.json",
    "Música": "musica.json"
}

def cargar_datos(tipo=None):
    if tipo is None:
        coleccion_completa = []
        for tipo_cat in ARCHIVOS_DATOS:
            coleccion_completa.extend(cargar_datos(tipo_cat))
        return coleccion_completa
    
    archivo = ARCHIVOS_DATOS.get(tipo)
    if not archivo or not os.path.exists(archivo):
        return []
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def guardar_datos(coleccion, tipo=None):
    if tipo is None:
        for tipo_cat in ARCHIVOS_DATOS:
            elementos_tipo = [el for el in coleccion if el.get('tipo') == tipo_cat]
            if elementos_tipo:
                guardar_datos(elementos_tipo, tipo_cat)
        return
    
    archivo = ARCHIVOS_DATOS.get(tipo)
    if not archivo:
        return
    try:
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(coleccion, f, indent=4, ensure_ascii=False)
    except IOError:
        pass

def guardar_elemento(elemento):
    tipo = elemento.get('tipo')
    archivo = ARCHIVOS_DATOS.get(tipo)
    if not archivo:
        return
    elementos = cargar_datos(tipo)
    elementos.append(elemento)
    try:
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(elementos, f, indent=4, ensure_ascii=False)
    except IOError:
        pass

def actualizar_elemento(tipo, titulo, elemento_actualizado):
    archivo = ARCHIVOS_DATOS.get(tipo)
    if not archivo:
        return False
    elementos = cargar_datos(tipo)
    for i, el in enumerate(elementos):
        if el.get('titulo') == titulo:
            elementos[i] = elemento_actualizado
            try:
                with open(archivo, 'w', encoding='utf-8') as f:
                    json.dump(elementos, f, indent=4, ensure_ascii=False)
                return True
            except IOError:
                return False
    return False

def eliminar_elemento(tipo, titulo):
    archivo = ARCHIVOS_DATOS.get(tipo)
    if not archivo:
        return False
    elementos = cargar_datos(tipo)
    elementos_filtrados = [el for el in elementos if el.get('titulo') != titulo]
    if len(elementos_filtrados) < len(elementos):
        try:
            with open(archivo, 'w', encoding='utf-8') as f:
                json.dump(elementos_filtrados, f, indent=4, ensure_ascii=False)
            return True
        except IOError:
            return False
    return False

def validar_valoracion(valoracion):
    try:
        val = float(valoracion)
        if 0.0 <= val <= 10.0:
            return val
    except ValueError:
        pass
    return None
