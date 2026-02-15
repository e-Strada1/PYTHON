import json
import os
import random

class Jugador:
    def __init__(self, nombre, puntos=0, fallos=0):
        self.nombre = nombre
        self.puntos = puntos
        self.fallos = fallos
        self.tipo = "Normal"

    def to_dict(self):
        return self.__dict__

class JugadorEspecial(Jugador):
    def __init__(self, nombre, habilidad, puntos=0, fallos=0):
        super().__init__(nombre, puntos, fallos)
        self.habilidad = habilidad
        self.tipo = "Especial"

class GestionJuego:
    def __init__(self):
        self.ruta_json = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plantilla.json")
        self.plantilla = []
        self.cargar_datos()

    def escribir_archivo(self):
        try:
            lista_dicts = [j.to_dict() for j in self.plantilla]
            with open(self.ruta_json, 'w', encoding='utf-8') as f:
                json.dump(lista_dicts, f, indent=4, ensure_ascii=False)
            print(f"\n[SISTEMA] Datos guardados correctamente.")
        except Exception as e:
            print(f"[ERROR] No se pudo guardar: {e}")

    def cargar_datos(self):
        if os.path.exists(self.ruta_json):
            try:
                with open(self.ruta_json, 'r', encoding='utf-8') as f:
                    datos = json.load(f)
                    for d in datos:
                        if d.get("tipo") == "Especial":
                            obj = JugadorEspecial(d['nombre'], d['habilidad'], d['puntos'], d['fallos'])
                        else:
                            obj = Jugador(d['nombre'], d['puntos'], d['fallos'])
                        self.plantilla.append(obj)
            except: pass

    def buscar_jugador(self, nombre_buscado):
        """Busca un objeto jugador por su nombre (sin importar mayúsculas)."""
        for j in self.plantilla:
            if j.nombre.lower() == nombre_buscado.lower():
                return j
        return None

    def jugar_mates(self, jugador):
        print(f"\n--- PARTIDA DE {jugador.nombre.upper()} ---")
        print("Dificultades: 1. Fácil | 2. Medio | 3. Difícil")
        dif = input("Elige (1-3): ")

        if dif == "1": rango, multi = 10, 1
        elif dif == "2": rango, multi = 20, 3
        else: rango, multi = 50, 5

        for _ in range(3):
            a, b = random.randint(1, rango), random.randint(1, rango)
            operacion = "+" if dif == "1" else "*" if dif == "2" else random.choice(["+", "*", "-"])
            
            if operacion == "+": correcto = a + b
            elif operacion == "*": correcto = a * b
            else: correcto = a - b

            try:
                respuesta = int(input(f"¿Cuánto es {a} {operacion} {b}? "))
                if respuesta == correcto:
                    puntos = 10 * multi
                    jugador.puntos += puntos
                    print(f"¡Correcto! +{puntos} pts.")
                else:
                    jugador.fallos += 1
                    print(f"Fallo. Era {correcto}.")
            except ValueError:
                jugador.fallos += 1
                print("Entrada no válida.")

        self.escribir_archivo()

    def menu(self):
        while True:
            print("\n--- MENÚ PRINCIPAL ---")
            print("1. Nuevo Jugador | 2. Ver Ranking | 3. Jugar | 4. Salir")
            op = input("> ")

            if op == "1":
                nom = input("Nombre: ")
                esp = input("¿Especial? (s/n): ").lower() == 's'
                nuevo = JugadorEspecial(nom, input("Habilidad: ")) if esp else Jugador(nom)
                self.plantilla.append(nuevo)
                self.escribir_archivo()

            elif op == "2":
                print("\n--- RANKING ---")
                for j in self.plantilla:
                    print(f"{j.nombre:12} | Puntos: {j.puntos} | Fallos: {j.fallos}")

            elif op == "3":
                nombre = input("Introduce el nombre del jugador para jugar: ")
                jugador_encontrado = self.buscar_jugador(nombre)
                
                if jugador_encontrado:
                    self.jugar_mates(jugador_encontrado)
                else:
                    print(f"El jugador '{nombre}' no existe.")

            elif op == "4": break

if __name__ == "__main__":
    GestionJuego().menu()