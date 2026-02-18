from gestor_datos import cargar_datos
import funciones

def mostrar_menu():
    print("\n1. Añadir | 2. Listar | 3. Buscar | 4. Editar | 5. Eliminar | 6. Salir")
    return input("Opción: ")

def main():
    coleccion = cargar_datos()
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            funciones.añadir_elemento(coleccion)
        elif opcion == "2":
            funciones.listar_elementos(coleccion)
        elif opcion == "3":
            funciones.buscar_elemento(coleccion)
        elif opcion == "4":
            funciones.editar_elemento(coleccion)
        elif opcion == "5":
            funciones.eliminar_elemento(coleccion)
        elif opcion == "6":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()