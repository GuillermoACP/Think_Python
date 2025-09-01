'''
Ejercicio 5.2. El Último Teorema de Fermat dice que no hay enteros positivos a, b y c tales que
an + bn = cn
para cualquier valor de n mayor que 2.
1. Escribe una función con nombre comprobar_fermat que tome cuatro parámetros —a, b, c
y n— y compruebe si se cumple el teorema de Fermat. Si n es mayor que 2 y
an + bn = cn
el programa debería imprimir “¡Oh, no, Fermat se equivocó!”. De lo contrario, el programa
debería imprimir “No, eso no funciona.”
2. Escribe una función que permita al usuario ingresar valores para a, b, c y n, los convierta
a enteros y utilice la función comprobar_fermat para comprobar si violan el teorema de
Fermat.
'''

def comprobar_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print("¡Oh, no, Fermat se equivocó!")
    else:
        print("No, eso no funciona.")

def entrada_usuario():
    a = int(input("Ingrese el valor de a: "))
    b = int(input("Ingrese el valor de b: "))
    c = int(input("Ingrese el valor de c: "))
    n = int(input("Ingrese el valor de n: "))
    comprobar_fermat(a, b, c, n)

entrada_usuario()