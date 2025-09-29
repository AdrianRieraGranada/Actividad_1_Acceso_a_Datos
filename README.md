# ACTIVIDAD 1

## HERRAMIENTAS USADAS
He usado la versión de **Python 3.12**, las librerías **"os"** para la creación de **ficheros** y **"datetime"** para obtener la fecha y la hora de hoy. Y para el uso de IA he usado Copilot para **ayudarme a hacer** las diversas partes, en especial la tercera parte. He documentado partes de la conversación en **IA.md**. 

---
### Parte 1
En esta parte solo hemos **hecho uso** de la librería **os** para la creación y lectura del archivo. **Hemos creado** un archivo y **escrito** la información de reserva para posteriormente leer la información de las reservas escritas y sacar **cuántas** personas van en **Business**. Resultado al ejecutar el script:

Archivo 'reservas.txt' creado exitosamente en 'Act1'.
Se han escrito las reservas en el archivo.

Listado de Reservas:
Número de Asiento: 12A, Nombre: Juan Pérez, Clase: Economy
Número de Asiento: 14B, Nombre: María López, Clase: Business
Número de Asiento: 21C, Nombre: Carlos García, Clase: Economy

Resumen:
Total de pasajeros: 3
Total de pasajeros en clase Business: 1

---
### Parte 2
En la parte 2 **leemos** las reservas y crearemos tantos archivos como destinos haya, sin que se repitan a la hora de crear el archivo (**ejemplo:** si hay dos de Madrid, se **creará** Madrid.txt) y en estos añadiremos a todos los pasajeros con cuyo destino coincida. Resultado al ejecutar el script:

Creado el archivo para el destino Madrid
Total de pasajeros para Madrid: 3

Creado el archivo para el destino París
Total de pasajeros para París: 3

Creado el archivo para el destino Londres
Total de pasajeros para Londres: 3

---
### Parte 3
Se trata de hacer lo mismo que en la parte 2, pero con gestión de errores y haciendo una breve descripción de lo que le falta a la reserva e indicar **día** y hora de cuando **dio** el error. Resultado al ejecutar el script:

Archivo maestro 'reservas_maestro_con_errores.txt' creado en 'Act1' con datos de prueba.

--- INICIANDO PROCESO DE LECTURA Y CLASIFICACIÓN ---

--- INFORME FINAL DE PROCESAMIENTO ---

Archivos de Destino Creados (Reservas Válidas):
- **Madrid.txt**: Contiene **1** reservas válidas.
- **París.txt**: Contiene **1** reservas válidas.
- **Londres.txt**: Contiene **2** reservas válidas.
- **Milán.txt**: Contiene **1** reservas válidas.

Contenido del archivo de errores (registro_errores.log):
2025-09-29 17:29:35, "21C, Carlos García, Economy", Faltan 1 campos. Se esperaban 4.
2025-09-29 17:29:35, "19E, Luis Gómez", Faltan 2 campos. Se esperaban 4.
2025-09-29 17:29:35, "", Línea vacía o solo espacios.
2025-09-29 17:29:35, "25G, Pedro Martínez, First, New York, Extra", Sobran 1 campos. Se esperaban 4.
