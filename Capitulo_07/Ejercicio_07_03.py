'''
Ejercicio 7.3. El matemático Srinivasa Ramanujan encontró una serie infinita que se puede utilizar
para generar una aproximación numérica de 1/π:
            ∞
            ____
            \
            /    (4k)!(1103 + 26390k)
            ---- --------------------
            k=0 ((k!)^4 396^(4k))

Escribe una función llamada estimacion_pi que utilice esta fórmula para calcular y devolver una
estimación de π. Debería utilizar un bucle while para calcular términos de la sumatoria hasta que
el último término sea más pequeño que 1e-15 (que es la notación de Python para 10−15). Puedes
verificar el resultado comparándolo con math.pi.
'''
import math

def estimacion_pi():
    k = 0
    suma = 0
    termino = 1  # Inicializamos con un valor mayor que 1e-15 para entrar en el bucle

    while termino > 1e-15:
        numerador = math.factorial(4 * k) * (1103 + 26390 * k)
        denominador = (math.factorial(k) ** 4) * (396 ** (4 * k))
        termino = numerador / denominador
        suma += termino
        k += 1

    pi_estimada = 1 / (suma * (2 * math.sqrt(2) / 9801))
    return pi_estimada

print(estimacion_pi())