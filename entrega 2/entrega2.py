import json
import logging
import os

# Detectamos la carpeta donde se encuentra este script (.py)
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Enlazamos los nombres de los archivos a esa carpeta específica
ARCHIVO_DATOS = os.path.join(directorio_actual, "datos.json")
ARCHIVO_LOG = os.path.join(directorio_actual, "progreso.log")

logging.basicConfig(
    filename=ARCHIVO_LOG, 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

def cargar_datos():
    """Busca el JSON en la carpeta del script. Si no existe, lo crea."""
    try:
        if os.path.exists(ARCHIVO_DATOS):
            with open(ARCHIVO_DATOS, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                logging.info(f"Fichero JSON cargado desde: {ARCHIVO_DATOS}")
                return datos
        else:
            # Si el archivo no existe, creamos uno inicial
            datos_iniciales = { 
                "j1": {"puntos": 120, "muertes": 3},
                "j2": {"puntos": 50, "muertes": 8}
            }
            with open(ARCHIVO_DATOS, 'w', encoding='utf-8') as f:
                json.dump(datos_iniciales, f, indent=4)
            logging.info("Archivo JSON no detectado. Se ha creado uno nuevo con datos iniciales.")
            return datos_iniciales
    except Exception as e:
        logging.error(f"Error al cargar JSON: {e}")
        return {}

def guardar_datos(jugadores):
    """Sobreescribe el JSON con la información actualizada."""
    try:
        with open(ARCHIVO_DATOS, 'w', encoding='utf-8') as f:
            json.dump(jugadores, f, indent=4, ensure_ascii=False)
        logging.info("Cambios guardados exitosamente en el archivo JSON.")
    except Exception as e:
        logging.error(f"No se pudo guardar en el JSON: {e}")

# Inicializamos los datos al arrancar
jugadores = cargar_datos()

def insertarElementos(jugadores, puntaje, muertes):
    while True:
        nombre = input("Escribe tu nombre de jugador: ")
        if nombre.strip():
            break
        print("El nombre no es válido\n")
       
    try:
        jugadores[nombre] = {"puntos": int(puntaje), "muertes": int(muertes)}
        guardar_datos(jugadores)
        logging.info(f"Registro exitoso: {nombre}")
        print(f"Jugador {nombre} guardado.\n")
    except ValueError:
        logging.error("Error de formato en puntos/muertes al insertar.")
        print("Error: Los puntos y muertes deben ser números.\n")

def buscarJugador(jugadores):
    busqueda = input("Nombre del jugador a buscar: ")
    if busqueda in jugadores:
        p, m = jugadores[busqueda]["puntos"], jugadores[busqueda]["muertes"]
        print(f"\nJugador: {busqueda}\nPuntos: {p}\nMuertes: {m}\n")
        logging.info(f"Consulta: Datos de {busqueda} visualizados.")
    else:
        print("Jugador no encontrado.\n")
        logging.warning(f"Consulta fallida: {busqueda} no existe.")

def modificar(jugadores):
    busqueda = input("¿Qué jugador quieres modificar?: ")
    if busqueda not in jugadores:
        print("El jugador no existe.\n")
        return

    try:
        print("\n1.Nombre | 2.Puntos | 3.Muertes")
        opcion = int(input("Opción: "))
        
        if opcion == 1:
            nuevo_nombre = input("Nuevo nombre: ")
            if nuevo_nombre.strip():
                jugadores[nuevo_nombre] = jugadores.pop(busqueda)
                logging.info(f"Modificación: {busqueda} renombrado a {nuevo_nombre}")
        elif opcion == 2:
            jugadores[busqueda]["puntos"] = int(input("Nuevos puntos: "))
            logging.info(f"Modificación: Puntos actualizados para {busqueda}")
        elif opcion == 3:
            jugadores[busqueda]["muertes"] = int(input("Nuevas muertes: "))
            logging.info(f"Modificación: Muertes actualizadas para {busqueda}")
        
        guardar_datos(jugadores)
        print("Cambios aplicados.\n")
    except ValueError:
        logging.error("Error de valor en la modificación.")
        print("Error: Entrada no válida.\n")

def eliminarElementos(jugadores):
    busqueda = input("Jugador a eliminar: ")
    if busqueda in jugadores:
        jugadores.pop(busqueda)
        guardar_datos(jugadores)
        logging.info(f"Eliminación: Jugador {busqueda} borrado.")
        print("Eliminado con éxito.\n")
    else:
        logging.warning(f"Eliminación fallida: {busqueda} no existe.")

def mostrarTodos(jugadores):
    print("\n--- LISTADO ---")
    for k, v in jugadores.items():
        print(f"{k}: {v['puntos']} pts, {v['muertes']} muertes")
    print("---------------\n")
    logging.info("Listado completo mostrado.")

def menu():
    print("1.Añadir | 2.Buscar | 3.Modificar | 4.Eliminar | 5.Mostrar | 6.Salir")
    try: return int(input("Selección: "))
    except: return 0

logging.info("--- INICIO DE SESIÓN ---")

while True:
    op = menu()
    if op == 1:
        insertarElementos(jugadores, input("Puntos: "), input("Muertes: "))
    elif op == 2: buscarJugador(jugadores)
    elif op == 3: modificar(jugadores)
    elif op == 4: eliminarElementos(jugadores)
    elif op == 5: mostrarTodos(jugadores)
    elif op == 6:
        logging.info("--- FIN DE SESIÓN ---")
        break
    else: print("Opción inválida.\n")