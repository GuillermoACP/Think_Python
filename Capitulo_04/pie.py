from __future__ import print_function, division

import math
import turtle


def draw_pie(t, n, r):
    """Dibuja un pastel (pie) y luego mueve la tortuga a la derecha.

    t: Turtle
    n: número de segmentos
    r: longitud de los radios
    """
    polypie(t, n, r)           # dibuja el pastel
    t.pu()                     # levanta el lápiz
    t.fd(r*2 + 10)             # avanza a la derecha para dejar espacio
    t.pd()                     # baja el lápiz para dibujar de nuevo

def polypie(t, n, r):
    """Dibuja un pastel dividido en segmentos radiales.

    t: Turtle
    n: número de segmentos
    r: longitud de los radios
    """
    angle = 360.0 / n          # ángulo central de cada segmento
    for i in range(n):
        isosceles(t, r, angle/2)  # cada segmento es un triángulo isósceles
        t.lt(angle)               # gira para dibujar el siguiente


def isosceles(t, r, angle):
    """Dibuja un triángulo isósceles.

    La tortuga comienza y termina en el vértice,
    mirando hacia el centro de la base.

    t: Turtle
    r: longitud de los lados iguales
    angle: medio del ángulo del vértice (en grados)
    """
    y = r * math.sin(angle * math.pi / 180)  # altura desde el vértice a la base

    t.rt(angle)
    t.fd(r)               # dibuja un lado
    t.lt(90+angle)
    t.fd(2*y)             # dibuja la base
    t.lt(90+angle)
    t.fd(r)               # dibuja el otro lado
    t.lt(180-angle)       # reorienta la tortuga


bob = turtle.Turtle()

bob.pu()
bob.bk(130)     # retrocede un poco para centrar el dibujo
bob.pd()

# dibuja varios pasteles con distinto número de lados
size = 40
draw_pie(bob, 5, size)
draw_pie(bob, 6, size)
draw_pie(bob, 7, size)
draw_pie(bob, 8, size)

bob.hideturtle()
turtle.mainloop()
