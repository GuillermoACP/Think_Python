"""
Este módulo contiene un ejemplo de código relacionado con:

Think Python, 2nd Edition
por Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey
Licencia: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division
import turtle

# Importamos funciones auxiliares de otro archivo polygon.py
from polygon import circle, arc

# ----------------------------
# NIVEL 0: primitivas básicas
# ----------------------------
# Aquí se definen funciones que simplemente envuelven
# los comandos básicos de turtle. No hacen nada nuevo, 
# solo sirven como base para niveles posteriores.

def fd(t, length):    # mover hacia adelante
    t.fd(length)

def bk(t, length):    # mover hacia atrás
    t.bk(length)

def lt(t, angle=90):  # girar a la izquierda
    t.lt(angle)

def rt(t, angle=90):  # girar a la derecha
    t.rt(angle)

def pd(t):            # bajar el lápiz
    t.pd()

def pu(t):            # levantar el lápiz
    t.pu()


# -----------------------------------------
# NIVEL 1: combinaciones simples de nivel 0
# -----------------------------------------
# Son pequeñas funciones que usan las primitivas del nivel 0.
# Aquí ya hay pequeñas secuencias, pero sin pre/post condiciones.

def fdlt(t, n, angle=90):
    """Avanza y luego gira a la izquierda"""
    fd(t, n)
    lt(t, angle)

def fdbk(t, n):
    """Avanza y regresa, quedando en el mismo lugar"""
    fd(t, n)
    bk(t, n)

def skip(t, n):
    """Levanta el lápiz, avanza, baja el lápiz"""
    pu(t)
    fd(t, n)
    pd(t)

def stump(t, n, angle=90):
    """Traza una línea vertical y deja a la tortuga arriba mirando a la derecha"""
    lt(t)
    fd(t, n)
    rt(t, angle)

def hollow(t, n):
    """Mueve la tortuga verticalmente, sin dibujar, y deja mirando a la derecha"""
    lt(t)
    skip(t, n)
    rt(t)


# ----------------------------------------------
# NIVEL 2: combinaciones de nivel 1 y 0 (más útiles)
# ----------------------------------------------
# Aquí se definen piezas que se usan para formar letras:
# postes (líneas verticales), vigas (horizontales), etc.

def post(t, n):
    """Traza una línea vertical y regresa a la posición original"""
    lt(t)
    fdbk(t, n)
    rt(t)

def beam(t, n, height):
    """Traza una línea horizontal a cierta altura y regresa"""
    hollow(t, n*height)   # mueve la tortuga hacia arriba
    fdbk(t, n)            # dibuja la línea
    hollow(t, -n*height)  # regresa hacia abajo

def hangman(t, n, height):
    """Línea vertical hasta una altura, línea horizontal y regreso"""
    stump(t, n * height)
    fdbk(t, n)
    lt(t)
    bk(t, n*height)
    rt(t)

def diagonal(t, x, y):
    """Traza una diagonal hasta un punto (x, y) y regresa"""
    from math import atan2, sqrt, pi
    angle = atan2(y, x) * 180 / pi   # calcula ángulo en grados
    dist = sqrt(x**2 + y**2)         # distancia con Pitágoras
    lt(t, angle)
    fdbk(t, dist)
    rt(t, angle)

def vshape(t, n, height):
    """Traza una V (diagonal izquierda + diagonal derecha)"""
    diagonal(t, -n/2, height*n)
    diagonal(t, n/2, height*n)

def bump(t, n, height):
    """Dibuja una "panza" (semicírculo) en cierta altura"""
    stump(t, n*height)
    arc(t, n/2.0, 180)     # usa la función arc importada de polygon
    lt(t)
    fdlt(t, n*height+n)


# -----------------------------------------------------------------
# FUNCIONES PARA DIBUJAR LETRAS (A, B, C, ... Z)
# -----------------------------------------------------------------
# Cada función dibuja una letra. 
# Precondición: la tortuga empieza en la esquina inferior izquierda de la letra.
# Postcondición: termina en la esquina inferior derecha, lista para la siguiente.
# Todas reciben: una tortuga t y un tamaño n.
# La mayoría de letras son de ancho n y alto 2n.

def draw_a(t, n):
    diagonal(t, n/2, 2*n)
    beam(t, n, 1)
    skip(t, n)
    diagonal(t, -n/2, 2*n)

def draw_b(t, n):
    bump(t, n, 1)
    bump(t, n, 0)
    skip(t, n/2)

def draw_c(t, n):
    hangman(t, n, 2)
    fd(t, n)

def draw_d(t, n):
    bump(t, 2*n, 0)
    skip(t, n)

def draw_ef(t, n):
    hangman(t, n, 2)
    hangman(t, n, 1)

def draw_e(t, n):
    draw_ef(t, n)
    fd(t, n)

def draw_f(t, n):
    draw_ef(t, n)
    skip(t, n)

def draw_g(t, n):
    hangman(t, n, 2)
    fd(t, n/2)
    beam(t, n/2, 2)
    fd(t, n/2)
    post(t, n)

def draw_h(t, n):
    post(t, 2*n)
    hangman(t, n, 1)
    skip(t, n)
    post(t, 2*n)

def draw_i(t, n):
    beam(t, n, 2)
    fd(t, n/2)
    post(t, 2*n)
    fd(t, n/2)

def draw_j(t, n):
    beam(t, n, 2)
    arc(t, n/2, 90)
    fd(t, 3*n/2)
    skip(t, -2*n)
    rt(t)
    skip(t, n/2)

def draw_k(t, n):
    post(t, 2*n)
    stump(t, n, 180)
    vshape(t, 2*n, 0.5)
    fdlt(t, n)
    skip(t, n)

def draw_l(t, n):
    post(t, 2*n)
    fd(t, n)

def draw_n(t, n):
    post(t, 2*n)
    skip(t, n)
    diagonal(t, -n, 2*n)
    post(t, 2*n)

def draw_m(t, n):
    post(t, 2*n)
    draw_v(t, n)
    post(t, 2*n)

def draw_o(t, n):
    skip(t, n)
    circle(t, n)   # usa la función circle importada de polygon
    skip(t, n)

def draw_p(t, n):
    bump(t, n, 1)
    skip(t, n/2)

def draw_q(t, n):
    draw_o(t, n)
    diagonal(t, -n/2, n)

def draw_r(t, n):
    draw_p(t, n)
    diagonal(t, -n/2, n)

def draw_s(t, n):
    fd(t, n/2)
    arc(t, n/2, 180)
    arc(t, n/2, -180)
    fdlt(t, n/2, -90)
    skip(t, 2*n)
    lt(t)

def draw_t(t, n):
    beam(t, n, 2)
    skip(t, n/2)
    post(t, 2*n)
    skip(t, n/2)

def draw_u(t, n):
    post(t, 2*n)
    fd(t, n)
    post(t, 2*n)

def draw_v(t, n):
    skip(t, n/2)
    vshape(t, n, 2)
    skip(t, n/2)

def draw_w(t, n):
    draw_v(t, n)
    draw_v(t, n)

def draw_x(t, n):
    diagonal(t, n, 2*n)
    skip(t, n)
    diagonal(t, -n, 2*n)

def draw_v(t, n):  # ¡OJO! esta función sobrescribe la anterior draw_v
    skip(t, n/2)
    diagonal(t, -n/2, 2*n)
    diagonal(t, n/2, 2*n)
    skip(t, n/2)

def draw_y(t, n):
    skip(t, n/2)
    stump(t, n)
    vshape(t, n, 1)
    rt(t)
    fdlt(t, n)
    skip(t, n/2)

def draw_z(t, n):
    beam(t, n, 2)
    diagonal(t, n, 2*n)
    fd(t, n)

def draw_(t, n):
    """Dibuja un espacio en blanco"""
    skip(t, n)


# ---------------------------------------------------
# PROGRAMA PRINCIPAL: dibujar la palabra HELLO
# ---------------------------------------------------
if __name__ == '__main__':

    # crear y posicionar la tortuga
    size = 20
    bob = turtle.Turtle()

    # dibujar las letras H, E, L, L, O
    for f in [draw_h, draw_e, draw_l, draw_l, draw_o]:
        f(bob, size)
        skip(bob, size)

    turtle.mainloop()
