'''
Ejercicio 6.5. El máximo común divisor (MCD) de a y b es el número más grande que divide a ambos sin obtener resto.
Una manera de encontrar el MCD de dos números está basada en la observación de que si r es el resto de dividir a por b, entonces mcd(a, b) = mcd(b, r). Como caso base, podemos utilizar mcd(a, 0) = a.
Escribe una función llamada mcd que tome parámetros a y b y devuelva su máximo común divisor
'''

def mcd(a, b):
    # Caso base
    if b == 0:
        return a
    # r es el resto de dividir a por b
    r = a % b    
    return mcd(b, r)

print(mcd(48, 18))
print(mcd(56, 98))
print(mcd(101, 10))