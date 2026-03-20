## 📦 Sistema Pro de Inventario con Persistencia (CSV)
---
Este proyecto es una solución modular en Python que permite la gestión completa de productos (CRUD), el análisis de estadísticas de negocio y la persistencia de datos mediante archivos CSV. Se enfoca en el uso avanzado de colecciones (listas, diccionarios, tuplas), programación modular y manejo robusto de excepciones.
---
## 🎯 Objetivos de la Historia de Usuario
---
Persistencia de Datos: Guardar y cargar el inventario desde archivos externos para conservar la información entre sesiones.
Arquitectura Modular: Organizar el código en módulos especializados (app.py, servicios.py, archivos.py).
Análisis de Negocio: Generar métricas automáticas sobre el valor y volumen del inventario.
Robustez: Implementar validaciones críticas para prevenir cierres inesperados por datos corruptos o entradas inválidas.
---
## 📝 Descripción de Tareas (Tasks)
---
🔹 Task 1: Arquitectura y Flujo
Diseño del diagrama de flujo integral que abarca desde el menú principal hasta los subflujos de persistencia (Guardado/Carga con validación).
---
🔹 Task 2: Estructura de Datos y CRUD Modular
Uso de una lista de diccionarios para representar productos: {"nombre": str, "precio": float, "cantidad": int}.
Creación del módulo servicios.py con funciones documentadas (Docstrings) para:
agregar_producto(), mostrar_inventario(), buscar_producto(), actualizar_producto() y eliminar_producto().
---
🔹 Task 3: Motor de Estadísticas
Implementación de calcular_estadisticas() para obtener:
Unidades totales y valor total del inventario.
Identificación del producto más caro y el de mayor stock.
Opcional: Uso de funciones lambda para el cálculo de subtotales.
---
🔹 Task 4: Persistencia de Salida (Guardar CSV)
Desarrollo de guardar_csv() en el módulo archivos.py.
Validación de inventario vacío y manejo de errores de permisos de escritura mediante try/except.
---
🔹 Task 5: Persistencia de Entrada (Cargar CSV)
Implementación de cargar_csv() con reglas estrictas:
Validación de encabezados y tipos de datos numéricos no negativos.
Gestión de errores: Conteo de filas inválidas omitidas sin interrumpir el programa.
Lógica de Fusión: Opción de sobrescribir el inventario actual o fusionar datos existentes por nombre de producto.
---
🔹 Task 6: Interfaz de Usuario y Experiencia (UX)
Menú principal interactivo con 9 opciones.
Ciclo de vida infinito (while) hasta que el usuario decida salir.
Validación exhaustiva de todas las entradas del usuario para garantizar la estabilidad del sistema.
---
✅ Criterios de Aceptación
💾 Persistencia y Datos
---
Generación de archivos CSV con formato estándar: nombre,precio,cantidad.
Capacidad de recuperación de datos con reporte de errores en archivos corruptos.
Uso correcto de listas de diccionarios y modularización en múltiples archivos.
---
## 📊 Análisis e Interfaz
Cálculo preciso de métricas de valor y stock.
Menú funcional (1-9) con mensajes claros para éxito, error e inventario vacío.
---
## 🛠️ Calidad de Código
---
Uso de Docstrings y comentarios técnicos.
Manejo profesional de excepciones (FileNotFoundError, ValueError, etc.).
Entrega de documentación visual (Diagrama de flujo).
---
## 🚀 Stack Tecnológico
---
Lenguaje: Python 3.x
Módulos Core: csv, os, sys
Paradigma: Programación Modular
---
