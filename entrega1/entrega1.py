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
