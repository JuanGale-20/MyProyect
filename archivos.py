import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    "Guarda el inventario en CSV."

    if not inventario:
        print("No hay datos para guardar.")
        return

    if not ruta.lower().endswith(".csv"):
        print("Error: Solo se permiten archivos .csv")
        return

    try:
        with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)

            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])

            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        print("Archivo guardado correctamente.")

    except:
        print("Error al guardar el archivo.")


def cargar_csv(ruta):
    "Carga productos desde CSV."

    if not ruta.lower().endswith(".csv"):
        print("Error: Solo se pueden cargar archivos .csv")
        return []

    inventario = []

    try:
        with open(ruta, mode="r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)

            try:
                header = next(reader)
            except:
                print("Archivo vacío.")
                return []

            if header != ["nombre", "precio", "cantidad"]:
                print("Encabezado incorrecto.")
                return []

            for fila in reader:
                try:
                    nombre = fila[0].strip()
                    precio = float(fila[1])
                    cantidad = int(fila[2])

                    if precio < 0 or cantidad < 0:
                        print("Fila con valores negativos ignorada.")
                    else:
                        inventario.append({
                            "nombre": nombre,
                            "precio": precio,
                            "cantidad": cantidad
                        })

                except:
                    print("Fila inválida ignorada.")

        print("Archivo cargado correctamente.")
        return inventario

    except:
        print("Error al cargar el archivo.")
        return []