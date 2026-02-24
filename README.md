# The-Dive-Challenge-1
El Laberinto del Gato y el Ratón: Un Duelo de Inteligencias en Python

Este proyecto implementa un simulador de persecución inteligente en un tablero bidimensional, donde un gato y un ratón compiten estratégicamente utilizando el algoritmo Minimax.
El objetivo es modelar un entorno adversarial donde:
El gato intenta minimizar la distancia y atrapar al ratón.
El ratón intenta maximizar su distancia y sobrevivir la mayor cantidad de turnos posible.
El proyecto fue desarrollado completamente desde cero utilizando únicamente Python estándar, sin librerías externas de inteligencia artificial.

¿Qué hace esta aplicación?

Genera un tablero bidimensional configurable.
Define posiciones iniciales para gato y ratón.
Simula turnos alternados.
Implementa Minimax para la toma de decisiones estratégicas.
Evalúa estados del juego usando distancia Manhattan.
Determina automáticamente el ganador según las condiciones establecidas.
El sistema modela un entorno de decisión adversarial similar a juegos como ajedrez, pero simplificado a un entorno de persecución.

Lógica del Juego
Turnos
Cada turno:
  - Se evalúan los posibles movimientos.
  - Se generan nuevos estados del tablero.
  - Se aplica Minimax con profundidad limitada.
  - Se selecciona el mejor movimiento según la función heurística.

Función de Evaluación

Se utiliza la distancia Manhattan entre el gato y el ratón:
- El gato busca minimizar esta distancia.
- El ratón busca maximizarla.

Estados del Juego

  Cada nodo del árbol de Minimax representa:
  - Posición del gato
  - Posición del ratón
  - Turno actual
  - Profundidad restante

Tecnologías Utilizadas

- Python 3
- Programación Orientada a Objetos
- Algoritmo Minimax
- Estructuras de datos (listas, tuplas)

Cómo Ejecutarlo
python minimax_lab.py

No requiere instalación de dependencias externas.

Condiciones de Finalización

  El juego termina cuando:
  - El gato alcanza la misma posición que el ratón.
  - Se alcanza el número máximo de turnos (supervivencia del ratón).

Mejoras Implementadas

- Separación clara de responsabilidades (tablero, lógica, simulación).
- Control de profundidad para evitar explosión combinatoria.
- Simulación visual básica en consola.
- Estructura extensible para agregar obstáculos o mejoras futuras.

Principales Aprendizajes

- Implementación práctica del algoritmo Minimax.
- Modelado de estados en árboles de decisión.
- Importancia de limitar profundidad por complejidad exponencial.
- Diseño estructurado usando clases.
- Simulación paso a paso para depuración.

Posibles Mejoras Futuras

- Implementar poda Alpha-Beta.
- Agregar obstáculos dinámicos.
- Implementar ratón inteligente vs gato inteligente simultáneamente.
- Interfaz interactiva para que el usuario juegue.
- Métricas de rendimiento y análisis de tiempo de ejecución.

👨‍💻 Autor

Alan Nunez
