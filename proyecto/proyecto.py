class Juego:
    def iniciar_Resultados():
        puntos = 0
        muertes = 0
        return puntos,muertes
    def reiniciar_Resultados(puntos,muertes):
        puntos =0
        muertes =0
        return puntos,muertes
    def mostrar_Resultados(puntos,muertes):
        print("Puntos: "+puntos)
        print("")
        print("Muertes: "+muertes)
    

class Jugador:
    nombre = ""
    puntuaciones = {"puntos": 0,"muertes":0}
    