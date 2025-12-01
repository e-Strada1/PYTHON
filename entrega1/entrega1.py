jugadores = { 
    "j1" :{"puntos":120,"muertes":3},
    "j2" :{"puntos":50,"muertes":8}
}

def insertar_elementos(jugadores):
    while True:
        (""" Hasta que el nombre no sea valido siempre va a hacer este bucle para registrar un nombre válido""")
        nombre =input("Escribe tu nombre de jugador")
        if(nombre != ""):
            break
        else:
            print("El nombre no es válido")
    while True:
        """ Hasta que el nombre no sea valido siempre va a hacer este bucle para registrar una cantidad de puntos válida
        Esta parte debera recibir los puntos pasado por parametro"""
        puntaje = input("Introduce el numero de punto del jugador")
        muertes = input("Introduce el numero de muertes del jugador")
        try:
            puntos = int(puntaje)
            numMuertes = int(muertes)
            if(puntos >= 0 and numMuertes >=0):
                break
            else:
                print("Valores introducidos no válidos. Los valores deben ser mayores o iguales a cero")
        except ValueError:
            print("Entrada de valores no válida.")