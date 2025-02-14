'''
1.- Escribe un programa que pida por teclado un día de la semana y que diga qué asignatura toca a primera hora ese
día.
'''

dia = input("Introduce un día de la semana: ")

if dia == "Lunes":
    print("Toca programacion")
elif dia == "Martes":
    print("Toca sistemas")
elif dia == "Miercoles":
    print("Toca Sostenibilidad")
elif dia == "Jueves":
    print("Toca digitalizacion")
elif dia == "Viernes":
    print("Toca FOL")



'''
2.- Realiza un programa que pida una hora por teclado y que muestre luego buenos días, buenas tardes o buenas
noches según la hora. Se utilizarán los tramos de 6 a 12, de 13 a 20 y de 21 a 5 respectivamente. Sólo se tienen en
cuenta las horas, los minutos no se deben introducir por teclado.
'''


hora = int(input("Introduce una hora (0-23): "))

if 6 <= hora <= 12:
    print("Buenos días")
elif 13 <= hora <= 20:
    print("Buenas tardes")
elif (21 <= hora <= 23) or (0 <= hora <= 5):
    print("Buenas noches")
else:
    print("Hora no válida")
'''
3.- Escribe un programa que calcule el salario semanal de un trabajador teniendo en cuenta que las horas ordinarias
(40 primeras horas de trabajo) se pagan a 12 euros la hora. A partir de la hora 41, se pagan a 16 euros la hora.

'''

horas_trabajada = int(input("Introduce las horas trabajadas: "))

if horas_trabajada <= 40:
    salario = horas_trabajada * 12
else:
    salario = 40 * 12 + (horas_trabajada - 40) * 16

print("El salario es de: ", salario)

'''
4-Escribe un programa que nos diga el horóscopo a partir del día y el mes de nacimiento.
'''

mes_nacimiento = str(input("Introduce tu mes de nacimiento:  "))

dia_nacimiento = int(input("Introduce tu dia de nacimiento: "))


if mes_nacimiento == "Enero":
    if dia_nacimiento < 21:
        print("Capricornio")
    else:
        print("Acuario")
elif mes_nacimiento == "Febrero":
    if dia_nacimiento < 20:
        print("Acuario")
    else:
        print("Piscis")
elif mes_nacimiento == "Marzo": 
    if dia_nacimiento < 21:
        print("Piscis")
    else:
        print("Aries")
elif mes_nacimiento == "Abril":
    if dia_nacimiento < 21:
        print("Aries")
    else:
        print("Tauro")
elif mes_nacimiento == "Mayo":
    if dia_nacimiento < 21:
        print("Tauro")
    else:
        print("Geminis")

elif mes_nacimiento == "Junio":
    if dia_nacimiento < 21:
        print("Geminis")
    else:
        print("Cancer")
elif mes_nacimiento == "Julio":
    if dia_nacimiento < 23:
        print("Cancer")
    else:
        print("Leo")
elif mes_nacimiento == "Agosto":
    if dia_nacimiento < 23:
        print("Leo")
    else:
        print("Virgo")
elif mes_nacimiento == "Septiembre":
    if dia_nacimiento < 23:
        print("Virgo")
    else:
        print("Libra")  
elif mes_nacimiento == "Octubre":
    if dia_nacimiento < 23:
        print("Libra")
    else:
        print("Escorpio")
elif mes_nacimiento == "Noviembre":
    if dia_nacimiento < 23:
        print("Escorpio")
    else:
        print("Sagitario")
elif mes_nacimiento == "Diciembre":
    if dia_nacimiento < 22:
        print("Sagitario")
    else:
        print("Capricornio")
else:
    print("Mes no válido")


'''
5-Escribe un programa que dada una hora determinada (horas y minutos), calcule los segundos que faltan para llegar
a la medianoche.
'''







'''
6- Escribe un programa que ordene tres números enteros introducidos por teclado.
'''




'''
7-Escribe un programa que diga cuál es la última cifra de un número entero introducido por teclado.
'''




'''
8- Escribe un programa que diga cuál es la primera cifra de un número entero introducido por teclado. Se permiten
números de hasta 5 cifras.
'''

numero = int(input("Introduce un número entero: "))
if numero < 10:
    print("La primera cifra es: ", numero)
else:
    if numero < 100:
        print("La primera cifra es: ", numero // 10)
    elif numero < 1000:
        print("La primera cifra es: ", numero // 100)
    elif numero < 10000:
        print("La primera cifra es: ", numero // 1000)
    else:
        print("El número es demasiado largo")



'''
9- Realiza un programa que nos diga cuántos dígitos tiene un número entero que puede ser positivo o negativo. Se
permiten números de hasta 5 dígitos.
'''





'''
10-Realiza un programa que diga si un número entero positivo introducido por teclado es capicúa. Se permiten
números de hasta 5 cifras.
'''