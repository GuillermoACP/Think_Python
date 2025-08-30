'''
1. Escribe estas funciones en un archivo con nombre palindromo.py y pruébalas. ¿Qué ocurre si llamas a medio con una cadena de dos letras? ¿De una letra? ¿Qué pasa con la cadena vacía, la cual se escribe '' y no contiene letras?
2. Escribe una función llamada es_palindromo que tome una cadena como argumento y devuelva True si es un palíndromo y False si no. Recuerda que puedes utilizar la función incorporada len para verificar la longitud de una cadena.
'''

def primera(palabra):
    return palabra[0]
def ultima(palabra):
    return palabra[-1]
def medio(palabra):
    return palabra[1:-1]

print (medio('banana'))

def es_palindromo(cadena):
    if primera == ultima:
        return