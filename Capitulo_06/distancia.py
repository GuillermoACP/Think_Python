import math

def distancia(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dcuadrado = dx**2 + dy**2
    resultado = math.sqrt(dcuadrado)
#    print(resultado)
    return resultado

#distancia(1,2,4,6)