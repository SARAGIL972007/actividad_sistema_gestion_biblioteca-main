from data.biblioteca import libros, categorias

from utils.operaciones import (
    mostrar_disponibles,
    buscar_por_paginas,
    contar_libros,
    promedio_paginas,
    agregar_categoria
)

continuar = "s"

while continuar == "s":
    print("\n=== BIBLIOTECA ===")
    print("1. Ver libros disponibles")
    print("2. Buscar libros cortos (menos de 400 páginas)")
    print("3. Ver estadísticas")
    print("4. Agregar categoría")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        mostrar_disponibles(libros)

    elif opcion == "2":
        buscar_por_paginas(libros, 400)

    elif opcion == "3":
        cantidad = contar_libros(libros)
        promedio = promedio_paginas(libros)

        print(f"Cantidad total de libros: {cantidad}")
        print(f"Promedio de páginas: {promedio:.2f}")

    elif opcion == "4":
        nueva_categoria = input(
            "Escribe la nueva categoría: "
        ).strip()

        if nueva_categoria:
            agregar_categoria(categorias, nueva_categoria)
            print("Categorías actuales:", categorias)
        else:
            print("La categoría no puede estar vacía.")

    elif opcion == "5":
        print("¡Gracias por utilizar la biblioteca!")
        continuar = "n"

    else:
        print("Opción no válida. Elige un número del 1 al 5.")
   
