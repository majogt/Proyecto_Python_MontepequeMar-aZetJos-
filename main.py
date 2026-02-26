from gestor_datos import cargar_datos
import funciones

def mostrar_menu():
    print("\n" + "="*50)
    print("GESTOR DE COLECCIÓN CULTURAL")
    print("="*50)
    print("1. Añadir elemento")
    print("2. Listar elementos")
    print("3. Buscar elemento")
    print("4. Editar elemento")
    print("5. Eliminar elemento")
    print("6. Estadísticas generales")
    print("7. Salir")
    print("="*50)
    return input("Opción: ").strip()

def main():
    while True:
        opcion = mostrar_menu()
        coleccion = cargar_datos() 
        
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
            funciones.estadisticas_generales()  
        elif opcion == "7":
            print("\n¡Hasta luego!")
            break
        else:
            print("✗ Opción no válida. Por favor intenta de nuevo.")

if __name__ == "__main__":
    main()
    
