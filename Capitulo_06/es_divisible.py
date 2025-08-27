def es_divisible (x,y):
    if x % y == 0:
#        print('True')
        return True
    else:
#        print('False')
        return False

x = float(input('Numero: '))
y= float(input('Numero: '))
if es_divisible(x, y) == True:
    print('x es divisible por y')
else:
    print('x No es divisble por y')
    
