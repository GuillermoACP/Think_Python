'''
Ejercicio 5.6. La curva de Koch es un fractal que se ve más o menos como en la Figura 5.2. Para dibujar una curva de Koch con longitud x, todo lo que tienes que hacer es
1. Dibujar una curva de Koch con longitud x/3.
2. Girar 60 grados a la izquierda.
50 Capítulo 5. Condicionales y recursividad
3. Dibujar una curva de Koch con longitud x/3.
4. Girar 120 grados a la derecha.
5. Dibujar una curva de Koch con longitud x/3.
6. Girar 60 grados a la izquierda.
7. Dibujar una curva de Koch con longitud x/3.
La excepción es si x es menor que 3: en ese caso, puedes simplemente dibujar una línea recta con longitud x.
1. Escribe una función llamada koch que tome una tortuga y una longitud como parámetros y que use a la tortuga para dibujar una curva de Koch con la longitud dada.
2. Escribe una función llamada copo_de_nieve que dibuje tres curvas de Koch que hagan el contorno de un copo de nieve.
'''

import turtle

def koch(tortuga, longitud):
    if longitud < 3:
        tortuga.forward(longitud)
    else:
        koch(tortuga, longitud / 3)
        tortuga.left(60)
        koch(tortuga, longitud / 3)
        tortuga.right(120)
        koch(tortuga, longitud / 3)
        tortuga.left(60)
        koch(tortuga, longitud / 3)

def copo_de_nieve(tortuga, longitud):
    for _ in range(3):
        koch(tortuga, longitud)
        tortuga.right(120)

copo_de_nieve(turtle.Turtle(), 300)