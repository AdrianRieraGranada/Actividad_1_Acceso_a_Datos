import os
from datetime import datetime

# --- CONFIGURACIÓN DE ARCHIVOS ---
ARCHIVO_MAESTRO_ERRORES = "reservas_maestro_con_errores.txt"
ARCHIVO_LOG_ERRORES = "registro_errores.log"
DIRECTORIO_DESTINO = "ArchivosReservas_parte3" 
NUM_CAMPOS_REQUERIDOS = 4  # (Seient, Nom, Classe, Destí)

# --- DATOS INICIALES (Con Errores para la prueba) ---
# Se recomienda mantener la estructura del ejercicio anterior (separado por comas y espacios)
reservas_con_errores = [
    "12A, Juan Pérez, Economy, Madrid",             # Válida (4 campos)
    "14B, María López, Business, París",            # Válida (4 campos)
    "21C, Carlos García, Economy",                  # ERROR: Falta Destino (3 campos)
    "05D, Ana Sánchez, Business, Londres",          # Válida (4 campos)
    "19E, Luis Gómez",                              # ERROR: Faltan Clase y Destino (2 campos)
    "08F, Sofía Vargas, Economy, Londres",          # Válida (4 campos)
    "",                                             # ERROR: Línea vacía (0 campos)
    "25G, Pedro Martínez, First, New York, Extra",  # ERROR: Campo extra (5 campos)
    "01A, Laura Díaz, Business, Milán"              # Válida (4 campos)
]

# --- FUNCIONES DE GESTIÓN DE ARCHIVOS ---

def crear_archivo_maestro(nombre_archivo, directorio=".", reservas=[]):
    """Crea el directorio y el archivo maestro con las reservas iniciales."""
    ruta_completa = os.path.join(directorio, nombre_archivo)
    os.makedirs(directorio, exist_ok=True)
    with open(ruta_completa, "w") as archivo:
        for reserva in reservas:
            archivo.write(f"{reserva}\n")
    print(f" Archivo maestro '{nombre_archivo}' creado en '{directorio}' con datos de prueba.")

def registrar_error(linea_con_error, descripcion):
    """Registra el error en el archivo de log con la fecha y hora actual."""
    ruta_log = os.path.join(DIRECTORIO_DESTINO, ARCHIVO_LOG_ERRORES)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Formato del log: [Data i Hora], [Línia amb error], [Descripció de l'error]
    linea_log = f"{timestamp}, \"{linea_con_error.strip()}\", {descripcion}\n"
    
    with open(ruta_log, "a") as log:
        log.write(linea_log)

def leer_clasificar_y_registrar_errores(nombre_archivo_maestro):
    """
    Lee el archivo maestro, valida las reservas, clasifica las válidas 
    y registra las no válidas.
    """
    print("\n--- INICIANDO PROCESO DE LECTURA Y CLASIFICACIÓN ---")
    
    ruta_maestro = os.path.join(DIRECTORIO_DESTINO, nombre_archivo_maestro)
    
    # Asegurar que el log esté limpio antes de empezar
    ruta_log = os.path.join(DIRECTORIO_DESTINO, ARCHIVO_LOG_ERRORES)
    if os.path.exists(ruta_log):
        os.remove(ruta_log)
    
    destinos_totales = {}  # Diccionario para contar reservas por destino

    try:
        with open(ruta_maestro, "r") as archivo:
            contenido = archivo.readlines()
    except FileNotFoundError:
        print(f" Error: El archivo maestro '{nombre_archivo_maestro}' no existe.")
        return

    for linea in contenido:
        linea_limpia = linea.strip()
        
        # 1. Validación de línea vacía
        if not linea_limpia:
            registrar_error(linea, "Línea vacía o solo espacios.")
            continue
        
        # 2. Validación de campos
        # Usamos split(',').strip() para asegurarnos de que el conteo de campos sea exacto.
        campos = [campo.strip() for campo in linea_limpia.split(',')]
        
        if len(campos) != NUM_CAMPOS_REQUERIDOS:
            # Determinamos la descripción del error
            if len(campos) < NUM_CAMPOS_REQUERIDOS:
                descripcion = f"Faltan {NUM_CAMPOS_REQUERIDOS - len(campos)} campos. Se esperaban {NUM_CAMPOS_REQUERIDOS}."
            else:
                descripcion = f"Sobran {len(campos) - NUM_CAMPOS_REQUERIDOS} campos. Se esperaban {NUM_CAMPOS_REQUERIDOS}."
                
            registrar_error(linea, descripcion)
            continue
        
        # 3. Clasificación y escritura (Línea Válida)
        
        # Campos Válidos: [0]=Asiento, [1]=Nombre, [2]=Clase, [3]=Destino
        destino = campos[3]
        ruta_destino = os.path.join(DIRECTORIO_DESTINO, f"{destino}.txt")
        
        # Escribir la reserva válida en el archivo de destino correspondiente
        with open(ruta_destino, "a") as archivo_destino:
            archivo_destino.write(f"{linea_limpia}\n")
        
        # Contar para el resumen final
        destinos_totales[destino] = destinos_totales.get(destino, 0) + 1

    return destinos_totales

def verificar_e_informar(destinos_totales):
    """Imprime el resumen de archivos de destino y el contenido del log de errores."""
    print("\n--- INFORME FINAL DE PROCESAMIENTO ---")
    
    # 1. Informar sobre archivos de destino
    if destinos_totales:
        print("\n Archivos de Destino Creados (Reservas Válidas):")
        for destino, count in destinos_totales.items():
            print(f"- **{destino}.txt**: Contiene **{count}** reservas válidas.")
    else:
        print("\n⚠️ No se procesaron reservas válidas para crear archivos de destino.")
        
    # 2. Informar sobre el log de errores
    ruta_log = os.path.join(DIRECTORIO_DESTINO, ARCHIVO_LOG_ERRORES)
    
    if os.path.exists(ruta_log) and os.path.getsize(ruta_log) > 0:
        print(f"\n Contenido del archivo de errores ({ARCHIVO_LOG_ERRORES}):")
        with open(ruta_log, "r") as log:
            print(log.read().strip())
    else:
        print(f"\n El archivo {ARCHIVO_LOG_ERRORES} está vacío. ¡No se registraron errores!")


# --- EJECUCIÓN PRINCIPAL ---

# 1. Crear el archivo maestro corrupto de prueba
crear_archivo_maestro(ARCHIVO_MAESTRO_ERRORES, DIRECTORIO_DESTINO, reservas_con_errores)

# 2. Leer, clasificar y registrar errores
reservas_por_destino = leer_clasificar_y_registrar_errores(ARCHIVO_MAESTRO_ERRORES)

# 3. Verificar e informar
verificar_e_informar(reservas_por_destino)