'''
Ejercicio 3.2. Un objeto de función es un valor que puedes asignar a una variable o pasarlo como argumento. Por ejemplo, hacer_2veces es una función que toma un objeto de función como argumento y lo llama dos veces:

def hacer_2veces(f):
    f()
    f()

Aquí hay un ejemplo que utiliza hacer_2veces para llamar a una función con nombre imprimir_spam dos veces.

def imprimir_spam():
    print('spam')

hacer_2veces(imprimir_spam)

1. Escribe este ejemplo en un script y pruébalo.
2. Modifica hacer_2veces para que tome dos argumentos, un objeto de función y un valor, y
llame a la función dos veces, pasando al valor como argumento.
3. Copia la definición de impr_2veces, presentada previamente en este capítulo, a tu script.
4. Usa la versión modificada de hacer_2veces para llamar a impr_2veces dos veces, pasando
a 'spam' como argumento.
5. Define una nueva función llamada hacer_4veces que tome un objeto de función y un valor
y llame a la función cuatro veces, pasando al valor como argumento. Debería haber solo dos
sentencias en el cuerpo de esta función, no cuatro
'''

def hacer_2veces(f, valor):
    f(valor)
    f(valor)

def impr_2veces(s):
    print(s)
    print(s)

def hacer_4veces(funcion, valor):
    hacer_2veces(funcion, valor)
    hacer_2veces(funcion, valor)


#hacer_2veces(impr_2veces, "sapm")

hacer_4veces(impr_2veces, "spam")



