'''
Ejercicio 6.2. La función de Ackermann

Escribe una función con nombre ack que evalúe la función de  Ackermann. Utiliza tu función para evaluar ack(3,4), que debería ser 125. ¿Qué ocurre para valores más grandes de m y n? 
'''

def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1,1)
    elif m > 0 and n > 0:
        return ack(m - 1,ack(m,n - 1))
    
print(ack (3,4))
print(ack (9,9))
        
    