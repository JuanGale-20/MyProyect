def agregar_producto(inventario, nombre, precio, cantidad):
    "Agrega un producto al inventario."

    if nombre.strip() == "":
        print("Error: El nombre no puede estar vacío.")
        return

    if precio < 0:
        print("Error: El precio no puede ser negativo.")
        return

    if cantidad < 0:
        print("Error: La cantidad no puede ser negativa.")
        return

    inventario.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })

    print("Producto agregado correctamente.")


def mostrar_inventario(inventario):
    "Muestra el inventario completo"

    if not inventario:
        print("\n--- Error: El inventario está vacío ---")
        return

    print("\n--- INVENTARIO ---")
    for p in inventario:
        print(f"{p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")


def buscar_producto(inventario, nombre):
    "Busca un producto por nombre."

    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            print(p)
            return

    print("Producto no encontrado.")


def actualizar_producto(inventario, nombre, nuevo_precio="", nueva_cantidad=""):

    producto = None

    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            producto = p

    if producto is None:
        print("Producto no encontrado.")
        return

    if nuevo_precio != "":
        if nuevo_precio < 0:
            print("Error: El precio no puede ser negativo.")
            return
        producto["precio"] = nuevo_precio

    if nueva_cantidad != "":
        if nueva_cantidad < 0:
            print("Error: La cantidad no puede ser negativa.")
            return
        producto["cantidad"] = nueva_cantidad

    print("Producto actualizado correctamente.")


def eliminar_producto(inventario, nombre):
    "Elimina un producto."

    producto = None

    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            producto = p

    if producto is None:
        print("Producto no encontrado.")
        return

    inventario.remove(producto)
    print("Producto eliminado correctamente.")


def calcular_estadisticas(inventario):
    "Calcula estadísticas del inventario."

    if not inventario:
        print("Inventario vacío.")
        return

    unidades_totales = 0
    valor_total = 0

    p_mas_caro = inventario[0]
    p_mayor_stock = inventario[0]

    for producto in inventario:
        unidades_totales += producto['cantidad']
        valor_total += producto['precio'] * producto['cantidad']

        if producto['precio'] > p_mas_caro['precio']:
            p_mas_caro = producto

        if producto['cantidad'] > p_mayor_stock['cantidad']:
            p_mayor_stock = producto

    print("\n--- ESTADÍSTICAS ---")
    print(f"Unidades totales: {unidades_totales}")
    print(f"Valor total: {valor_total}")
    print(f"Producto más caro: {p_mas_caro['nombre']}")
    print(f"Mayor stock: {p_mayor_stock['nombre']}")