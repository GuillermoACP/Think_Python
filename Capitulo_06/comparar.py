'''
Como ejercicio, escribe una función comparar que tome dos valores, x e y, y devuelva 1 si x > y, devuelva 0 si x == y o devuelva -1 si x < y.
'''

def comparar(x,y):
    if x > y:
        print('1')
        return 1
    elif x == y:
        print('0')
        return 0
    elif x < y:
        print('-1')
        return -1
    
comparar (2,2)
