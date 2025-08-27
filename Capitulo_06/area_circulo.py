from distancia import *

def area(r):
    return math.pi * r**2

def area_circulo(xc, yc, xp, yp):
    radio = distancia(xc, yc, xp, yp)
    resultado = area(radio)
    print (resultado)
    return resultado

area_circulo(1,2,4,6)