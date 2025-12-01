jugadores = { 
    "j1" :{"puntos":120,"muertes":3},
    "j2" :{"puntos":50,"muertes":8}
}
def insertarElementos(jugadores,puntaje,muertes):#Funcion para insertar un nuevo jugador en el diccionario. Los puntos y muertes deberan ser pasados y tratados antes.
    while True:
        """ Hasta que el nombre no sea valido siempre va a hacer este bucle para registrar un nombre válido"""
        nombre =input("Escribe tu nombre de jugador: ")
        print("")
        if(nombre != ""):
            break
        else:
            print("El nombre no es válido\n")
       
    try:
        puntos = int(puntaje)
        numMuertes = int(muertes)
    except ValueError:
        print("Entrada de valores no válida.\n")

    nuevoJugador = {"puntos":puntos,"muertes":numMuertes} 
    """ Creamos una variable nuevo jugador para los datos de puntos y muertes """
    jugadores[nombre] = nuevoJugador
    """ Creo en el diccionario de jugadores el nuevo jugador con sus datos correspondientes """

def buscarJugador(jugadores):#Función de busqueda que encontrara el jugador que desee el usuario
    
    busqueda = input("Que jugador quieres buscar: ")
    encontrado = False #Declaro la variable encontrado a false para en el futuro comprobar si se ha encontrado o no el jugador
    for clave in jugadores.keys():#Para todos las claves busca la clave que sea la buscada y lo muestra
        if(clave == busqueda): 
            print("\nJugador: "+clave)
            puntos = jugadores[clave]["puntos"]
            muertes = jugadores[clave]["muertes"]
            print("Puntos: "+str(puntos)+"\n")
            print("Muertes: "+str(muertes)+"\n")
            encontrado = True
            break

    if(encontrado == False):
        print("El jugador que desea buscar no se encuentra dentro de la lista de jugadores\n")

def modificar(jugadores):
    busqueda = input("Que jugador quieres modificar: ")
    encontrado = False #Declaro la variable encontrado a false para en el futuro comprobar si se ha encontrado o no el jugador en cualquiera de las opciones
    opcion =int(input("\n¿Que desea modificar?\n"
    "1.Nombre\n"
    "2.Puntos\n"
    "3.Muertes\n"))
    if(opcion == 1):
        """ Si la opcion es 1 modificara el nombre """
        nombre =input("Introduzca el nuevo nombre: ")
        if(nombre != ""): #Comprobamos que el nombre no este vacío
            for clave in jugadores.keys():
                if(clave == busqueda):
                    jugadores[nombre] = jugadores.pop(busqueda) #Añadimos en el diccionario un jugador nuevo con el nombre al que se quiere cambiar y mediante la función pop borramos la antigua y obtenemos los datos que le daremos al nuevo jugador
                    encontrado = True #Se ha encontrado el jugador por lo que cambio el parametro encontrado a True 
        else:
            print("El nombre no puede ser vacío")
        
    elif opcion == 2:
        """ Si la opcion es 2 modificara los puntos del jugador  """
        puntos = input("Introduzca el valor nuevo para los puntos: ")
        try: 
            puntaje = int(puntos) #Comprobamos que la variable puntos pueda pasarse a entero
            if(puntaje <0):
                print("No se puede tener un valor negativo\n")
            jugadores[busqueda]["puntos"] = puntaje
            encontrado = True
        except ValueError: #Siempre que el valor de puntos no sea valido vendra a esta excepcion
            print("El valor de puntos introducido no es válido\n")

    elif opcion == 3:
        """ Si la opcion es 3 modificara el numero de muertes del jugador """
        muertes = input("Introduzca el valor nuevo para el numero de muertes: ")
        try: 
            numMuertes = int(muertes) #Comprobamos que el numMuertes pueda pasarse a entero
            if(muertes <0):
                print("No se puede tener un valor negativo\n")
            jugadores[busqueda]["muertes"] = numMuertes
            encontrado = True
        except ValueError: #Siempre que el valor de numMuertes no sea valido vendra a esta excepcion
            print("El valor de muertes introducido no es válido\n")
    if(encontrado == False):
        print("El jugador que desea modificar no se encuentra en la lista de jugadores\n")
    print("\n")

def eliminarElementos(jugadores):
    busqueda = input("Que jugador quieres eliminar\n")
    encontrado = False # Declaramos una variable encontrado par saber si se ha encontrado el jugador que se desea eliminar
    for clave in jugadores.keys(): #Hacemos un bucle para buscar en todo el diccionario de jugadores
        if(clave == busqueda):
            jugadores.pop(clave) #Con la función pop borramos el diccionario del jugador deseado
            encontrado = True# Cambiamos el valor de encontrado ya que se ha conseguido encontra el jugador que se desea eliminar
            break
    if encontrado == False:
        print("El jugador que desea eliminar no existe o ya ha sido eliminado previamente\n")
    

def mostrarTodos(jugadores):
    for clave in jugadores.keys():
        """ Recorremos todas las claves del diccionario de jugadores y vamos mostrando la clave junto a el propio diccionario de cada clave """
        print("----Jugador:"+clave+"-----\n")
        print("Puntaje: "+ str(jugadores[clave]["puntos"])+"\n")
        print("NumMuertes💀 : "+str(jugadores[clave]["muertes"])+"\n")

def menu(): #Funcion para definir un menu 
    resultado = int(input("1. Añadir elemento\n"
    "2. Buscar elemento\n"
    "3. Modificar elemento\n"
    "4. Eliminar elemento\n"
    "5. Mostrar todos\n"
    "6. Salir\n"))
    return resultado

opcion = menu()

while opcion != 6:
    if opcion == 1:
        puntos = input("Introduce un numero de puntos: ")
        muertes = input("Introduce un numero de muertes: ")
        insertarElementos(jugadores,puntos,muertes)
    elif opcion ==2:
        buscarJugador(jugadores)
    elif opcion ==3:
        modificar(jugadores)
    elif opcion ==4:
        eliminarElementos(jugadores)
    elif opcion ==5:
        mostrarTodos(jugadores)
    
    opcion = menu()