from servicios import *
from archivos import *

inventario = []
controlador = 0

while controlador != 9:
    print("\n--- TIENDA ---")
    print("1. Agregar")
    print("2. Mostrar")
    print("3. Buscar")
    print("4. Actualizar")
    print("5. Eliminar")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")

    op = input("Opción: ")
    controlador = int(op)

    # AGREGAR
    if op == "1":
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        agregar_producto(inventario, nombre, precio, cantidad)

    # MOSTRAR
    elif op == "2":
        mostrar_inventario(inventario)

    # BUSCAR
    elif op == "3":
        nombre = input("Buscar: ")
        buscar_producto(inventario, nombre)

    # ACTUALIZAR
    elif op == "4":
        nombre = input("Nombre: ")
        precio = input("Nuevo precio: ")
        cantidad = input("Nueva cantidad: ")
        
        if precio != "":
            precio = float(precio)
        else:
            precio = ""

        if cantidad != "":
            cantidad = int(cantidad)
        else:
            cantidad = ""

        actualizar_producto(inventario, nombre, precio, cantidad)

    # ELIMINAR
    elif op == "5":
        nombre = input("Nombre: ")
        eliminar_producto(inventario, nombre)

    # ESTADÍSTICAS
    elif op == "6":
        calcular_estadisticas(inventario)

    # GUARDAR
    elif op == "7":
        ruta = input("Archivo: ")
        guardar_csv(inventario, ruta)

    # CARGAR
    elif op == "8":
        ruta = input("Archivo: ")
        inventario = cargar_csv(ruta)

    elif op == "9":
        print("Saliendo del programa...")

    else:
        print("Opción inválida")