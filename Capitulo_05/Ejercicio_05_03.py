'''
Ejercicio 5.3. Si te dan tres palos, podrías ser capaz o no de formar un triángulo. Por ejemplo, si uno de los palos mide 12 pulgadas y los otros dos miden una pulgada, no serás capaz de hacer que los palos cortos se encuentren en el medio. Para tres longitudes cualesquiera, hay una prueba simple para ver si es posible formar un triángulo:
Si cualquiera de las tres longitudes es mayor que la suma de las otras dos, entonces no puedes formar un triángulo. De lo contrario, sí puedes. (Si la suma de dos longitudes es igual a la tercera, forman lo que llaman un triángulo “degenerado”.)

1. Escribe una función con nombre es_triangulo que tome tres enteros como argumentos e imprima “Sí” o “No”, dependiendo de si puedes o no formar un triángulo con palos cuyas longitudes sean los enteros dados.
2. Escribe una función que permita al usuario ingresar tres longitudes de palos, los convierta a enteros y utilice la función es_triangulo para comprobar si los palos con las longitudes dadas pueden formar un triángulo.
'''

def es_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Sí")
    else:
        print("No")

def entrada_usuario():
    a = int(input("Ingrese la longitud del primer palo: "))
    b = int(input("Ingrese la longitud del segundo palo: "))
    c = int(input("Ingrese la longitud del tercer palo: "))
    es_triangulo(a, b, c)

entrada_usuario()