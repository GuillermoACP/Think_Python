'''
El módulo time proporciona una función, con el mismo nombre time, que devuelve el tiempo transcurrido desde la Hora Media de Greenwich (GMT) en “la época” (epoch), que es un momento arbitrario usado como punto de referencia. En sistemas UNIX, la época es el 1 de enero de 1970.

>>> import time
>>> time.time()
1437746094.5735958

Escribe un script que lea el tiempo actual y lo convierta a una hora del día en horas, minutos y segundos, además del número de días desde la época.
'''

import time

dias_segundos = (60 * 60) * 24
horas_segundos = 60 * 60
hora_actual = time.time()

dias = int(hora_actual // dias_segundos)
segundos_dia =  int(hora_actual % dias_segundos)

horas = segundos_dia // horas_segundos
minutos = (segundos_dia % horas_segundos) // 60
segundos = segundos_dia % 60

print (f'Tiempo actual desde la empoca: {hora_actual}')
print (f'Dias desde la epoca: {dias}')
print (f'Hora actual del dia {horas}:{minutos}:{segundos}')
