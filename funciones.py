from gestor_datos import guardar_datos, validar_valoracion

def añadir_elemento(coleccion):
    print("\n--- Añadir Elemento ---")
    titulo = input("Título: ").strip()
    if not titulo:
        print("El título es obligatorio.")
        return

    tipo = input("Tipo (Libro/Película/Música): ").strip()
    autor = input("Autor/Director/Artista: ").strip()
    genero = input("Género: ").strip()
    
    val_input = input("Valoración (0.0 - 10.0): ")
    valoracion = validar_valoracion(val_input)
    
    if valoracion is None:
        print("Valoración inválida. Se asignará 0.0000")
        valoracion = 0.0000

    elemento = {
        "titulo": titulo,
        "tipo": tipo,
        "autor": autor,
        "genero": genero,
        "valoracion": valoracion
    }
    
    coleccion.append(elemento)
    guardar_datos(coleccion)
    print("Elemento añadido.")

def listar_elementos(coleccion):
    print("\n--- Colección ---")
    if not coleccion:
        print("La colección está vacía.")
        return

    header = f"{'Título':<25} | {'Tipo':<12} | {'Autor':<20} | {'Val.'}"
    print(header)
    print("-" * len(header))
    
    for el in coleccion:
        print(f"{el['titulo']:<25} | {el['tipo']:<12} | {el['autor']:<20} | {el['valoracion']:.4f}")

def buscar_elemento(coleccion):
    print("\n--- Buscar ---")
    criterio = input("Término de búsqueda: ").lower().strip()
    resultados = [el for el in coleccion if criterio in el['titulo'].lower() or criterio in el['autor'].lower()]
    
    if resultados:
        for el in resultados:
            print(f"- {el['titulo']} ({el['tipo']}) - {el['valoracion']:.4f}")
    else:
        print("Sin coincidencias.")

def editar_elemento(coleccion):
    titulo_buscar = input("\nTítulo a editar: ").strip()
    for el in coleccion:
        if el['titulo'].lower() == titulo_buscar.lower():
            el['titulo'] = input(f"Nuevo título [{el['titulo']}]: ") or el['titulo']
            nueva_val = input(f"Nueva valoración [{el['valoracion']}]: ")
            if nueva_val:
                val_valida = validar_valoracion(nueva_val)
                if val_valida is not None:
                    el['valoracion'] = val_valida
            guardar_datos(coleccion)
            print("Actualizado.")
            return
    print("No encontrado.")

def eliminar_elemento(coleccion):
    titulo = input("\nTítulo a eliminar: ").strip()
    original = len(coleccion)
    coleccion[:] = [el for el in coleccion if el['titulo'].lower() != titulo.lower()]
    if len(coleccion) < original:
        guardar_datos(coleccion)
        print("Eliminado.")
    else:
        print("No encontrado.")

