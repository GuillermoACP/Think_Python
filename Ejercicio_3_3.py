'''
Ejercicio 3.3. Nota: Este ejercicio debería hacerse utilizando solo las sentencias y otras características que hemos aprendido hasta ahora.
1. Escribe una función que dibuje una cuadrícula como la siguiente:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +

Pista: para imprimir más de un valor en una línea, puedes imprimir una secuencia de valores separada por comas:

print('+', '-')

Por defecto, print avanza a la siguiente línea, pero puedes anular ese comportamiento y poner
un espacio al final, como esto:

print('+', end=' ')
print('-')

La salida de estas sentencias es '+ -' en la misma línea. La salida desde la siguiente sentencia
print debería comenzar en la siguiente línea.

2. Escribe una función que dibuje una cuadrícula similar con cuatro filas y cuatro columnas.
'''

def cuadricula_2x2():
    n = 2

    borde = ("+ " + "- " * 4) * n + "+"
    interior = ("| " + "  " * 4) * n + "|"

    bloque = borde + '\n' + (interior + '\n') * 4
    print(bloque + bloque + borde)

#cuadricula_2x2()

def cuadricula_4x4():
    n = 4
    borde = ("+ " + "- " * 4) * n + "+"
    interior = ("| "+ "  " * 4) * n + "|"
    n_bloq = 4
    bloque = ( borde + '\n' + (interior + '\n') * n ) * n_bloq
    print(bloque + borde)

cuadricula_4x4()
