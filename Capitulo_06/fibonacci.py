def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        resultado = fibonacci(n-1) + fibonacci(n-2)
        print(resultado)
        return resultado
    
fibonacci(10)