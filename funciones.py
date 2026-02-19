from gestor_datos import guardar_datos, validar_valoracion

def añadir_elemento(coleccion):
    print("\n--- Añadir Elemento ---")
    titulo = input("Título: ").strip()
    if not titulo:
        print("El título es obligatorio.")
        return

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
    print("\n" + "="*50)
    print(f"{'MI COLECCIÓN CULTURAL':^50}")
    print("="*50)
    
    if not coleccion:
        print("La colección está vacía.")
        return

    categorias = ["Libro", "Película", "Música"]
    
    for cat in categorias:
        items = [el for el in coleccion if el['tipo'] == cat]
        
        if items:
            print(f"\n▶ {cat.upper()}S ({len(items)})")
            print(f"{'-'*75}")
            header = f"{'Título':<25} | {'Autor/Artista':<25} | {'Val.'}"
            print(header)
            print(f"{'-'*75}")
            
            for el in items:
                print(f"{el['titulo']:<25} | {el['autor']:<25} | {el['valoracion']:.4f}")
    
    otros = [el for el in coleccion if el['tipo'] not in categorias]
    if otros:
        print(f"\n▶ OTROS ({len(otros)})")
        for el in otros:
            print(f"{el['titulo']:<25} | {el['tipo']:<12} | {el['valoracion']:.4f}")
