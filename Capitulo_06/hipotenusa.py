'''
Como ejercicio, utiliza desarrollo incremental para escribir una función llamada hipotenusa que devuelva el largo de la hipotenusa de un triángulo rectánculo, dadas las longitudes de los otros dos lados como argumentos. Guarda cada etapa del proceso de desarrollo a medida que avances.


Pasos para calcular la hipotenusa:
Identifica los catetos: Los catetos son los dos lados que forman el ángulo recto del triángulo. 
Eleva al cuadrado ambos catetos: Multiplica cada longitud del cateto por sí misma (a² y b²). 
Suma los resultados: Suma los dos valores que obtuviste en el paso anterior (a² + b²). 
Saca la raíz cuadrada: La raíz cuadrada de esta suma te dará la longitud de la hipotenusa (c). 
'''
import math
def hipotenusa(a,b):
    ax = a ** 2
    bx = b ** 2
#    print(f'ax: {ax} bx: {bx}')
    suma_x = ax + bx
#       print (f'Suma: {suma_x}')
    hipotenusa = math.sqrt(suma_x)
#    print (f'Hipotenusa: {hipotenusa}')
    return hipotenusa

#hipotenusa(3,4)