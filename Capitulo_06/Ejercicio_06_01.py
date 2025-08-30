'''
Ejercicio 6.1. Dibuja un diagrama de pila para el siguiente programa. ¿Qué imprime el programa
'''

def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    cuadrado = b(total)**2
    return cuadrado

x = 1
y = x + 1
print(c(x, y+3, x+y))