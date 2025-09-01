'''
Ejercicio 5.4. ¿Cuál es la salida del siguiente programa? Dibuja un diagrama de pila que muestre el estado del programa cuando imprime el resultado.

def recursivo(n, s):
if n == 0:
print(s)
else:
recursivo(n-1, n+s)
recursivo(3, 0)

1. ¿Qué ocurriría si llamas a esta función así: recursivo(-1, 0)?
2. Escribe un docstring que explique todo lo que alguien necesitaría saber para utilizar esta función (y nada más).
'''
def recursivo(n, s):
    if n == 0:
        print(s)
    else:
        recursivo(n-1, n+s)

recursivo(3, 0)
# 1. Si llamas a la función recursivo(-1, 0) entraría en un bucle infinito ya que n nunca llegaría a ser 0.
# 2. Esta función toma dos argumentos: n, un número entero, y s, una suma acumulativa. La función imprime la suma acumulativa cuando n es 0, y de lo contrario, llama a sí misma con n-1 y n+s.
