# proyecto: cumpleaños
# Autor: Yenny Lluviza Alvarado Morales
# carnet: 15196-20
# Lo que hace este programa es que encuentra la edad de una persona en pase a la fecha de nacimiento 

from datetime import date

# la fecha de hoy 
hoy = date.today()

#  obtener el dia de hoy 
dia = hoy.day

# obtener el mes de hoy 
mes = hoy.month

# obtener el año de hoy 
year = hoy.year

# Recaudar los datos de la persona
print('Hola, hoy vamos a calcular tu edad actual')

# tenemos que saber el nombre comleto de la persona
nombres = input('Cual es tu nombre: ')
apellidos = input('Cuales son tus apellidos: ')

# tenemos que saber el dia de nacimiento de la persona
dia_naci = input('¿Cual es el dia en el que naciste? ')
dia_naci = int(dia_naci)

# tenemos que saber el mes en que nacio la persona
mes_naci = input('¿Cual es el mes en que naciste? ')
mes_naci = int(mes_naci)

# tenemos que saber el año en el que nacio la persona 
year_naci = input('¿Cual es el año en el que naciste? ')
year_naci = int(year_naci)

# bueno ahora tenemos que restar el año actual con la fecha de cumpleaños de la persona

diff_year = year - year_naci
diff_dia = dia - dia_naci
diff_mes = mes - mes_naci
diff_year -= ((mes , dia) < (mes_naci , dia_naci))

# string - cadena - str

print('Bueno lo logramos ya sabemos tu edad tienes '  + str(diff_year) + ' años ' + str(diff_mes) + ' meses ' + str(diff_dia) + ' dias ')
