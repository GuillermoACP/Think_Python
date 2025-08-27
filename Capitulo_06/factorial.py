def factorial(n):

    if not isinstance (n, int):
        print('El factorial solo esta definido para enteros.')
        return None
    elif n < 0:
        print('El facotrial no esta definido para negativos.')
        return None
    
    espacio = ' ' * (4 * n)
    print (espacio, 'factorial', n)

    if n == 0:
        print(espacio, 'devolviendo 1')
        return 1
    else:
        recursivo = factorial(n-1)  
        resultado = n * recursivo 
        print (espacio, 'delvolviendo', resultado)    
        return resultado

    
print(factorial('fred'))
print(factorial(-2))
print(factorial(5))