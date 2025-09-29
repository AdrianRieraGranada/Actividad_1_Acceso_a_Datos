CONVERSACIÓN CON COPILOT 

Pregunta: "si quiero que me cree en un directorio en especifico?"

Respuesta: def crear_archivo_reserva(nombre_archivo, directorio="."):
    ruta_completa = os.path.join(directorio, nombre_archivo)
    os.makedirs(directorio, exist_ok=True)  # Crea el directorio si no existe
    with open(ruta_completa, "w") as archivo:
        archivo.write("")  # Crear un archivo vacío
    print(f"Archivo '{nombre_archivo}' creado exitosamente en '{directorio}'.")

directorio_destino = "Act1"
crear_archivo_reserva("reservas.txt", directorio_destino)


-Autocompletado en esta línea: contenido = archivo.readlines()


Pregunta: "como acceder al número de palabra en específico en cada línea"

Respuesta: "palabras = linea.strip().split(',')  # Divide la línea en palabras usando la coma como delimitador
            if len(palabras) > 0:
                numero_asiento = palabras[0].strip()  # Obtiene el número de asiento (primera palabra)
                nombre_pasajero = palabras[1].strip() if len(palabras) > 1 else ""  # Obtiene el nombre del pasajero (segunda palabra)
                clase = palabras[2].strip() if len(palabras) > 2 else ""  # Obtiene la clase (tercera palabra)

                print(f"Número de Asiento: {numero_asiento}, Nombre: {nombre_pasajero}, Clase: {clase}")"


Pregunta: ^^^^ TypeError: 'str' object cannot be interpreted as an integer

Respuesta: El error TypeError: 'str' object cannot be interpreted as an integer ocurría en la línea:with open(directorio,f"{destino}.txt", "a") as archivo_destino:
    Solución:ruta_destino = os.path.join(directorio, f"{destino}.txt")
    with open(ruta_destino, "a") as archivo_destino:



Pregunta: "Ahora, para las líneas que no son válidas, necesito registrarlas en un archivo registro_errores.log. Cada línea debe incluir la fecha y hora actual del incidente, la línea con error y una descripción. Cómo añado la fecha y hora a la función de logging?"

Respuesta: "Necesitarás importar la librería datetime y crear una nueva función registrar_error. La función usará datetime.now() y strftime() para el formato de hora."