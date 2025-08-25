'''
Ejercicio 3.1. Escribe una función con nombre justificar_derecha que tome una cadena con nombre s como parámetro e imprima la cadena con suficientes espacios al inicio de tal manera que la última letra de la cadena esté en la columna 70 de la pantalla.

>>> justificar_derecha('monty')
'''
 
def justificar_derecha(s):
    num_entrada = len(s)
    justificacion = 70 - num_entrada
    print ((' ' * justificacion) + s) 
    

justificar_derecha(s=input('Palabra: '))
