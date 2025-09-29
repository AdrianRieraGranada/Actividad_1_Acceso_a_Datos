import os

def crear_archivo_reserva(nombre_archivo, directorio="."):
    ruta_completa = os.path.join(directorio, nombre_archivo)
    os.makedirs(directorio, exist_ok=True)  
    with open(ruta_completa, "w") as archivo:
        archivo.write("")  
    print(f"Archivo '{nombre_archivo}' creado exitosamente en '{directorio}'.")

def escribir_reservas(nombre_archivo, directorio=".", reservas=[]):
    ruta_completa = os.path.join(directorio, nombre_archivo)
    with open(ruta_completa, "a") as archivo:
        for reserva in reservas:
            archivo.write(f"{reserva}\n")
    print("Se han escrito las reservas en el archivo.")

def leer_reservas(nombre_archivo, directorio="."):
    print("Listado de Reservas:")
    ruta_completa = os.path.join(directorio, nombre_archivo)
    with open(ruta_completa, "r") as archivo:
        contenido = archivo.readlines()
        pasajeros_totales=0
        pasajeros_bussiness=0
        for linea in contenido:
            pasajeros_totales+=1
            palabras = linea.strip().split(',')  # Divide la línea en palabras usando la coma como delimitador
            if len(palabras) > 0:
                numero_asiento = palabras[0].strip()  # Obtiene el número de asiento (primera palabra)
                nombre_pasajero = palabras[1].strip() if len(palabras) > 1 else ""  # Obtiene el nombre del pasajero (segunda palabra)
                clase = palabras[2].strip() if len(palabras) > 2 else ""  # Obtiene la clase (tercera palabra)

                print(f"Número de Asiento: {numero_asiento}, Nombre: {nombre_pasajero}, Clase: {clase}")
                if clase=="Business": 
                    pasajeros_bussiness+=1
        print("")
        print("Resumen:")
        print(f"Total de pasajeros: {pasajeros_totales}")
        print(f"Total de pasajeros en clase Business: {pasajeros_bussiness}")


reservas = [
    "12A, Juan Pérez, Economy",
    "14B, María López, Business",
    "21C, Carlos García, Economy",
]   



directorio_destino = "ArchivosReservas_parte1"

crear_archivo_reserva("reservas.txt", directorio_destino)
escribir_reservas("reservas.txt", directorio_destino, reservas)
print("")
leer_reservas("reservas.txt", directorio_destino)