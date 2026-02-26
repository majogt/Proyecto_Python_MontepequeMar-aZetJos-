from gestor_datos import cargar_datos, guardar_datos, guardar_elemento, actualizar_elemento, eliminar_elemento as eliminar_elemento_gestor, validar_valoracion, json


def seleccionar_tipo():
    print("\nSelecciona el tipo:")
    print("1. Libro")
    print("2. Película")
    print("3. Música")
    opcion = input("Opción (1-3): ").strip()
    tipos = {"1": "Libro", "2": "Película", "3": "Música"}
    if opcion in tipos:
        return tipos[opcion]
    return None

def añadir_elemento(coleccion):
    print("\n--- Añadir Elemento ---")
    tipo = seleccionar_tipo()
    if not tipo:
        return
    titulo = input("Título: ").strip()
    if not titulo:
        return
    autor = input("Autor/Director/Artista: ").strip()
    genero = input("Género: ").strip()
    val_input = input("Valoración (0.0 - 10.0): ")
    valoracion = validar_valoracion(val_input)
    if valoracion is None:
        valoracion = 0.0
    elemento = {
        "titulo": titulo,
        "tipo": tipo,
        "autor": autor,
        "genero": genero,
        "valoracion": valoracion
    }
    guardar_elemento(elemento)
    print(f"✓ {tipo} '{titulo}' añadido correctamente.")

def listar_elementos(coleccion):
    print("\n" + "="*50)
    print(f"{'MI COLECCIÓN CULTURAL':^50}")
    print("="*50)
    if not coleccion:
        print("La colección está vacía.")
        return
    categorias = ["Libro", "Película", "Música"]
    for cat in categorias:
        items = [el for el in coleccion if el.get('tipo') == cat]
        if items:
            print(f"\n▶ {cat.upper()}S ({len(items)})")
            print(f"{'-'*80}")
            header = f"{'Título':<25} | {'Autor/Artista':<20} | {'Género':<15} | {'Val.'}"
            print(header)
            print(f"{'-'*80}")
            for el in items:
                titulo = el.get('titulo', 'N/A')
                autor = el.get('autor', 'N/A')
                genero = el.get('genero', 'N/A')
                valoracion = el.get('valoracion', 0)
                print(f"{titulo:<25} | {autor:<20} | {genero:<15} | {valoracion:.2f}")
    otros = [el for el in coleccion if el.get('tipo') not in categorias]
    if otros:
        print(f"\n▶ OTROS ({len(otros)})")
        for el in otros:
            titulo = el.get('titulo', 'N/A')
            tipo_otro = el.get('tipo', 'N/A')
            valoracion = el.get('valoracion', 0)
            print(f"{titulo:<25} | {tipo_otro:<12} | {valoracion:.2f}")

def buscar_elemento(coleccion):
    print("\n--- Buscar Elemento ---")
    termino = input("Ingresa el título a buscar: ").strip().lower()
    if not termino:
        return
    resultados = [el for el in coleccion if termino in el.get('titulo', '').lower()]
    if resultados:
        print(f"\n✓ Se encontraron {len(resultados)} resultado(s):")
        print(f"{'-'*80}")
        for el in resultados:
            print(f"Título: {el.get('titulo', 'N/A')}")
            print(f"Tipo: {el.get('tipo', 'N/A')} | Autor: {el.get('autor', 'N/A')} | Género: {el.get('genero', 'N/A')} | Valoración: {el.get('valoracion', 0):.2f}")
            print(f"{'-'*80}")
    else:
        print("No se encontraron resultados.")

def editar_elemento(coleccion):
    print("\n--- Editar Elemento ---")
    tipo = seleccionar_tipo()
    if not tipo:
        return
    elementos_tipo = cargar_datos(tipo)
    if not elementos_tipo:
        print(f"No hay {tipo.lower()}s registrados.")
        return
    print(f"\n{tipo.upper()}S disponibles:")
    for i, el in enumerate(elementos_tipo, 1):
        print(f"{i}. {el.get('titulo', 'Sin título')}")
    try:
        opcion = int(input("Selecciona el número del elemento a editar: ")) - 1
        if 0 <= opcion < len(elementos_tipo):
            elemento = elementos_tipo[opcion].copy()
            titulo_original = elemento.get('titulo', '')
            print("\n¿Qué deseas editar? (Deja en blanco para no cambiar)")
            nuevo_titulo = input(f"Título [{elemento.get('titulo', '')}]: ").strip()
            nuevo_autor = input(f"Autor/Artista [{elemento.get('autor', '')}]: ").strip()
            nuevo_genero = input(f"Género [{elemento.get('genero', '')}]: ").strip()
            nueva_val = input(f"Valoración [{elemento.get('valoracion', 0):.2f}]: ").strip()
            elemento['titulo'] = nuevo_titulo if nuevo_titulo else elemento.get('titulo', '')
            elemento['autor'] = nuevo_autor if nuevo_autor else elemento.get('autor', '')
            elemento['genero'] = nuevo_genero if nuevo_genero else elemento.get('genero', '')
            if nueva_val:
                valoracion = validar_valoracion(nueva_val)
                if valoracion is not None:
                    elemento['valoracion'] = valoracion
            if actualizar_elemento(tipo, titulo_original, elemento):
                print("✓ Elemento actualizado correctamente.")
            else:
                print("✗ Error al actualizar el elemento.")
        else:
            print("Opción inválida.")
    except ValueError:
        print("Entrada inválida.")

def estadisticas_generales():
    coleccion = cargar_datos()
    total_elementos = len(coleccion)
    total_libros = sum(1 for el in coleccion if el.get('tipo') == 'Libro')
    total_peliculas = sum(1 for el in coleccion if el.get('tipo') == 'Película')
    total_musica = sum(1 for el in coleccion if el.get('tipo') == 'Musica')
    valoraciones = [el.get('valoracion', 0) for el in coleccion]
    promedio_valoraciones = sum(valoraciones) / len(valoraciones) if valoraciones else 0.0
    estadisticas = {
        "total": total_elementos,
        "libros": total_libros,
        "peliculas": total_peliculas,
        "musica": total_musica,
        "promedio_valoraciones": promedio_valoraciones
    }
    with open('estadisticas.json', 'w') as f:
        json.dump(estadisticas, f)

def eliminar_elemento(coleccion):
    print("\n--- Eliminar Elemento ---")
    tipo = seleccionar_tipo()
    if not tipo:
        return
    elementos_tipo = cargar_datos(tipo)
    if not elementos_tipo:
        print(f"No hay {tipo.lower()}s registrados.")
        return
    print(f"\n{tipo.upper()}S disponibles:")
    for i, el in enumerate(elementos_tipo, 1):
        print(f"{i}. {el.get('titulo', 'Sin título')}")
    try:
        opcion = int(input("Selecciona el número del elemento a eliminar: ")) - 1
        if 0 <= opcion < len(elementos_tipo):
            elemento = elementos_tipo[opcion]
            titulo_elemento = elemento.get('titulo', 'Sin título')
            confirmacion = input(f"¿Estás seguro de que deseas eliminar '{titulo_elemento}'? (s/n): ").strip().lower()
            if confirmacion == 's':
                if eliminar_elemento_gestor(tipo, titulo_elemento):
                    print("✓ Elemento eliminado correctamente.")
                else:
                    print("✗ Ocurrio un error al eliminar el elemento vuelva a intentar.")
            else:
                print("La eliminacion fue cancelada.")
        else:
            print("Opción inválida.")
    except ValueError:
        print("Entrada inválida.")
