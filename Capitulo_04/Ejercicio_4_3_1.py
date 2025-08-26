'''
1. Escribe una función llamada cuadrado que tome un parámetro con nombre t, que es una tortuga. Debería utilizar la tortuga para dibujar un cuadrado.
Escribe una llamada a función que pase a bob como argumento de cuadrado, y luego ejecuta el programa de nuevo.

2. Agrega otro parámetro, con nombre longitud, a cuadrado. Modifica el cuerpo para que la longitud de los lados sea longitud, y luego modifica la llamada a función para poner un segundo argumento. Ejecuta el programa de nuevo. Prueba tu programa con un rango de valores para longitud.
'''
import turtle

def cuadrado(t, longitud):    
    for i in range(4):
        t.fd(longitud)
        t.lt(90)

    print(t)
    turtle.mainloop()

bob = turtle.Turtle()
#cuadrado(bob, 200)

'''
3. Haz una copia de cuadrado y cambia el nombre a poligono. Agrega otro parámetro con nombre n y modifica el cuerpo para que dibuje un polígono regular con n lados.
Pista: los ángulos exteriores de un polígono regular con n lados son de 360/n grados.
'''
def poligono(t, longitud, n):    
    for i in range(n):
        t.fd(longitud)
        t.lt(360/n)

    print(t)
    turtle.mainloop()

bob = turtle.Turtle()
#poligono(bob, 200, 5)

'''
4. Escribe una función llamada circulo que tome una tortuga, t, y radio, r, como parámetros y dibuje un círculo aproximado llamando a poligono con una longitud y número de lados apropiado. Prueba tu función con un rango de valores de r.
Pista: averigua cuál es el perímetro del círculo y asegúrate de que se cumpla que
longitud * n = perimetro.
'''
def circulo(t, r):
    n = 50
    perimetro = 2 * 3.1416 * r
    longitud = perimetro / n
    poligono(t, longitud, n)    
    
bob = turtle.Turtle()
#circulo(bob, 50)

'''
5. Haz una versión más general de circulo llamada arco que tome un parámetro adicional, angulo, que determine qué fracción de un círculo dibujar. angulo está en grados, así que cuando angulo=360, arco debería dibujar un círculo completo.
'''

def arco (t, r, angulo):
    n = 50
    perimetro = 2 * 3.1416 * r
    l_arco = perimetro * (angulo/360)
    longitud = l_arco / n
    giro = angulo / n
    for i in range(n):
        t.fd(longitud)
        t.lt(giro)
    turtle.mainloop()
    
bob = turtle.Turtle()
arco(bob, 50, 180)