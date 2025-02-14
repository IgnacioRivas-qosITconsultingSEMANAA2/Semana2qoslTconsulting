
'''
**Nota:** Estos ejercicios son optativos para hacer al final de la unidad y están pensados para apoyar tu aprendizaje.

1. Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos 
(es suficiente con mostrar True o False):
   - Si los dos números son iguales
   - Si los dos números son diferentes
   - Si el primero es mayor que el segundo
   - Si el segundo es mayor o igual que el primero

**Ejemplo de ejecución:**
```
Introduce un número entero: 2
Introduce otro número entero: 2
Son los dos números iguales: True
Son los dos números diferentes: False
El primero es mayor que el segundo: False
El segundo es mayor o igual que el primero: True
'''
'''
numero_primero = input("Introduce un numero cualquiera: ")

numero_segundo = input("Introduce un segundo numero cualquiera: ")

print("Los dos numeros son iguales : ", numero_primero == numero_segundo)
print("Los dos numeros son diferentes : " , numero_segundo != numero_primero)
print("El primer numero es mayor que el segundo : ", numero_primero > numero_segundo )
print("El segundo numero es mayor o igual que el primero : " , numero_segundo >= numero_primero)
'''

'''
2. Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario 
tiene una longitud mayor o igual que 3 y a su vez es menor que 10 (es suficiente con mostrar True o False).

'''
'''

resultado = ""

cadena = str(input("Introduce una cadena de texto :  "))

if len(cadena ) >= 3 and len(cadena) > 10 :
    resultado= True
else:
    resultado = False

print(resultado)
'''
'''
Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:

Guarda en una variable numero_magico el valor 12345679 (sin el 8)

Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9 (asegúrate que es un número)

Multiplica el numero_usuario por 9 en sí mismo

Multiplica el numero_magico por el numero_usuario en sí mismo

Finalmente muestra el valor final del numero_magico por pantalla
'''
'''
numero_magico = 12345679

correcto = False
while not correcto:
    numero_usuario = int(input("Introduce un numero del 1 al 9 : "))
    if numero_usuario in range (1, 9):
        correcto = True
    else: 
        print("Introduce un numero correcto pofavor")
    
numero_usuario = numero_usuario*9

numero_magico = numero_magico*numero_usuario

print("Este es el numero_magico: ", numero_magico)
'''

print("=====================================")
'''
Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:
Mostrar una suma de los dos números.
Mostrar una resta de los dos números (el primero menos el segundo).
Mostrar una multiplicación de los dos números.
En caso de no introducir una opción válida, el programa informará de que no es correcta.
'''

'''
primer_numero= float(input("Introduce el primer numero: "))

segundo_numero = float(input("Introduce el segundo numero: "))



opcion_valida = False

while not opcion_valida:
    print("===Mini calculadora en Python===")
    print("1.- Sumar los dos numeros")
    print("2.- Restar los dos numeros")
    print("3.- Multiplicar los dos numeros")
    print("4.- Salir")

escoger = str(input("Elige una opcion 1 / 2 / 3 / 4 ")).strip()
if escoger == '1':
        resultado = primer_numero + segundo_numero
        print("Resultado: ",resultado)
        print("¿Quieres hacer otra operacion?Y/N")
        escoger = str(input()).strip().lower()
        if escoger == 'y':
            opcionValida = False
        else:
            opcionValida = True
elif escoger == '2':
        resultado = primer_numero - segundo_numero
        print("Resultado: ",resultado)
        print("¿Quieres hacer otra operacion?Y/N")
        escoger = str(input()).strip().lower()
        if escoger == 'y':
            opcionValida = False
        else:
            opcionValida = True
elif escoger == '3':
        resultado = primer_numero*segundo_numero
        print("Resultado: ",resultado)
        print("¿Quieres hacer otra operacion?Y/N")
        escoger = str(input()).strip().lower()
        if escoger == 'y':
            opcionValida = False
        else:
            opcionValida = True
elif escoger == '4':
        print("Saliste del Programa Calculadora")
        opcion_valida == True
else:
        print("Introduce una opción valida 1 / 2 / 3 / 4")
        opcion_valida == False
    
''' 

'''
Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.
'''
'''

impar = False

while not impar:
      numero = int(input("Introduce un numero impar colega: "))
      if numero % 2 != 0:
            impar  =True
            
      else:
            print("Introduce un numero impar maricon")
           
print("El numero", numero, "es impar")

'''
'''
Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100:
Sugerencia: Puedes utilizar las funciones sum() y range() para hacerlo más fácil. El tercer parámetro en la q
función range(inicio, fin, salto) indica un salto de números, pruébalo.
'''
'''
resultado=sum(range(0,101,2))
print( "El resultado es: ", resultado)

'''
'''
Realiza un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética.
'''
'''
cantidad = int(input("Cantidad de numeros que quieres introducir"))
suma = 0 
for x in range(cantidad):
    numero = float(input(f"Introduce el numero: {x+1}"))
    suma += numero

resultado = suma/cantidad
print("Media Aritmética: ",resultado)
'''

'''
Enunciado 1:
Realiza una función llamada area_rectangulo() que devuelva el área del rectángulo a partir de su base y altura. Calcula el área de un rectángulo de 15 de base y 10 de altura.
Nota: El área de un rectángulo es el resultado de multiplicar la base por la altura.
'''


base = 15
altura = 10

def area_rectangulo(num1, num2 ) :
    return num1 * num2
resultado = area_rectangulo(base, altura)
print("El area del rectangulo es: " , resultado)

print("=====================================")

'''
Enunciado 2:
Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de su radio. Calcula el área de un círculo de 5 de radio.
Nota: Usa la librería de una sola línea para obtener el área y el radio y multiplicación al resultado por el número pi. Puedes utilizar el valor de π del módulo math:
'''

radio = 5

def area_circulo(radio):
    return 3.1416 * radio** 2
resultado = area_circulo(radio)
print("El area del circulo es: ", resultado)



print("=====================================")
'''
Enunciado 3:
Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:

Si el primer número es mayor que el segundo, debe devolver 1.
Si el primer número es menor que el segundo, debe devolver -1.
Si ambos números son iguales, debe devolver un 0.
Nota: Comprueba la relación entre los números: 5 y 10, 10 y 5 y 5 y 5.

'''

# Completa el ejercicio aquí
primerNumero = 5
segundoNumero = 10

def relacion(num1,num2):
    if num1 > num2:
        return 1
    elif num2 > num1:
        return -1
    else:
        return 0

primerResultado = relacion(5,10)
segundoResultado = relacion(10,5)
tercerResultado = relacion(5,5)

print(primerResultado)
print(segundoResultado)
print(tercerResultado)
print("=====================================")

'''
Enunciado 4:
Realiza una función llamada intermedio() que a partir de dos números, devuelva su punto intermedio.
Nota: El punto intermedio de dos números corresponde a la suma de los números dividida entre 2.
Comprueba el punto intermedio entre -12 y 24.
'''



primerNumero = -12
segundoNumero = 24

def intermedio(num1,num2):
    return(num1 + num2) / 2
resultado = intermedio(primerNumero, segundoNumero)

print("El punto intermedio es: " , resultado)

print("=====================================")
'''

Enunciado 5:
Realiza una función llamada recortar() que reciba tres parámetros. El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. La función tendrá que cumplir lo siguiente:

Devolver el límite inferior si el número es menor que este.
Devolver el límite superior si el número es mayor que este.
Devolver el número sin cambios si no supera ningún límite.
Comprueba el resultado de recortar 15 entre los límites 0 y 10.
'''
# Completa el ejercicio aquí

def recortar(recorte,limIn,limSup):
    if limIn > recorte:
        return limIn
    elif limSup < recorte:
        return limSup
    else:
        return recorte

numeroRecorte = 15
limiteInferior=0
limiteSuperior=10

resultado = recortar(15,0,10)

print("Resultado: ",resultado)
print("=====================================")

'''
Enunciado 6:
Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.
'''



numeros = [-12, 84, 13, 20, -33, 101, 9]

# Completa el ejercicio aquí
def separar(lista):
    listaPar=[]
    listaImpar=[]
    for i in lista:
        if (i % 2==0):
            listaPar.append(i)
        else:
            listaImpar.append(i)
    listaPar.sort()
    listaImpar.sort()

    resultado= f"Pares: {listaPar} \nImpares {listaImpar}"
    return resultado

resultado = separar(numeros)

print(resultado)
    
        
