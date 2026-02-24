import random
import time
import os

# --- CONFIGURACIÓN ---
DIM = 5  # Dimension de mi Matriz 5x5
PROFUNDIDAD_MINIMAX = 3 # Cuántos pasos a futuro ven los agentes

class JuegoPersecucion:
    def __init__(self):
        self.ancho = DIM
        self.alto = DIM
        # El gato empieza en la esquina superior izquierda
        self.gato = (0, 0)
        # El ratón empieza en un posicion inicial aleatoria (evitando que pise al gato al inicio)
        self.raton = (random.randint(1, DIM-1), random.randint(1, DIM-1))

    def limpiar_pantalla(self):
        # Limpia la consola según el sistema operativo
        os.system('cls' if os.name == 'nt' else 'clear')

    #Funcion dibujar el tablero y las posiciones del gato y el ratón
    def dibujar(self, turno):
        self.limpiar_pantalla()
        print(f"------ TURNO {turno} ------")
        for y in range(self.alto):
            fila = ""
            for x in range(self.ancho):
                if (x, y) == self.gato:
                    fila += " 🐈 "
                elif (x, y) == self.raton:
                    fila += " 🐭 "
                else:
                    fila += "  . "
            print(fila)
        print("-" * 21)

#Función de Rango de Movimientos Validos
def obtener_movimientos(pos):
    x, y = pos
    validos = []
    # Movimientos: Arriba, Abajo, Izquierda, Derecha
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < DIM and 0 <= ny < DIM:
            validos.append((nx, ny))
    return validos

#Función para evaluar estado del gato y el ratón con la distancia de Manhattan
def evaluar_estado(pos_gato, pos_raton):
    # Distancia de Manhattan: |x1 - x2| + |y1 - y2|
    return abs(pos_gato[0] - pos_raton[0]) + abs(pos_gato[1] - pos_raton[1])

#Función Algoritmo Minimax tanto para el Gato(Min) y el Ratón (Max)
def minimax(pos_gato, pos_raton, profundidad, es_maximizador):
    # Caso base: Gato atrapa al ratón
    if pos_gato == pos_raton:       
        return -100            #Con este valor evitamos a toda costa esta decisión que lleve al gato atrapar al ratón
    
    if profundidad == 0:        #Ya llega a la rama principal (se evalua distancia de manhattan entre los nodos)
        return evaluar_estado(pos_gato, pos_raton)

    if es_maximizador: # Turno del Ratón (Maximiza distancia)
        mejor_valor = -float('inf')       #Se usa para inicializar
        for mov in obtener_movimientos(pos_raton):
            valor = minimax(pos_gato, mov, profundidad - 1, False)
            mejor_valor = max(mejor_valor, valor)
        return mejor_valor
    else: # Turno del Gato (Minimiza distancia)
        mejor_valor = float('inf')      #Se usa para inicializar
        for mov in obtener_movimientos(pos_gato):
            valor = minimax(mov, pos_raton, profundidad - 1, True)
            mejor_valor = min(mejor_valor, valor)
        return mejor_valor

def ejecutar_simulacion():
    juego = JuegoPersecucion()
    
    for turno in range(1, 21): # Máximo 20 turnos para escapar
        juego.dibujar(turno)    # Dibujamos el turno
        time.sleep(0.5) # Pausa para ver la secuencia

        # 1. MOVIMIENTO DEL GATO (Minimiza Manhattan)
        mejor_puntuacion = float('inf') #Inicializamos el mejor valor con un numero muy alto
        proximo_paso_gato = juego.gato
        for mov in obtener_movimientos(juego.gato):
            puntos = minimax(mov, juego.raton, PROFUNDIDAD_MINIMAX, True)
            if puntos < mejor_puntuacion:
                mejor_puntuacion = puntos
                proximo_paso_gato = mov
        juego.gato = proximo_paso_gato
        #Si el gato atrapa el raton el juego termina
        if juego.gato == juego.raton:
            juego.dibujar(turno)
            print("¡EL GATO HA ALMORZADO! Game Over para el ratón.")
            return

        # 2. MOVIMIENTO DEL RATÓN (Maximiza Manhattan)
        mejor_puntuacion = -float('inf')        #Inicializamos mejor valor con un numero muy bajo
        proximo_paso_raton = juego.raton
        for mov in obtener_movimientos(juego.raton):
            puntos = minimax(juego.gato, mov, PROFUNDIDAD_MINIMAX, False)
            if puntos > mejor_puntuacion:
                mejor_puntuacion = puntos
                proximo_paso_raton = mov
        juego.raton = proximo_paso_raton

    print("EL RATÓN SE ESCAPÓ")

if __name__ == "__main__":
    ejecutar_simulacion()