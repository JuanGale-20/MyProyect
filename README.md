## 🛒 Sistema de Inventario
---
## 📌 Descripción

Este proyecto consiste en un sistema de gestión de inventario desarrollado en Python. Permite administrar productos mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar), así como guardar y cargar información utilizando archivos CSV.
---
## ⚙️ Características principales

Agregar productos
Mostrar inventario
Buscar productos
Actualizar información
Eliminar productos
Calcular estadísticas
Guardar datos en archivos CSV
Cargar datos desde archivos CSV
Validaciones de entrada
Manejo de errores
---
## 🧱 Estructura del proyecto

El proyecto está organizado en módulos:

app.py → Maneja el menú principal
servicios.py → Contiene la lógica del CRUD y estadísticas
archivos.py → Gestiona archivos CSV
README.md → Documentación
---
## 📊 Estadísticas del inventario

El sistema calcula automáticamente:

Total de unidades disponibles
Valor total del inventario
Producto con mayor precio
Producto con mayor cantidad en stock
---
## 💾 Guardar CSV

Guarda el inventario en formato CSV
Incluye encabezados estándar
Verifica que el inventario no esté vacío
Maneja errores de escritura
---
## 📂 Cargar CSV

Permite cargar datos desde un archivo CSV
Valida el formato del archivo
Omite filas inválidas
Permite sobrescribir o fusionar el inventario

En caso de fusión:

Se suman cantidades si el producto ya existe
Se actualiza el precio si hay diferencias
---
## 🖥️ Menú principal


El sistema funciona con un menú interactivo que incluye:

Agregar producto
Mostrar inventario
Buscar producto
Actualizar producto
Eliminar producto
Ver estadísticas
Guardar CSV
Cargar CSV
Salir
---
## 🧠 Manejo de errores

El sistema controla errores como:

Entradas inválidas
Archivos inexistentes
Errores de lectura o escritura
Datos incorrectos en CSV

Esto evita que la aplicación se cierre inesperadamente.
---
## 🗺️ Diagrama de flujo
Aplicar conocimientos en:

Programación en Python
Estructuras de datos
Modularización
Manejo de archivos
Validación de datos
Manejo de excepciones
