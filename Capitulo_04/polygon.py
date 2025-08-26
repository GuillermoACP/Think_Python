from __future__ import print_function, division

import math
import turtle

def square(t, length):
    """Dibuja un cuadrado con lados del tamaño dado.

    Retorna la tortuga a la posición y orientación inicial.
    """
    for i in range(4):
        t.fd(length)   # mover hacia adelante
        t.lt(90)       # girar a la izquierda 90°

def polyline(t, n, length, angle):
    """Dibuja n segmentos de línea.

    t: objeto Turtle
    n: número de segmentos
    length: longitud de cada segmento
    angle: ángulo entre segmentos
    """
    for i in range(n):
        t.fd(length)  # dibuja un lado
        t.lt(angle)   # gira antes de dibujar el siguiente

def polygon(t, n, length):
    """Dibuja un polígono con n lados.

    t: objeto Turtle
    n: número de lados
    length: longitud de cada lado.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    """Dibuja un arco con radio y ángulo dados.

    t: objeto Turtle
    r: radio
    angle: ángulo del arco en grados
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360   # longitud real del arco
    n = int(arc_length / 4) + 3                      # número de segmentos
    step_length = arc_length / n                     # longitud de cada segmento
    step_angle = float(angle) / n                    # ángulo de cada segmento

    # pequeño ajuste: gira medio paso antes para reducir error
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def circle(t, r):
    """Dibuja un círculo con radio r.

    t: Turtle
    r: radio
    """
    arc(t, r, 360)   # simplemente llama a arc con 360°

if __name__ == '__main__':
    bob = turtle.Turtle()

    # dibujar un círculo centrado en el origen
    radius = 100
    bob.pu()         # levantar lápiz
    bob.fd(radius)   # mover hacia adelante el radio
    bob.lt(90)       # girar hacia arriba
    bob.pd()         # bajar lápiz
    circle(bob, radius)

    # esperar a que el usuario cierre la ventana
    turtle.mainloop()
