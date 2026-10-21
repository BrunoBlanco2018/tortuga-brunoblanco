"""Primer hito: carrera de dos tortugas.

La infraestructura gráfica ya está resuelta. Los TODO sólo requieren variables,
condicionales y bucles, que son los contenidos impartidos al anunciar M1.
"""

from __future__ import annotations

import turtle

import random #Implemento esta variable como mejora del código para darle aleatoriedad a la carrera

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
START_X = -320
FINISH_X = 300

# TODO 1: asigna dos velocidades positivas. Predice quién ganará.
RED_SPEED = 0
BLUE_SPEED = 0


def prepare_game():
    """Prepara la ventana, la pista y las dos tortugas (código proporcionado)."""
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.title("Carrera de tortugas")

    painter = turtle.Turtle(visible=False)
    painter.speed(0)
    for y in (-80, 0, 80):
        painter.penup()
        painter.goto(START_X, y)
        painter.pendown()
        painter.forward(FINISH_X - START_X)

    red = turtle.Turtle(shape="turtle")
    red.color("red")
    red.penup()
    red.goto(START_X, 40)

    blue = turtle.Turtle(shape="turtle")
    blue.color("blue")
    blue.penup()
    blue.goto(START_X, -40)
    return screen, red, blue


def run_race(red: turtle, blue: turtle) -> str:
    """Mueve las tortugas hasta que una alcance la meta."""
    # TODO 2: valida con un condicional que ambas velocidades sean positivas.
    # Si alguna no lo es, muestra un mensaje y devuelve una cadena vacía.
    if RED_SPEED <= 0 or BLUE_SPEED <= 0:
        print("La velocidad de ambas tortugas debe ser positiva")
        return ""
    
    # TODO 3: crea un bucle que mueva las dos tortugas en cada vuelta.
    # Cuando una alcance FINISH_X, devuelve "roja" o "azul".
    # Si las dos alcanzan FINISH_X en la misma vuelta, devuelve "empate".
    while red.xcor() < FINISH_X and blue.xcor() < FINISH_X:
        red.forward(RED_SPEED)
        blue.forward(BLUE_SPEED)
    if red.xcor() >= FINISH_X and blue.xcor() < FINISH_X:
        return "roja"
    elif red.xcor() < FINISH_X and blue.xcor() >= FINISH_X:
        return "azul"
    else:
        return "empate"

def aleatoriezar_velocidad(vel_min, vel_max):
    global RED_SPEED
    global BLUE_SPEED
    RED_SPEED = random.randint(vel_min, vel_max)
    BLUE_SPEED = random.randint(vel_min, vel_max)

def main():
    """Pone en marcha la carrera (código proporcionado)."""
    screen, red, blue = prepare_game()
    aleatoriezar_velocidad(1, 5) #Extra añadido para dar aleatoriedad a la carrera
    winner = run_race(red, blue)
    if winner == "empate":
        screen.title("¡Empate! Las dos tortugas llegan a la vez")
    elif winner:
        screen.title(f"¡Ha ganado la tortuga {winner}!")
    screen.mainloop()


if __name__ == "__main__":
    main()