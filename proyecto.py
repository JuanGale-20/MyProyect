inventario = []
controlador = 0

while controlador != 4:

    print("\nBienvenido a nuestra tienda virtual")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadística")
    print("4. Salir")

    try:
        controlador = int(input("Ingrese la opción: "))
    except:
        print("Error: debe ingresar un número válido")
        

    if controlador == 1:
        nombre_producto = input("Ingrese el nombre del producto: ")

        # Validar precio
        precio = ""
        while precio == "":
            try:
                precio = float(input("Ingrese el precio: "))
            except:
                print("Error: valor inválido")
                precio = ""

        # Validar cantidad
        cantidad = ""
        while cantidad == "":
            try:
                cantidad = int(input("Ingrese la cantidad: "))
            except:
                print("Error: valor inválido")
                cantidad = ""

        inventario.append({
            "nombre": nombre_producto,
            "precio": precio,
            "cantidad": cantidad
        })

        print("Producto agregado ")

    elif controlador == 2:
        print("Inventario:")

        if len(inventario) == 0:
            print("No hay productos registrados")
        else:
            for producto in inventario:
                total = producto["precio"] * producto["cantidad"]
                print(f"{producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']} | Total: {total}")

    elif controlador == 3:
        total_general = 0

        for producto in inventario:
            total_general += producto["precio"] * producto["cantidad"]

        print(f"Total del inventario: {total_general}")

    elif controlador == 4:
        print(f"{producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']} | Total: {total}")
        print("Saliendo del programa...")

    else:
        print("Opción inválida")