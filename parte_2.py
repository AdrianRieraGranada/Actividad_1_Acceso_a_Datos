import os

def crear_archivo_reserva(nombre_archivo, directorio="."):
    ruta_completa = os.path.join(directorio, nombre_archivo)
    os.makedirs(directorio, exist_ok=True)  
    # No se crea el archivo aquí, se creará solo si es necesario en leer_reservas

def escribir_reservas(nombre_archivo, directorio=".", reservas=[]):
    ruta_completa = os.path.join(directorio, nombre_archivo)
    # Leer las reservas existentes
    reservas_existentes = []
    if os.path.exists(ruta_completa):
        with open(ruta_completa, "r") as archivo:
            reservas_existentes = [linea.strip() for linea in archivo.readlines()]
    
    with open(ruta_completa, "a") as archivo:
        for reserva in reservas:
            if reserva not in reservas_existentes:
                archivo.write(f"{reserva}\n")



def leer_reservas(nombre_archivo, directorio="."):
    ruta_completa = os.path.join(directorio, nombre_archivo)
    with open(ruta_completa, "r") as archivo:
        contenido = archivo.readlines()

    destinos_totales=[]
    for linea in contenido:
        linea = linea.strip()  # Eliminar espacios en blanco al principio y al final
        if not linea:  # Verificar si la línea está vacía
            continue  # Saltar a la siguiente iteración si la línea está vacía
        
        palabras = linea.split(',')  # Divide la línea en palabras usando la coma como delimitador
        if len(palabras) > 0:
            destino = palabras[3].strip() if len(palabras) > 3 else ""  # Obtiene la clase (tercera palabra)
            destinos_totales.append(destino)

            # Escribimos la línea en el archivo correspondiente al destino
            ruta_destino = os.path.join(directorio, f"{destino}.txt")
            # Comprobamos si el archivo de destino existe
            if not os.path.exists(ruta_destino):
                # Si no existe, lo creamos y escribimos la reserva
                with open(ruta_destino, "w") as archivo_destino:
                    archivo_destino.write(f"{linea}\n")
            else:
                # Si existe, verificamos si la línea ya está en el archivo antes de agregarla
                with open(ruta_destino, "r") as archivo_destino:
                    contenido_destino = archivo_destino.readlines()
                linea_existe = False
                for linea_destino in contenido_destino:
                    if linea.strip() == linea_destino.strip():
                        linea_existe = True
                        break
                if not linea_existe:
                    with open(ruta_destino, "a") as archivo_destino:
                        archivo_destino.write(f"{linea}\n")
            

    destinos_totales=set(destinos_totales)  # Convertimos la lista a un conjunto para obtener destinos únicos
    # Recorremos los destinos únicos para mostrar sus archivos

    for destino in destinos_totales:
        ruta_destino = os.path.join(directorio, f"{destino}.txt")
        with open(ruta_destino, "r") as archivo_destino:
            contenido_destino = archivo_destino.readlines()
            print("")
            print(f"Creado el archivo para el destino {destino}")
            destino_total_pasajeros=0
            for linea in contenido_destino:
                destino_total_pasajeros+=1
            print(f"Total de pasajeros para {destino}: {destino_total_pasajeros}")

    print("")
    

reservas=[
    "12A, Juan Pérez, Economy, Madrid",
    "14B, María López, Business, París",
    "21C, Carlos García, Economy, Madrid",
    "05D, Ana Sánchez, Business, Londres",
    "19E, Luis Gómez, Economy, París",
    "08F, Sofía Vargas, Economy, Londres"
]

directorio_destino = "Act1"
#crear_archivo_reserva("reservas_maestro.txt", directorio_destino) #No se crea el archivo maestro
escribir_reservas("reservas_maestro.txt", directorio_destino, reservas)
print("")
leer_reservas("reservas_maestro.txt", directorio_destino)