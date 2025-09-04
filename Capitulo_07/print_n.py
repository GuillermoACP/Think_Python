'''
Como ejercicio, reescribe la función print_n de la Sección 5.8 utilizando iteración en lugar de recursividad.
'''

def print_n(s, n):
    while n > 0:
        print(s)
        n -= 1