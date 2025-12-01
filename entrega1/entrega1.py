jugadores = { 
    "j1" :{"puntos":120,"muertes":3},
    "j2" :{"puntos":50,"muertes":8}
}
def insertarElementos(jugadores,puntaje,muertes):
    while True:
        (""" Hasta que el nombre no sea valido siempre va a hacer este bucle para registrar un nombre válido""")
        nombre =input("Escribe tu nombre de jugador")
        if(nombre != ""):
            break
        else:
            print("El nombre no es válido")
       
    try:
        puntos = int(puntaje)
        numMuertes = int(muertes)
    except ValueError:
        print("Entrada de valores no válida.")

    nuevoJugador = {"puntos":puntos,"muertes":numMuertes} 
    """ Creamos una variable nuevo jugador para los datos de puntos y muertes """
    jugadores[nombre] = nuevoJugador
    """ Creo en el diccionario de jugadores el nuevo jugador con sus datos correspondientes """

def buscarJugador(jugadores):
    
    busqueda = input("Que jugador quieres buscar")
    encontrado = False
    for clave,valor in jugadores.items():
        if(clave == busqueda):
            print("Jugador: "+clave)
            puntos = valor["puntos"]
            muertes = valor["muertes"]
            print("Puntos: "+puntos)
            print("Muertes: "+muertes)
            encontrado = True
            break

    if(encontrado == False):
        print("El jugador que desea buscar no se encuentra dentro de la lista de jugadores")

def modificar(jugadores):
    busqueda = input("Que jugador quieres modificar")
    encontrado = False
    opcion =int(input("¿Que desea modificar?\n"
    "1.Nombre\n"
    "2.Puntos\n"
    "3.Muertes"))
    if(opcion == 1)
        """ Si la opcion es 1 modificara el nombre """
        nombre =input("Introduzca el nuevo nombre")
        if(nombre != ""):
            for clave in jugadores.keys():
                if(clave == busqueda):
                    jugadores[nombre] = jugadores.pop(busqueda)
                    encontrado = True
        else:
            print("El nombre no puede ser vacío")
        
    elif(opcion == 2):
        """ Si la opcion es 2 modificara los puntos del jugador  """
        puntos = input("Introduzca el valor nuevo para los puntos")
        try: 
            puntaje = int(puntos)
            if(puntos <0):
                print("No se puede tener un valor negativo")
            jugadores[busqueda]["puntos"] = puntaje
        except ValueError:
            print("El valor de puntos introducido no es válido")

    elif(opcion =3):
        """ Si la opcion es 3 modificara el numero de muertes del jugador """
        muertes = input("Introduzca el valor nuevo para el numero de muertes")
        try: 
            numMuertes = int(muertes)
            if(muertes <0):
                print("No se puede tener un valor negativo")
            jugadores[busqueda]["muertes"] = numMuertes
        except ValueError:
            print("El valor de muertes introducido no es válido")
    if(encontrado == False):
        print("El jugador que desea modificar no se encuentra en la lista de jugadores")


def eliminarElementos(jugadores):
    busqueda = input("Que jugador quieres eliminar")
    encontrado = False
    for clave in jugadores.keys():
        if(clave == busqueda):
            jugadores.pop(clave)
            encontrado = True
    
    if(encontrado = False):
        print("El jugador que desea eliminar no existe o ya ha sido eliminado previamente")
    

def mostrarTodos(jugadores):
    for clave in jugadores.keys():
        """ Recorremos todas las claves del diccionario de jugadores y vamos mostrando la clave junto a el propio diccionario de cada clave """
        print("----Jugador: {clave} -----")
        print("\n")
        print("Puntaje: {clave["puntos"]}")
        print("\n")
        print("NumMuertes💀: {clave["muertes"]}") 

def menu():
    resultado = int(input(""))
