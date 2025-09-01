'''
Ejercicio 6.4. Un número, a, es potencia de b si es divisible por b y además a/b es potencia de b. Escribe una función llamada es_potencia que tome parámetros a y b y devuelva True si a es potencia de b. 
Nota: tendrás que pensar en el caso base
'''


def es_potencia(a, b):
    if a == 1:
        return True
    if a % b != 0:
        return False
    return es_potencia(a // b, b)

print(es_potencia(8, 2))
print(es_potencia(9, 3))
print(es_potencia(27, 3))
print(es_potencia(10, 2))