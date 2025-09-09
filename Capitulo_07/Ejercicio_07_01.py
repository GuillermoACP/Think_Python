'''
Ejercicio 7.1. Copia el bucle de la Sección 7.5 y encapsúlalo en una función llamada mi_sqrt
que tome a a como parámetro, escoja un valor razonable de x y devuelva una estimación de la raíz
cuadrada de a.
Para probarla, escribe una función con nombre probar_raiz_cuadrada que imprima una tabla
como esta:
a mi_sqrt(a) math.sqrt(a) diferencia
- ---------- ------------ ----------
1.0 1.0 1.0 0.0
2.0 1.41421356237 1.41421356237 2.22044604925e-16
3.0 1.73205080757 1.73205080757 0.0
4.0 2.0 2.0 0.0
5.0 2.2360679775 2.2360679775 0.0
6.0 2.44948974278 2.44948974278 0.0
7.0 2.64575131106 2.64575131106 0.0
8.0 2.82842712475 2.82842712475 4.4408920985e-16
9.0 3.0 3.0 0.0
La primera columna es un número, a; la segunda columna es la raíz cuadrada de a calculada con
mi_sqrt; la tercera columna es la raíz cuadrada calculada por math.sqrt; la cuarta columna es el
valor absoluto de la diferencia entre las dos estimaciones.
'''
import math

def mi_sqrt(a):
    x = a / 2  
    tolerancia = 1e-10
    while True:
        raiz = (x + a / x) / 2
        if abs(raiz - x) < tolerancia:
            return raiz
        x = raiz

def probar_raiz_cuadrada():
    print("{:<5} {:<15} {:<15} {:<15}".format("a", "mi_sqrt(a)", "math.sqrt(a)", "diferencia"))
    print("-" * 60)
    
    for i in range(1, 10):
        mi_sqrt_valor = mi_sqrt(i)
        math_sqrt_valor = math.sqrt(i)
        diferencia = abs(mi_sqrt_valor - math_sqrt_valor)
        print("{:<5} {:<15.10f} {:<15.10f} {:<15.10e}".format(i, mi_sqrt_valor, math_sqrt_valor, diferencia))

probar_raiz_cuadrada()


