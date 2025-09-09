'''
70 Capítulo 7. Iteración
Ejercicio 7.2. La función incorporada eval toma una cadena y la evalúa utilizando el intérprete
de Python. Por ejemplo:
>>> eval('1 + 2 * 3')
7
>>> import math
>>> eval('math.sqrt(5)')
2.2360679774997898
>>> eval('type(math.pi)')
<class 'float'>
Escribe una función llamada bucle_eval que, de manera iterativa, solicite la entrada del usuario,
tome la entrada resultante y la evalúe utilizando eval, e imprima el resultado.
Debería continuar hasta que el usuario ingrese 'listo' y luego devuelva el valor de la última
expresión que evaluó.
'''
def bucle_eval():
    resultado = None
    while True:
        entrada = input('Ingrese una expresión (o "listo" para terminar): ')
        if entrada == 'listo':
            break
        try:
            resultado = eval(entrada)
            print('Resultado:', resultado)
        except Exception as e:
            print('Error al evaluar la expresión:', e)
    return resultado

bucle_eval()